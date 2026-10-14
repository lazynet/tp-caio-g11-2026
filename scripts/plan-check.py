"""Chequeo estructural del deck; no certifica madurez ni evidencia de negocio."""

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

DECK_TYPES = (("owner", str), ("status", str), ("marp", bool))
ANNEX_TYPES = (("owner", str), ("status", str), ("title", str))
# board revisa pero no escribe anexos.
ANNEX_OWNERS = ("caio", "architect", "governance", "people", "finance")
# Estructura que pide el equipo docente para que el board vea de dónde sale cada número.
ANNEX_SECTIONS = (
    "Objetivo",
    "Supuestos de partida",
    "Evidencia",
    "Riesgos y mitigación",
    "Decisiones",
)


def evidence_kind(path, root):
    for name in ("context", "material", "defense/evidence"):
        if path.is_relative_to(root / name):
            return "navigation" if path.name == "index.md" else "concept"
    return None


def validate_evidence(root, evidence):
    if not evidence:
        return []
    command = [
        sys.executable,
        str(Path(__file__).with_name("okf-check.py")),
        "--root",
        str(root),
        "--delivery",
    ]
    for path in sorted(evidence):
        command.extend(["--path", str(path.relative_to(root))])
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
    except (OSError, UnicodeError) as exc:
        return [f"Entrega rechazada: no se pudo ejecutar okf-check: {exc}"]
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        return [f"Entrega rechazada por okf-check (exit {result.returncode}): {detail}"]
    return []


def split_frontmatter(text, types=DECK_TYPES):
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Falta frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("Frontmatter sin cierre")
    try:
        import yaml
    except ImportError as exc:
        raise ValueError("plan-check necesita PyYAML también en borrador") from exc

    class UniqueLoader(yaml.SafeLoader):
        pass

    def unique_mapping(loader, node):
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node)
            if key in mapping:
                raise ValueError(f"Clave YAML duplicada: {key}")
            mapping[key] = loader.construct_object(value_node)
        return mapping

    UniqueLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
    )
    try:
        metadata = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
    except (yaml.YAMLError, TypeError) as exc:
        raise ValueError(f"Frontmatter YAML inválido: {exc}") from exc
    if not isinstance(metadata, dict):
        raise ValueError("El frontmatter debe ser un mapping YAML")
    for key, expected in types:
        if type(metadata.get(key)) is not expected:
            raise ValueError(
                f"Tipo YAML inválido para {key}: se exige {expected.__name__}"
            )
    return metadata, "\n".join(lines[end + 1 :])


def visible(text):
    # Los ejemplos de código no son slides ni referencias navegables.
    text = re.sub(
        r"<!--.*?(?:-->|\Z)",
        lambda match: "\n" * match[0].count("\n"),
        text,
        flags=re.DOTALL,
    )
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            result.append("")
        else:
            result.append(line if fence is None else "")
    text = "\n".join(result)
    return re.sub(
        r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)",
        lambda match: re.sub(r"[^\n]", "\ufffc", match[0]),
        text,
        flags=re.DOTALL,
    )


def local_html_links(text):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            for key, destination in attrs:
                if key in ("href", "src") and destination is not None:
                    parsed = urlsplit(destination.strip())
                    if not parsed.scheme and not parsed.netloc and parsed.path:
                        destinations.append(destination)

    destinations = []
    LinkParser().feed(visible(text))
    return destinations


