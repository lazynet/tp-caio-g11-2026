"""Chequeo estructural del deck; no certifica madurez ni evidencia de negocio."""

import argparse
import hashlib
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
PENDING = re.compile(
    r"\b(TODO|TBD|FIXME|(?i:pendiente\w*|por definir|falta evidencia|sin evidencia|esqueleto))\b"
)
FINDING_CATEGORIES = {
    "required_gap": set(),
    # decision cita el momento/hito de resolución, también si no hay fecha calendario.
    # La competencia de authority y el sentido de las citas requieren revisión editorial.
    "future_decision": {"scope", "authority", "decision", "consequence"},
    "execution_condition": {"scope", "authority", "decision", "consequence"},
    "historical_uncertainty": {"record", "limit"},
    "metadata": set(),
}


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def finding_catalog(root, documents):
    # La clasificación es una revisión editorial versionada, no un juicio de IA.
    path = root / "scripts/delivery-findings.json"
    if not path.exists():
        return {}, []
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=unique_json
        )
        if (
            not isinstance(data, dict)
            or set(data) != {"version", "entries"}
            or type(data["version"]) is not int
            or data["version"] != 1
            or not isinstance(data["entries"], list)
        ):
            raise ValueError("Se exige version: 1 y entries: lista")
        entries = {}

        def location(item, keys):
            if not isinstance(item, dict) or set(item) != keys:
                raise ValueError("Campos de entrada/cita desconocidos o incompletos")
            name, number, text = item["path"], item["line"], item["text"]
            if (
                not isinstance(name, str)
                or not name
                or "\\" in name
                or Path(name).is_absolute()
                or ".." in Path(name).parts
                or any(part.casefold() == "private" for part in Path(name).parts)
                or Path(name).as_posix() != name
                or type(number) is not int
                or number < 1
                or not isinstance(text, str)
                or not text.strip()
                or not isinstance(item["sha256"], str)
                or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"])
            ):
                raise ValueError("Ubicación o texto inválidos")
            return name, number

        def exact(citation):
            name, number = location(citation, {"path", "line", "text", "sha256"})
            content = documents.get(root / name)
            if content is None:
                raise ValueError(f"Cita fuera del alcance exigido: {name}")
            if (
                hashlib.sha256(content.encode("utf-8")).hexdigest()
                != citation["sha256"]
            ):
                raise ValueError(f"Documento modificado desde la clasificación: {name}")
            lines = content.splitlines()
            if (
                "\n".join(
                    lines[number - 1 : number - 1 + len(citation["text"].split("\n"))]
                )
                != citation["text"]
            ):
                raise ValueError(f"Cita modificada o desplazada: {name}:{number}")

        for entry in data["entries"]:
            key = location(
                entry,
                {
                    "path",
                    "line",
                    "text",
                    "sha256",
                    "category",
                    "blocking",
                    "reason",
                    "basis",
                },
            )
            category = entry["category"]
            if (
                not isinstance(category, str)
                or category not in FINDING_CATEGORIES
                or type(entry["blocking"]) is not bool
                or not isinstance(entry["reason"], str)
                or not entry["reason"].strip()
                or not isinstance(entry["basis"], dict)
                or "\n" in entry["text"]
            ):
                raise ValueError(f"Clasificación inválida: {key}")
            if key in entries:
                raise ValueError(f"Detección duplicada: {key}")
            entries[key] = entry
            expected = set() if entry["blocking"] else FINDING_CATEGORIES[category]
            if set(entry["basis"]) != expected:
                raise ValueError(f"Respaldo incompleto o desconocido: {key}")
            for citation in entry["basis"].values():
                location(citation, {"path", "line", "text", "sha256"})
            if root / key[0] not in documents:
                continue
            exact({k: entry[k] for k in ("path", "line", "text", "sha256")})
            if not PENDING.search(visible(entry["text"])):
                raise ValueError(f"Entrada sin detección vigente: {key}")
            for citation in entry["basis"].values():
                exact(citation)
            if not entry["blocking"]:
                if category == "required_gap" or re.search(
                    r"\b(TODO|TBD|FIXME)\b", entry["text"]
                ):
                    raise ValueError(f"Faltante no dispensable: {key}")
                if category == "metadata":
                    content = documents[root / key[0]]
                    metadata, _ = split_frontmatter(content, ())
                    if (
                        not 1 < key[1] < frontmatter_lines(content)
                        or not re.fullmatch(r"tags:\s*\[[^\]\n]+\]\s*", entry["text"])
                        or not isinstance(metadata.get("tags"), list)
                    ):
                        raise ValueError(f"No es una etiqueta de metadatos: {key}")
        return entries, []
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        return {}, [f"Catálogo de entrega inválido: {exc}"]


def assess_finding(name, number, raw_line, catalog):
    entry = catalog.get((name, number))
    if entry is not None and entry["text"] == raw_line:
        return dict(entry)
    return {
        "path": name,
        "line": number,
        "text": raw_line,
        "category": "unclassified",
        "blocking": True,
        "reason": "Detección nueva o sin clasificación exacta; requiere revisión.",
        "basis": {},
    }


