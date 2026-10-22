"""Arma out/entrega.pdf: el deck de Marp seguido de los anexos, con el tope de 10 MB."""

import argparse
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

# La consigna pide "menor a 10 MB": tomamos la lectura más estricta (10^7 bytes).
MAX_BYTES = 10_000_000
PAGE_BREAK = '\n\n<div style="page-break-before: always"></div>\n\n'
CSS = """
@page { size: A4; margin: 18mm;
        @bottom-center { content: "Anexos · página " counter(page);
                         font-size: 9pt; color: #555; } }
body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
       font-size: 11pt; line-height: 1.45; color: #1a1a1a; max-width: none; }
h1, h2, h3, h4, h5, h6 { break-after: avoid; page-break-after: avoid; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4pt; }
h2 { font-size: 14pt; margin-top: 18pt; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 10pt; }
th, td { border: 1px solid #999; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #eee; }
tr { break-inside: avoid; page-break-inside: avoid; }
img { max-width: 100%; }
a.heading-link { color: inherit; text-decoration: none; }
a.annex-start { display: block; font-size: 1pt; line-height: 1pt;
                 color: transparent; text-decoration: none; }
.annex-summary { break-after: page; page-break-after: always;
                 font-size: 10.5pt; line-height: 1.35; }
.annex-summary h2 { margin-top: 10pt; color: #3d472b; }
.annex-summary h3 { font-size: 11pt; margin: 12pt 0 5pt; }
.annex-summary table { font-size: 9.5pt; line-height: 1.3; }
.annex-summary th { background: #e1ecc9; }
.annex-summary strong { color: #3d472b; }
.annex-summary a { color: #3d472b; }
"""


