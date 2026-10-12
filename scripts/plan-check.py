"""Chequeo estructural del deck; no certifica madurez ni evidencia de negocio."""

import argparse
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


def split_frontmatter(text):
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Falta frontmatter del deck")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("Frontmatter sin cierre")
    metadata = {}
    for line in lines[1:end]:
        match = re.fullmatch(r"([\w-]+):\s*(.*?)\s*", line)
        if match:
            metadata[match[1]] = match[2].strip("\"'")
    return metadata, "\n".join(lines[end + 1 :])


def visible(text):
    # Los ejemplos de código no son slides ni referencias navegables.
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
    return re.sub(r"<!--.*?-->", "", "\n".join(result), flags=re.DOTALL)


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


def links(text):
    text = visible(text)
    definitions = dict(
        re.findall(r"^\s{0,3}\[([^\]^]+)\]:\s*<?([^\s>]+)>?", text, re.MULTILINE)
    )
    for destination in re.findall(
        r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text
    ):
        yield destination.strip("<>")
    for label, reference in re.findall(r"!?\[([^\]]+)\]\[([^\]]*)\]", text):
        key = reference or label
        yield definitions.get(key, f"__undefined_reference__/{key}")
    for destination in definitions.values():
        yield destination


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
    if metadata.get("marp") != "true":
        errors.append("El deck debe declarar marp: true")
    if metadata.get("status") not in ("draft", "ready"):
        errors.append(
            "El status del deck debe ser draft o ready (ready no certifica evidencia)"
        )
    if mode == "delivery" and metadata.get("status") == "draft":
        errors.append("Entrega rechazada: deck declarado draft")
    slides = re.split(r"^\s{0,3}(?:---|\*\*\*)\s*$", visible(body), flags=re.MULTILINE)
    count = len(slides)
    if count > 10:
        errors.append(
            f"Máximo 10 slides incluyendo portada y equipo; encontradas {count}"
        )
    if any(not slide.strip() for slide in slides):
        errors.append("Hay slides vacías")
    queue, seen = [(deck, text)], set()
    while queue:
        origin, content = queue.pop(0)
        if origin in seen:
            continue
        seen.add(origin)
        for line_number, line in enumerate(content.splitlines(), 1):
            if re.search(
                r"\b(pendiente\w*|TODO|TBD|FIXME|por definir|falta evidencia|sin evidencia|esqueleto)\b",
                line,
                re.IGNORECASE,
            ):
                pending.append(
                    f"{origin.relative_to(root)}:{line_number}: {line.strip()}"
                )
        for destination in links(content):
            try:
                target = resolve_link(origin, destination, root)
                if target is not None:
                    references.add(str(target.relative_to(root)))
                    if target.suffix.lower() == ".md" and target not in seen:
                        queue.append((target, target.read_text(encoding="utf-8")))
            except (OSError, ValueError) as exc:
                errors.append(f"{origin.relative_to(root)}: {exc}")
    if mode == "delivery" and pending:
        errors.extend(f"Entrega rechazada por pendiente: {item}" for item in pending)
    return {
        "slides": count,
        "errors": errors,
        "pending": pending,
        "references": sorted(references),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
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