# El PDF es un informe para el directorio: no muestra quién iteró, cómo trabajó el
# equipo ni los códigos internos de la cursada.
PROCESS_TEXT = re.compile(
    # El nombre suelto va en la slide del equipo; lo que no va es su autoría de decisiones.
    r"\blazynet\b|\bdecisi[óo]n (?:humana )?de Mart[ií]n\b|\bdecidi[óo] Mart[ií]n\b"
    r"|\bronda\s+\d+\w*|\besta ronda\b"
    r"|\bversi[óo]n (?:anterior|previa|original)\b"
    r"|\b(?:pedido|paquete|programa|propuesta|alcance) anterior\b"
    r"|\breemplazad[oa] como\b|\bpeer review\b|\bdocentes?\b"
    r"|\bdraft\b|\bhuecos\b|\b(?:context|material|private)/"
    r"|\b(?:regla|referencia|versi[óo]n|recomendaci[óo]n)(?: \w+)? del borrador\b"
    r"|\bm\d+ ?u\d+\b",
    re.IGNORECASE,
)
# El anexo de método describe cómo se armó el plan: puede nombrar sus
# herramientas, pero no la historia de iteraciones ni la autoría de decisiones.
METHOD_ANNEX = Path("plan/annexes/08-como-se-armo.md")
METHOD_TEXT = re.compile(
    r"\bfichas?\b|\bcodex\b|`(?:caio|architect|governance|people|finance|board)`",
    re.IGNORECASE,
)


def frontmatter_lines(text):
    # Los errores citan la línea del archivo, no la del cuerpo.
    lines = text.lstrip("\ufeff").splitlines()
    return next(i for i in range(1, len(lines)) if lines[i].strip() == "---") + 1


def process_text(name, body, offset=0):
    # No se renderizan: comentarios, destinos de links, definiciones de referencia
    # y etiquetas de notas al pie.
    body = re.sub(
        r"<!--.*?-->", lambda m: "\n" * m[0].count("\n"), body, flags=re.DOTALL
    )
    found = []
    for line_number, line in enumerate(body.splitlines(), offset + 1):
        if re.match(r"\s{0,3}\[(?!\^)[^\]]+\]:\s*\S", line):
            continue
        line = re.sub(r"\]\([^)]*\)|\[\^[^\]]*\]", "]", line)
        match = PROCESS_TEXT.search(line) or (
            Path(name) != METHOD_ANNEX and METHOD_TEXT.search(line)
        )
        if match:
            found.append(
                f"{name}:{line_number}: texto de proceso en el informe: {match[0]!r}"
            )
    return found


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
    if parsed.scheme == "file":
        raise ValueError(f"Referencia file:// no admitida: {destination}")
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
    if any(part.casefold() == "private" for part in target.relative_to(root).parts):
        raise ValueError(f"Referencia privada no admitida: {destination}")
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
        text = path.read_text(encoding="utf-8")
        metadata, body = split_frontmatter(text, ANNEX_TYPES)
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
    errors.extend(process_text(name, body, frontmatter_lines(text)))
    return errors


def check(root, deck, mode):
    root, deck = root.resolve(), deck.resolve()
    errors, warnings, pending, findings, references = [], [], [], [], set()
    try:
        text = deck.read_text(encoding="utf-8")
        metadata, body = split_frontmatter(text)
    except (OSError, ValueError) as exc:
        return {
            "slides": 0,
            "errors": [str(exc)],
            "warnings": [],
            "pending": [],
            "findings": [],
            "references": [],
        }
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
    errors.extend(process_text(deck.relative_to(root), body, frontmatter_lines(text)))
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
    catalog, catalog_errors = finding_catalog(
        root, {path: documents.get(path, "") for path in delivered | evidence}
    )
    if mode == "delivery":
        errors.extend(catalog_errors)
    else:
        warnings.extend(catalog_errors)
    for origin in sorted(delivered | evidence):
        raw_lines = documents.get(origin, "").splitlines()
        for line_number, line in enumerate(
            visible(documents.get(origin, "")).splitlines(), 1
        ):
            if PENDING.search(line):
                pending.append(
                    f"{origin.relative_to(root)}:{line_number}: {line.strip()}"
                )
                findings.append(
                    assess_finding(
                        str(origin.relative_to(root)),
                        line_number,
                        raw_lines[line_number - 1],
                        catalog,
                    )
                )
    for annex in annex_files(root):
        errors.extend(check_annex(annex, root, mode))
        if mode == "delivery" and str(annex.relative_to(root)) not in references:
            errors.append(
                f"Entrega rechazada: anexo no referenciado desde el deck: {annex.relative_to(root)}"
            )
    if mode == "delivery":
        errors.extend(
            f"Entrega rechazada por pendiente: {item} ({finding['reason']})"
            for item, finding in zip(pending, findings)
            if finding["blocking"]
        )
    if mode == "delivery":
        errors.extend(validate_evidence(root, evidence))
    return {
        "slides": count,
        "errors": errors,
        "warnings": warnings,
        "pending": pending,
        "findings": findings,
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
            f"plan-check ({args.mode}): {result['slides']} slides; {len(result['pending'])} detecciones; {len(result['references'])} referencias locales"
        )
        for finding in result["findings"]:
            disposition = (
                ("BLOQUEO" if args.mode == "delivery" else "PENDIENTE DE ENTREGA")
                if finding["blocking"]
                else "INFORMATIVO"
            )
            print(
                f"{disposition} [{finding['category']}]: {finding['path']}:{finding['line']}: {finding['reason']}"
            )
        for warning in result["warnings"]:
            print(f"ADVERTENCIA: {warning}; clasificaciones no vigentes")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        if not result["errors"]:
            print("OK: estructura válida; evidencia humana y madurez no certificadas")
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
