"""Genera la guía de defensa aparte del PDF de entrega, desde sus fuentes canónicas."""

import argparse
from datetime import date
from html import escape
from html.parser import HTMLParser
import importlib.util
import os
from pathlib import Path
import tempfile
from urllib.parse import unquote

spec = importlib.util.spec_from_file_location(
    "build_delivery", Path(__file__).with_name("build-delivery.py")
)
delivery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delivery)

OUTPUT = Path("out/Grupo11-AcmeLabs-Defensa.pdf")
SOURCES = ("storyline.md", "speech-presentacion.md", "objeciones.md")
CHAPTERS = (
    ("Guion argumental", "annex-0"),
    ("Speech por diapositiva", "annex-1"),
    ("Preparación del ensayo", "annex-1-preparación-del-ensayo-propuesta"),
    ("Banco de objeciones", "annex-2"),
)
CSS = (
    delivery.CSS.replace("Anexos · página ", "Defensa · página ")
    + """
@page { margin: 17mm 17mm 19mm; }
@page portada { @bottom-center { content: none; } }
body { font-size: 10.5pt; line-height: 1.4; }
#annex-0 { font-size: 10pt; line-height: 1.35; }
#annex-1 { font-size: 10.3pt; line-height: 1.35; }
#annex-1 table { font-size: 8.8pt; line-height: 1.25; }
#annex-1 th, #annex-1 td { padding: 4pt; }
h1, h2, h3 { color: #3d472b; }
h1 { border-color: #3d472b; }
a { color: #475e2b; overflow-wrap: anywhere; }
th { background: #e1ecc9; }
p { orphans: 3; widows: 3; }
table { font-size: 9pt; line-height: 1.35; }
thead { display: table-header-group; }
th, td { padding: 5pt; border-color: #bcc4b3; }
#annex-2 table { table-layout: fixed; }
#annex-2 th:first-child, #annex-2 td:first-child { width: 5%; }
#annex-2 th:nth-child(2), #annex-2 td:nth-child(2) { width: 22%; }
#annex-2 th:nth-child(3), #annex-2 td:nth-child(3) { width: 58%; }
#annex-2 th:nth-child(4), #annex-2 td:nth-child(4) { width: 15%; }
#annex-2 table:first-of-type { table-layout: auto; }
#annex-2 table:first-of-type th, #annex-2 table:first-of-type td { width: auto; }
#annex-1-preparación-del-ensayo-propuesta { break-before: page; page-break-before: always; }
.cover { page: portada; padding-top: 36mm; }
.cover h1 { font-size: 35pt; line-height: 1.1; border: 0; margin: 18pt 0; }
.cover .eyebrow { text-transform: uppercase; letter-spacing: 2pt; font-size: 11pt; color: #475e2b; }
.cover .subtitle { font-size: 17pt; }
.cover .navigation { margin: 30pt 0; padding: 16pt 20pt; background: #e1ecc9; }
.cover .navigation p { margin: 7pt 0; }
.cover .note { color: #555; font-size: 10pt; }
"""
)


class InternalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.targets = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.targets.add(unquote(attrs["href"][1:]))


def defense_target(root, origin, destination, documents, public_ref):
    target = delivery.portable_target(root, origin, destination, documents, public_ref)
    return target.replace(
        "https://caio.invalid/slides",
        "https://github.com/lazynet/tp-caio-g11-2026/blob/"
        + delivery.quote(public_ref, safe="")
        + "/plan/slides.md",
    )


def defense_html(root, public_ref):
    documents = [
        (root / "defense" / name, (root / "defense" / name).read_text(encoding="utf-8"))
        for name in SOURCES
    ]
    navigation = "".join(
        f'<p><a href="#{target}">{i}. {title}</a></p>'
        for i, (title, target) in enumerate(CHAPTERS, 1)
    )
    cover = f"""<section class="cover">
<p class="eyebrow">Acme Labs · Grupo 11</p>
<h1>Preparación de<br>la defensa</h1>
<p class="subtitle">Plan Maestro CAIO</p>
<p>Documento de apoyo separado de la entrega</p>
<div class="navigation">{navigation}</div>
<p class="note">Versión de trabajo · {date.today().isoformat()}<br>
Fuentes canónicas del repositorio · referencia {escape(public_ref)}.</p>
<p class="note">El reparto de voces y la duración requieren acuerdo del equipo.
La preparación del ensayo es una propuesta; no acredita un ensayo realizado.</p>
</section>"""
    markup = (
        cover
        + delivery.PAGE_BREAK
        + delivery.documents_html(
            root, documents, public_ref, link_resolver=defense_target
        )
    )
    links = InternalLinks()
    links.feed(markup)
    missing = links.targets - links.ids
    if missing:
        raise ValueError(
            "Destinos de defensa inexistentes: " + ", ".join(sorted(missing))
        )
    return markup


def build(root, public_ref):
    from pypdf import PdfReader, PdfWriter

    if not public_ref.strip():
        raise ValueError("CAIO_PUBLIC_REF no puede estar vacío")
    markup = defense_html(root, public_ref)
    output = root / OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    # Se publica solo tras validar: un error conserva la guía anterior.
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        raw = Path(temp) / "raw.pdf"
        delivery.render_annexes(root, markup, raw, css_text=CSS)
        reader = PdfReader(raw)
        writer = PdfWriter()
        writer.clone_document_from_reader(reader)
        destinations = {
            unquote(str(name).lstrip("/")): target
            for name, target in reader.named_destinations.items()
        }
        for title, target in CHAPTERS:
            if target not in destinations:
                raise ValueError(f"Destino de defensa inexistente en PDF: {target}")
            writer.add_outline_item(
                title, reader.get_destination_page_number(destinations[target])
            )
        writer.add_metadata(
            {
                "/Title": "Grupo 11 · Acme Labs — Preparación de la defensa",
                "/Author": delivery.PDF_AUTHOR,
                "/Subject": "Guion, speech, objeciones y ensayo · " + public_ref,
            }
        )
        delivery.check_portable_pdf(writer)
        final = Path(temp) / "defense.pdf"
        with final.open("wb") as stream:
            writer.write(stream)
        delivery.check_portable_pdf(PdfReader(final))
        final.replace(output)
    print(f"{OUTPUT}: {len(reader.pages)} páginas, {output.stat().st_size:,} bytes")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    try:
        build(args.root.resolve(), os.environ.get("CAIO_PUBLIC_REF", "main"))
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