def load_plan_check():
    spec = importlib.util.spec_from_file_location(
        "plan_check", Path(__file__).with_name("plan-check.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def annexes_markdown(root, checker):
    parts = []
    for path in checker.annex_files(root):
        _, body = checker.split_frontmatter(
            path.read_text(encoding="utf-8"), checker.ANNEX_TYPES
        )
        parts.append(body.strip())
    return PAGE_BREAK.join(parts)


def annex_id(path, annexes, fragment=""):
    prefix = f"annex-{annexes.index(path)}"
    return f"{prefix}-{fragment}" if fragment else prefix


def annex_index_html(root, checker, pdf):
    annexes = checker.annex_files(root)
    named = {name.lstrip("/"): dest for name, dest in pdf.named_destinations.items()}
    rows = []
    for path in annexes:
        metadata, body = checker.split_frontmatter(
            path.read_text(encoding="utf-8"), checker.ANNEX_TYPES
        )
        title = metadata.get("title")
        if not title:
            heading = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            if not heading:
                raise ValueError(f"Anexo sin título ni H1: {path.name}")
            title = heading[1]
        anchor = annex_id(path, annexes)
        if anchor not in named:
            raise ValueError(f"Destino de anexo inexistente en PDF: {anchor}")
        page = pdf.get_destination_page_number(named[anchor])
        if page is None or page < 0:
            raise ValueError(f"Página de anexo inexistente: {anchor}")
        rows.append(
            # Chrome no exporta links a anclas que están en otro PDF.
            f'<tr><td><a href="https://caio.invalid/annexes#{anchor}">'
            f"{html.escape(str(title))}</a></td>"
            f"<td>{page + 1}</td></tr>"
        )
    return (
        "<h1>Índice de anexos</h1>"
        "<p>Cada anexo abre con una síntesis ejecutiva. El desarrollo y las "
        "fuentes quedan a continuación. Seleccioná un título para ir a su inicio. "
        "La numeración al pie comienza en el primer anexo.</p>"
        "<table><thead><tr><th>Anexo</th><th>Página de anexos</th></tr></thead>"
        "<tbody>" + "".join(rows) + "</tbody></table>"
    )


def portable_target(root, origin, destination, annexes, public_ref):
    parsed = urlsplit(destination)
    if (
        parsed.scheme
        and parsed.scheme != "file"
        or parsed.netloc
        and parsed.scheme != "file"
    ):
        return destination
    path = unquote(parsed.path)
    if parsed.scheme == "file":
        target = Path(path).resolve()
        # Marp conserva los links absolutos al repo como file:///context/….
        if not target.is_relative_to(root) and path.startswith(
            ("/plan/", "/context/", "/material/", "/defense/", "/private/")
        ):
            target = root / path.lstrip("/")
    elif path.startswith("/"):
        target = root / path.lstrip("/")
    else:
        target = origin.parent / path if path else origin
    target = target.resolve()
    if not target.is_relative_to(root):
        raise ValueError("Enlace local fuera del repo: no se puede publicar")
    relative = target.relative_to(root)
    if relative.parts[0] == "private":
        raise ValueError("Enlace a private/: el build no publica fuentes privadas")
    fragment = unquote(parsed.fragment)
    if target in annexes:
        return "#" + annex_id(target, annexes, fragment)
    if target == root / "plan/slides.md":
        return "https://caio.invalid/slides" + (
            "#" + quote(fragment) if fragment else ""
        )
    return (
        "https://github.com/lazynet/tp-caio-g11-2026/blob/"
        + quote(public_ref, safe="")
        + "/"
        + quote(relative.as_posix(), safe="/")
        + ("#" + quote(fragment) if fragment else "")
    )


def annexes_html(root, checker, public_ref):
    annexes = checker.annex_files(root)
    parts = []
    for path in annexes:
        _, body = checker.split_frontmatter(
            path.read_text(encoding="utf-8"), checker.ANNEX_TYPES
        )
        document = json.loads(
            subprocess.run(
                ["pandoc", "--from=markdown", "--to=json"],
                input=body,
                text=True,
                capture_output=True,
                check=True,
            ).stdout
        )

        def transform(node):
            if isinstance(node, dict):
                if node.get("t") in ("Header", "Div", "Span", "CodeBlock"):
                    attributes = node["c"][1] if node["t"] == "Header" else node["c"][0]
                    if attributes[0]:
                        attributes[0] = annex_id(path, annexes, attributes[0])
                if node.get("t") == "Link":
                    destination = node["c"][2][0]
                    node["c"][2][0] = portable_target(
                        root, path, destination, annexes, public_ref
                    )
                    if node["c"][2][0] == "https://caio.invalid/slides":
                        label = " ".join(
                            item.get("c", "")
                            for item in node["c"][1]
                            if item.get("t") == "Str"
                        )
                        match = re.search(r"\bSlide (\d+)\b", label)
                        if match:
                            node["c"][2][0] += f"#page-{match[1]}"
                for value in node.values():
                    transform(value)
            elif isinstance(node, list):
                for value in node:
                    transform(value)

        transform(document)
        rendered = subprocess.run(
            ["pandoc", "--from=json", "--to=html"],
            input=json.dumps(document),
            text=True,
            capture_output=True,
            check=True,
        ).stdout
        # Las notas al pie que Pandoc agrega al renderizar también necesitan
        # ids únicos para no saltar a una nota de otro anexo.
        rendered = re.sub(
            r'(id="|href="#)(?!annex-)([^"]+)',
            lambda match: match[1] + annex_id(path, annexes, match[2]),
            rendered,
        )
        # Chrome solo exporta destinos que reciben un link. El título se
        # enlaza a sí mismo, sin un símbolo visible, para que las slides del
        # deck puedan apuntar a cada sección.
        rendered = re.sub(
            r'(<h([1-6]) id="([^"]+)"[^>]*>)(.*?)(</h\2>)',
            lambda match: (
                match[1]
                + f'<a class="heading-link" href="#{match[3]}">{match[4]}</a>'
                + match[5]
            ),
            rendered,
            flags=re.DOTALL,
        )
        start = annex_id(path, annexes)
        parts.append(
            f'<div id="{start}"><a class="annex-start" href="#{start}"'
            f' aria-hidden="true">&nbsp;</a>{rendered}</div>'
        )
    return PAGE_BREAK.join(parts)


def slide_destinations(root, checker):
    _, body = checker.split_frontmatter(
        (root / "plan/slides.md").read_text(encoding="utf-8")
    )
    slides = re.split(
        r"^ {0,3}(?:---|\*\*\*)[ \t]*$", checker.visible(body), flags=re.MULTILINE
    )
    destinations = {"": 0}
    counts = {}
    for page, slide in enumerate(slides):
        destinations[f"page-{page + 1}"] = page
        for line in slide.splitlines():
            for anchor in checker.anchors(line):
                count = counts.get(anchor, 0)
                counts[anchor] = count + 1
                destinations[f"{anchor}-{count}" if count else anchor] = page
    return destinations


def rewrite_pdf_links(writer, root, annexes, slides, public_ref):
    from pypdf.generic import ArrayObject, DictionaryObject, NameObject

    named = {
        name.lstrip("/"): destination
        for name, destination in writer.named_destinations.items()
    }
    for page in writer.pages:
        for reference in page.get("/Annots", []):
            annotation = reference.get_object()
            action = annotation.get("/A")
            if not action or action.get("/S") != "/URI":
                continue
            uri = str(action.get("/URI", ""))
            if uri.startswith("https://caio.invalid/annexes#"):
                uri = "#" + unquote(urlsplit(uri).fragment)
            if urlsplit(uri).scheme == "file":
                uri = portable_target(
                    root, root / "plan/slides.md", uri, annexes, public_ref
                )
            if uri.startswith("https://caio.invalid/slides"):
                anchor = unquote(urlsplit(uri).fragment)
                if anchor not in slides:
                    raise ValueError(f"Destino de slide inexistente: {anchor}")
                destination = ArrayObject(
                    [
                        writer.pages[slides[anchor]].indirect_reference,
                        NameObject("/Fit"),
                    ]
                )
            elif uri.startswith("#annex-"):
                anchor = uri[1:]
                if anchor not in named:
                    raise ValueError(f"Destino de anexo inexistente en PDF: {anchor}")
                destination = named[anchor].dest_array
            else:
                from pypdf.generic import TextStringObject

                action[NameObject("/URI")] = TextStringObject(uri)
                continue
            annotation.pop("/Dest", None)
            annotation[NameObject("/A")] = DictionaryObject(
                {NameObject("/S"): NameObject("/GoTo"), NameObject("/D"): destination}
            )


def check_portable_pdf(pdf):
    for page in pdf.pages:
        for reference in page.get("/Annots", []):
            action = reference.get_object().get("/A", {})
            uri = str(action.get("/URI", ""))
            if urlsplit(uri).scheme == "file" or uri.startswith(
                "https://caio.invalid/"
            ):
                raise ValueError(
                    "entrega.pdf conserva un enlace file:// o un destino interno sin resolver"
                )


def size_error(size):
    if size >= MAX_BYTES:
        return (
            f"entrega.pdf pesa {size:,} bytes y la consigna pide menos de "
            f"{MAX_BYTES:,}: achicá imágenes o anexos"
        )
    return None


def find_chrome():
    # Marp respeta la misma variable, así que una sola configuración sirve para los dos.
    if os.environ.get("CHROME_PATH"):
        return os.environ["CHROME_PATH"]
    for name in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "microsoft-edge",
        "msedge",
        "chrome",
    ):
        found = shutil.which(name)
        if found:
            return found
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for base in (os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)")):
        if base:
            candidates += [
                f"{base}/Google/Chrome/Application/chrome.exe",
                f"{base}/Microsoft/Edge/Application/msedge.exe",
            ]
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    raise SystemExit("No encontré Chrome, Edge o Chromium: definí CHROME_PATH")


def render_annexes(root, markup, pdf, *, numbered=True):
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        css, html = temp / "annexes.css", temp / "annexes.html"
        css.write_text(
            CSS if numbered else CSS + "\n@page { @bottom-center { content: none; } }",
            encoding="utf-8",
        )
        subprocess.run(
            [
                "pandoc",
                "--from=html",
                "--standalone",
                "--embed-resources",
                f"--resource-path={root / 'plan/annexes'}",
                f"--css={css}",
                "--metadata=pagetitle:Anexos",
                f"--output={html}",
            ],
            input=markup,
            text=True,
            check=True,
        )
        pdf.unlink(missing_ok=True)
        chrome = subprocess.Popen(
            [
                find_chrome(),
                "--headless",
                "--disable-gpu",
                "--no-first-run",
                f"--user-data-dir={temp / 'chrome'}",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf}",
                html.as_uri(),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # Chrome headless a veces escribe el pdf y no termina: cuando el archivo
        # deja de crecer, lo cerramos nosotros.
        last, deadline = -1, time.monotonic() + 120
        while chrome.poll() is None and time.monotonic() < deadline:
            time.sleep(1)
            size = pdf.stat().st_size if pdf.is_file() else 0
            if size and size == last:
                break
            last = size
        if chrome.poll() is None:
            chrome.terminate()
            chrome.wait(timeout=10)
    if not pdf.is_file() or not pdf.stat().st_size:
        raise SystemExit("Chrome no generó el pdf de los anexos")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--deck", type=Path, default=Path("out/deck-marp.pdf"))
    parser.add_argument("--output", type=Path, default=Path("out/entrega.pdf"))
    args = parser.parse_args()
    root = args.root.resolve()
    deck = args.deck if args.deck.is_absolute() else root / args.deck
    output = args.output if args.output.is_absolute() else root / args.output
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        raise SystemExit("build-delivery necesita pypdf: instalalo en el .venv")
    if not deck.is_file():
        raise SystemExit(f"No existe {deck}: generalo con build-deck.sh marp")

    checker = load_plan_check()
    public_ref = os.environ.get("CAIO_PUBLIC_REF", "main")
    if not public_ref.strip():
        raise SystemExit("CAIO_PUBLIC_REF no puede estar vacío")
    try:
        markup = annexes_html(root, checker, public_ref)
    except ValueError as exc:
        raise SystemExit(str(exc))
    writer = PdfWriter()
    writer.append(str(deck))
    if markup:
        annexes_pdf = output.with_name("anexos.pdf")
        render_annexes(root, markup, annexes_pdf)
        index_pdf = output.with_name("indice-anexos.pdf")
        try:
            index_markup = annex_index_html(root, checker, PdfReader(annexes_pdf))
        except ValueError as exc:
            raise SystemExit(str(exc))
        render_annexes(root, index_markup, index_pdf, numbered=False)
        if len(PdfReader(index_pdf).pages) != 1:
            raise SystemExit("El índice de anexos tiene que ocupar una sola página")
        writer.append(str(index_pdf))
        writer.append(str(annexes_pdf))
    else:
        print("Aviso: no hay anexos en plan/annexes/; la entrega lleva solo el deck")
    try:
        rewrite_pdf_links(
            writer,
            root,
            checker.annex_files(root),
            slide_destinations(root, checker),
            public_ref,
        )
        check_portable_pdf(writer)
    except ValueError as exc:
        raise SystemExit(str(exc))
    writer.compress_identical_objects()
    with output.open("wb") as handle:
        writer.write(handle)
    check_portable_pdf(PdfReader(output))

    size = output.stat().st_size
    print(f"{output.relative_to(root)}: {len(writer.pages)} páginas, {size:,} bytes")
    error = size_error(size)
    if error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