def anchors(text):
    result, counts = set(), {}
    for heading in re.findall(
        r"^\s{0,3}#{1,6}\s+(.+?)\s*#*$", visible(text), re.MULTILINE
    ):
        heading = re.sub(r"<[^>]+>", "", heading).lower()
        slug = "".join(
            c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LN"
        )
        slug = slug.replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    result.update(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    result.update(re.findall(r'<a\s+name=["\']([^"\']+)["\']', text))
    return result


def links(text, include_definitions=True):
    text = visible(text)
    definitions = {
        " ".join(key.lower().split()): destination
        for key, destination in re.findall(
            r"^\s{0,3}\[([^\]^]+)\]:\s*<?([^\s>]+)>?", text, re.MULTILINE
        )
    }
    for destination in re.findall(
        r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text
    ):
        yield destination.strip("<>")
    # `[^a][^b]` son dos notas al pie seguidas, no un link por referencia.
    for label, reference in re.findall(r"!?\[(?!\^)([^\]]+)\]\[(?!\^)([^\]]*)\]", text):
        key = " ".join((reference or label).lower().split())
        yield definitions.get(key, f"__undefined_reference__/{key}")
    for key in re.findall(r"\[([^\]^]+)\](?![\[(:])", text):
        key = " ".join(key.lower().split())
        if key in definitions:
            yield definitions[key]
    if include_definitions:
        yield from definitions.values()


def resolve_link(origin, destination, root):
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if path.startswith("/"):
        bundle = next(
            (
                root / name
                for name in ("context", "material", "defense/evidence")
                if origin.is_relative_to(root / name)
            ),
            root,
        )
        target = bundle / path.lstrip("/")
    else:
        target = origin.parent / path if path else origin
    target = target.resolve()
    if not target.is_relative_to(root):
        raise ValueError(f"Referencia fuera del repo: {destination}")
    if not target.is_file():
        raise ValueError(f"Referencia local rota: {destination}")
    if parsed.fragment:
        if target.suffix.lower() != ".md":
            raise ValueError(f"Anchor local no verificable: {destination}")
        if unquote(parsed.fragment) not in anchors(target.read_text(encoding="utf-8")):
            raise ValueError(f"Anchor inexistente: {destination}")
    return target


def annex_files(root):
    # Los archivos con _ adelante (la plantilla) no son anexos ni van a la entrega.
    folder = root / "plan/annexes"
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.glob("*.md") if not p.name.startswith("_"))


def check_annex(path, root, mode):
    name = path.relative_to(root)
    try:
        metadata, body = split_frontmatter(
            path.read_text(encoding="utf-8"), ANNEX_TYPES
        )
    except (OSError, ValueError) as exc:
        return [f"{name}: {exc}"]
    errors = []
    if metadata["owner"] not in ANNEX_OWNERS:
        errors.append(
            f"{name}: owner del anexo debe ser uno de {', '.join(ANNEX_OWNERS)}"
        )
    if metadata["status"] not in ("draft", "ready"):
        errors.append(f"{name}: el status del anexo debe ser draft o ready")
    if mode == "delivery" and metadata["status"] == "draft":
        errors.append(f"Entrega rechazada: anexo declarado draft: {name}")
    headings = {
        heading.strip().casefold()
        for heading in re.findall(
            r"^\s{0,3}##\s+(.+?)\s*#*$", visible(body), re.MULTILINE
        )
    }
    for section in ANNEX_SECTIONS:
        if section.casefold() not in headings:
            errors.append(f"{name}: falta la sección ## {section}")
    return errors


