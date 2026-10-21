"""Valida estructura y trazabilidad local; no certifica afirmaciones ni fuentes."""

import argparse
import re
import subprocess
import sys
import tempfile
from collections import Counter
from contextlib import ExitStack
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("✗ okf-check necesita Python 3 con PyYAML (python3 -m pip install pyyaml)")

BUNDLES = {
    "context": {"Hecho", "Supuesto"},
    "material": {
        "Unidad",
        "Framework",
        "Concepto",
        "Caso",
        "Apunte de clase",
        "Programa",
        "Mapa",
        "Hueco",
    },
    "defense/evidence": {"Evidencia"},
}
ID = re.compile(r"^[\w.-]+$", re.UNICODE)
AUTHOR = re.compile(
    r"^(?:human:[A-Za-z0-9][A-Za-z0-9-]*|(?:codex|claude-code|copilot)/\S+)$"
)
HUMAN = re.compile(r"^human:[A-Za-z0-9][A-Za-z0-9-]*$")


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise TypeError("las claves YAML deben ser strings")
        if key in result:
            raise ValueError(f"clave YAML duplicada: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def iso_date(value):
    if isinstance(value, (date, datetime)):
        return True
    if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:T|$)", value):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def markdown(text):
    text = re.sub(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    return re.sub(r"<!--.*?(?:-->|\Z)", "", text, flags=re.S)


def reference_label(label):
    return " ".join(label.split()).casefold()


def anchors(text):
    result, counts = set(), Counter()
    text = markdown(text)
    for heading in re.findall(r"(?m)^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", text):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        result.add(slug if not counts[slug] else f"{slug}-{counts[slug]}")
        counts[slug] += 1
    result.update(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    return result


class Checker:
    def __init__(self, root, delivery=False):
        self.root = Path(root).resolve()
        self.delivery = delivery
        self.errors = []
        self.warnings = []

    def error(self, path, message):
        self.errors.append(f"✗ {path.relative_to(self.root)}: {message}")

    def missing(self, path, body, message):
        # Huecos solo habilita excepciones para la ficha que menciona explícitamente.
        gaps = self.root / "material/huecos.md"
        documented = bool(re.search(r"(?mi)^#{1,6}\s+Cautelas\s*\n\s*\S", body))
        if gaps.is_file():
            if not gaps.resolve().is_relative_to(self.root / "material"):
                raise ValueError("huecos fuera del bundle")
            documented |= path.name in gaps.read_text(encoding="utf-8")
        if not self.delivery and documented:
            self.warnings.append(
                f"ⓘ {path.relative_to(self.root)}: {message} (faltante documentado)"
            )
        else:
            self.error(path, message)

    def bundle(self, path):
        for name in BUNDLES:
            base = (self.root / name).resolve()
            if base.is_relative_to(self.root) and path.is_relative_to(base):
                return name, base
        return None, None

    def select(self, selections):
        paths = set()
        for selection in selections or BUNDLES:
            path = (self.root / selection).resolve()
            name, base = self.bundle(path)
            if not name or not path.exists():
                raise ValueError(f"path inexistente o fuera de bundles: {selection}")
            candidates = sorted(path.rglob("*.md")) if path.is_dir() else [path]
            if not candidates:
                raise ValueError(f"path sin archivos Markdown: {selection}")
            for candidate in candidates:
                resolved = candidate.resolve()
                if (
                    not resolved.is_relative_to(base)
                    or not resolved.is_file()
                    or resolved.suffix != ".md"
                ):
                    raise ValueError(f"path inválido o fuera del bundle: {candidate}")
                paths.add(resolved)
        return sorted(paths)

    def frontmatter(self, path, text):
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            return None, text
        try:
            end = lines.index("---", 1)
        except ValueError:
            self.error(path, "frontmatter sin cierre ---")
            return None, text
        try:
            data = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
            if not isinstance(data, dict):
                raise TypeError("el frontmatter debe ser un mapping")
        except (yaml.YAMLError, ValueError, TypeError) as exc:
            self.error(path, f"YAML inválido: {str(exc).splitlines()[0]}")
            return None, "\n".join(lines[end + 1 :])
        return data, "\n".join(lines[end + 1 :])

    def attribution(self, path, data, key, human=False):
        block = data.get(key)
        if not isinstance(block, dict):
            self.error(path, f"{key} debe ser un mapping con by y at")
            return
        pattern = HUMAN if human else AUTHOR
        if not isinstance(block.get("by"), str) or not pattern.fullmatch(block["by"]):
            self.error(
                path,
                f"{key}.by inválido"
                + ("; exige human:<usuario-github>" if human else ""),
            )
        if not iso_date(block.get("at")):
            self.error(path, f"{key}.at debe ser una fecha ISO")
        if human and not nonempty(block.get("scope")):
            self.error(path, f"{key}.scope debe describir fuente y alcance revisados")

    def sources(self, path, data, body):
        sources = data.get("sources", [])
        if not isinstance(sources, list):
            self.error(path, "sources debe ser una lista")
            return
        ids = set()
        for source in sources:
            if not isinstance(source, dict):
                self.error(path, "cada source debe ser un mapping")
                continue
            sid = source.get("id")
            if not isinstance(sid, str) or not ID.fullmatch(sid):
                self.error(path, "source.id inválido")
                continue
            if sid in ids:
                self.error(path, f"source.id duplicado: {sid}")
            ids.add(sid)
            if "resource" not in source:
                self.missing(path, body, f"source {sid}: falta resource")
            elif not nonempty(source["resource"]):
                self.error(path, f"source {sid}: resource debe ser un string no vacío")
            if "title" in source and not nonempty(source["title"]):
                self.error(path, f"source {sid}: title inválido")
        clean = markdown(body)
        definitions = re.findall(r"(?m)^ {0,3}\[\^([^]]+)\]:\s*(.*)$", clean)
        counts = Counter(sid for sid, _ in definitions)
        for sid, definition in definitions:
            if counts[sid] > 1 or not definition.strip():
                self.error(path, f"definición de nota duplicada o vacía: {sid}")
            if sid not in ids:
                self.error(path, f"nota {sid} sin source.id")
        references = set(re.findall(r"\[\^([^]]+)\](?!:)", clean))
        for sid in references:
            if sid not in ids or sid not in counts:
                self.error(path, f"cita {sid} necesita source.id y definición de nota")
        required = data.get("type") not in ("Mapa", "Hueco", "Supuesto") or bool(
            sources or references or definitions
        )
        if required and not sources:
            self.missing(path, body, "faltan sources para afirmaciones de terceros")
        if required and not references:
            self.missing(path, body, "faltan citas a sources en el contenido")

    def links(self, path, body, base):
        clean = markdown(body)
        definitions = {}
        for label, target in re.findall(
            r"(?m)^ {0,3}\[([^\]^][^]]*)\]:\s*(\S+)", clean
        ):
            definitions.setdefault(reference_label(label), target)
        targets = re.findall(
            r"!?\[[^]\n]+\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", clean
        )
        for label, ref in re.findall(r"\[([^]]+)\]\[([^]]*)\]", clean):
            if label.startswith("^") or ref.startswith("^"):
                continue
            key = reference_label(ref or label)
            if key not in definitions:
                self.error(path, f"referencia Markdown sin definición: {key}")
            else:
                targets.append(definitions[key])
        targets.extend(definitions.values())
        for raw in targets:
            target = unquote(raw.strip("<>"))
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path and not parsed.path.startswith("/"):
                self.error(path, f"link local debe ser absoluto al bundle: {target}")
                continue
            local = (base / parsed.path.lstrip("/")).resolve() if parsed.path else path
            if not local.is_relative_to(base) or not local.is_file():
                self.error(path, f"link local inexistente o fuera del bundle: {target}")
            elif parsed.fragment and parsed.fragment not in anchors(
                local.read_text(encoding="utf-8")
            ):
                self.error(path, f"anchor inexistente: {target}")

    def check(self, path):
        name, base = self.bundle(path)
        text = path.read_text(encoding="utf-8")
        data, body = self.frontmatter(path, text)
        self.links(path, body, base)
        if path.name == "index.md":
            if path == base / "index.md":
                if data != {"okf_version": "0.2"}:
                    self.error(path, 'index raíz exige solo okf_version: "0.2"')
            elif text.startswith("---\n"):
                self.error(path, "index anidado no admite frontmatter")
            return
        if path.name == "log.md" and data is None and not self.delivery:
            return
        if data is None:
            self.error(path, "falta frontmatter válido")
            return
        if not isinstance(data.get("type"), str) or data["type"] not in BUNDLES[name]:
            self.error(path, "type desconocido o inválido para el bundle")
        for key in ("title", "description"):
            if key not in data:
                self.missing(path, body, f"falta {key}")
            elif not nonempty(data[key]):
                self.error(path, f"{key} debe ser un string no vacío")
        if "generated" not in data:
            self.missing(path, body, "falta generated")
        else:
            self.attribution(path, data, "generated")
        status = data.get("status", "draft")
        if status not in ("draft", "accepted", "verified"):
            self.error(path, "status debe ser draft, accepted o verified")
        if status == "accepted" or "accepted" in data:
            self.attribution(path, data, "accepted", human=True)
        if status == "verified" or "verified" in data:
            self.attribution(path, data, "verified", human=True)
        if self.delivery and status != "verified":
            self.error(path, "entrega exige status: verified con revisión humana")
        self.sources(path, data, body)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--staged",
        action="store_true",
        help="validar solo el snapshot completo del índice, en borrador; paths relativos al repo",
    )
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--delivery",
        action="store_true",
        help="exigir revisión humana de las fichas seleccionadas",
    )
    parser.add_argument(
        "--path",
        action="append",
        default=[],
        help="archivo o directorio del repo; repetible",
    )
    parser.add_argument(
        "paths", nargs="*", help="selección adicional de paths del repo"
    )
    args = parser.parse_args(argv)
    if args.staged and args.delivery:
        parser.error("--staged solo admite modo borrador")
    try:
        with ExitStack() as stack:
            root = args.root.resolve()
            selections = args.path + args.paths
            if args.staged:
                result = subprocess.run(
                    ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                    capture_output=True,
                    check=True,
                    text=True,
                )
                if Path(result.stdout.strip()).resolve() != root:
                    raise ValueError("--root debe ser la raíz del repo Git")
                if any(Path(selection).is_absolute() for selection in selections):
                    raise ValueError("--staged exige paths relativos al repo")
                temporary = root / "tmp"
                if temporary.is_symlink():
                    raise ValueError("tmp no puede ser un symlink")
                temporary.mkdir(exist_ok=True)
                snapshot = stack.enter_context(
                    tempfile.TemporaryDirectory(prefix="okf-index-", dir=temporary)
                )
                subprocess.run(
                    [
                        "git",
                        "-C",
                        str(root),
                        "checkout-index",
                        "--all",
                        "--ignore-skip-worktree-bits",
                        f"--prefix={snapshot}/",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )
                root = Path(snapshot)
            checker = Checker(root, args.delivery)
            paths = checker.select(selections)
            for path in paths:
                checker.check(path)
    except subprocess.CalledProcessError:
        print(
            "✗ okf-check: no se pudo leer el índice o crear su snapshot",
            file=sys.stderr,
        )
        return 1
    except (ValueError, OSError, UnicodeError) as exc:
        message = (
            "falló la selección, lectura o snapshot del índice"
            if args.staged
            else str(exc)
        )
        print(f"✗ okf-check: {message}", file=sys.stderr)
        return 1
    for message in checker.warnings + checker.errors:
        print(message, file=sys.stderr)
    if checker.errors:
        print(f"✗ okf-check: {len(checker.errors)} errores", file=sys.stderr)
        return 1
    if args.delivery:
        print(
            f"✓ okf-check: {len(paths)} archivos conformes en entrega; solo estructura y declaración humana"
        )
    else:
        print(
            f"✓ okf-check: {len(paths)} archivos conformes en borrador; no implica aptitud para slides/entrega"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
