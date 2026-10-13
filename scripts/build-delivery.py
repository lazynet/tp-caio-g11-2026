"""Arma out/entrega.pdf: el deck de Marp seguido de los anexos, con el tope de 10 MB."""

import argparse
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# La consigna pide "menor a 10 MB": tomamos la lectura más estricta (10^7 bytes).
MAX_BYTES = 10_000_000
PAGE_BREAK = '\n\n<div style="page-break-before: always"></div>\n\n'
CSS = """
@page { size: A4; margin: 18mm; }
body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
       font-size: 11pt; line-height: 1.45; color: #1a1a1a; max-width: none; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4pt; }
h2 { font-size: 14pt; margin-top: 18pt; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 10pt; }
th, td { border: 1px solid #999; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #eee; }
img { max-width: 100%; }
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


def render_annexes(root, markdown, pdf):
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        css, html = temp / "annexes.css", temp / "annexes.html"
        css.write_text(CSS, encoding="utf-8")
        subprocess.run(
            [
                "pandoc",
                "--from=markdown",
                "--standalone",
                "--embed-resources",
                f"--resource-path={root / 'plan/annexes'}",
                f"--css={css}",
                "--metadata=pagetitle:Anexos",
                f"--output={html}",
            ],
            input=markdown,
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
        from pypdf import PdfWriter
    except ImportError:
        raise SystemExit("build-delivery necesita pypdf: instalalo en el .venv")
    if not deck.is_file():
        raise SystemExit(f"No existe {deck}: generalo con build-deck.sh marp")

    checker = load_plan_check()
    markdown = annexes_markdown(root, checker)
    writer = PdfWriter()
    writer.append(str(deck))
    if markdown:
        annexes_pdf = output.with_name("anexos.pdf")
        render_annexes(root, markdown, annexes_pdf)
        writer.append(str(annexes_pdf))
    else:
        print("Aviso: no hay anexos en plan/annexes/; la entrega lleva solo el deck")
    writer.compress_identical_objects()
    with output.open("wb") as handle:
        writer.write(handle)

    size = output.stat().st_size
    print(f"{output.relative_to(root)}: {len(writer.pages)} páginas, {size:,} bytes")
    error = size_error(size)
    if error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