def check(root, deck, mode):
    root, deck = root.resolve(), deck.resolve()
    errors, pending, references = [], [], set()
    try:
        text = deck.read_text(encoding="utf-8")
        metadata, body = split_frontmatter(text)
    except (OSError, ValueError) as exc:
        return {"slides": 0, "errors": [str(exc)], "pending": [], "references": []}
    if metadata.get("owner") != "caio":
        errors.append("El owner del deck debe ser caio")
    if metadata.get("marp") is not True:
        errors.append("El deck debe declarar marp: true")
    if metadata.get("status") not in ("draft", "ready"):
        errors.append(
            "El status del deck debe ser draft o ready (ready no certifica evidencia)"
        )
    if mode == "delivery" and metadata.get("status") == "draft":
        errors.append("Entrega rechazada: deck declarado draft")
    for line_number, line in enumerate(visible(body).splitlines(), 1):
        if re.fullmatch(
            r" {0,3}(?:-(?:[ \t]*-){2,}|\*(?:[ \t]*\*){2,}|_(?:[ \t]*_){2,})[ \t]*",
            line,
        ):
            if line.strip() not in ("---", "***"):
                errors.append(
                    f"Separador no admitido en cuerpo:{line_number}: usá --- o *** compactos"
                )
    slides = re.split(
        r"^ {0,3}(?:---|\*\*\*)[ \t]*$", visible(body), flags=re.MULTILINE
    )
    count = len(slides)
    if count > 10:
        errors.append(
            f"Máximo 10 slides incluyendo portada y equipo; encontradas {count}"
        )
    if any(not slide.strip() for slide in slides):
        errors.append("Hay slides vacías")
    queue, seen, documents, edges = [(deck, text)], set(), {}, {}
    while queue:
        origin, content = queue.pop(0)
        if origin in seen:
            continue
        seen.add(origin)
        documents[origin] = content
        edges[origin] = set()
        for destination in local_html_links(content):
            errors.append(
                f"{origin.relative_to(root)}: Enlace HTML local no admitido: {destination}; usá Markdown"
            )
        used_links = set(links(content, include_definitions=False))
        for destination in links(content):
            try:
                target = resolve_link(origin, destination, root)
                if target is not None:
                    references.add(str(target.relative_to(root)))
                    if target.suffix.lower() == ".md" and destination in used_links:
                        edges[origin].add(target)
                    if target.suffix.lower() == ".md" and target not in seen:
                        queue.append((target, target.read_text(encoding="utf-8")))
            except (OSError, ValueError) as exc:
                errors.append(f"{origin.relative_to(root)}: {exc}")
    # La navegación conserva el chequeo de links, pero no amplía el respaldo.
    delivered, evidence, queue = set(), set(), [deck]
    while queue:
        origin = queue.pop()
        if origin in delivered:
            continue
        delivered.add(origin)
        for target in edges.get(origin, ()):
            kind = evidence_kind(target, root)
            if kind == "concept":
                evidence.add(target)
            elif kind is None:
                queue.append(target)
    for origin in sorted(delivered | evidence):
        for line_number, line in enumerate(
            visible(documents.get(origin, "")).splitlines(), 1
        ):
            if re.search(
                r"\b(pendiente\w*|TODO|TBD|FIXME|por definir|falta evidencia|sin evidencia|esqueleto)\b",
                line,
                re.IGNORECASE,
            ):
                pending.append(
                    f"{origin.relative_to(root)}:{line_number}: {line.strip()}"
                )
    for annex in annex_files(root):
        errors.extend(check_annex(annex, root, mode))
        if mode == "delivery" and str(annex.relative_to(root)) not in references:
            errors.append(
                f"Entrega rechazada: anexo no referenciado desde el deck: {annex.relative_to(root)}"
            )
    if mode == "delivery" and pending:
        errors.extend(f"Entrega rechazada por pendiente: {item}" for item in pending)
    if mode == "delivery":
        errors.extend(validate_evidence(root, evidence))
    return {
        "slides": count,
        "errors": errors,
        "pending": pending,
        "references": sorted(references),
        "evidence": sorted(str(path.relative_to(root)) for path in evidence),
    }


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Solo valida fichas enlazadas desde documentos entregados; índices y links "
        "relacionados son navegación. No detecta cifras sin cita ni juzga semántica: "
        "se requieren board y revisión humana. ready solo descarta borrador explícito.",
    )
    parser.add_argument("--mode", choices=("draft", "delivery"), default="draft")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--deck", type=Path, default=Path("plan/slides.md"))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    deck = args.deck if args.deck.is_absolute() else args.root / args.deck
    if not deck.resolve().is_relative_to(args.root.resolve()):
        parser.error("El deck debe estar dentro del repo")
    result = check(args.root, deck, args.mode)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            f"plan-check ({args.mode}): {result['slides']} slides; {len(result['pending'])} pendientes; {len(result['references'])} referencias locales"
        )
        for error in result["errors"]:
            print(f"ERROR: {error}")
        if not result["errors"]:
            print("OK: estructura válida; evidencia humana y madurez no certificadas")
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
