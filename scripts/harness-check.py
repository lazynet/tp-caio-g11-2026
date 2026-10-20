"""Valida los roles compartidos y genera los adaptadores nativos de Codex."""

import argparse
import json
import re
from pathlib import Path

import yaml

ROLES = {"caio", "architect", "governance", "people", "finance", "board"}
ROLE_PATH = r"`((?:plan|defense)/[^`]+(?:\.md|/))`"
# Archivos de dueño único fijado por AGENTS.md y README.md.
SOLE_OWNER = {
    "plan/slides.md": "caio",
    "defense/storyline.md": "caio",
    "defense/objeciones.md": "caio",
}


def expected_adapters(root):
    adapters = {}
    claims = {}
    errors = []
    roles = root / ".claude/agents"
    found = {path.stem for path in roles.glob("*.md")}
    if found != ROLES:
        errors.append(
            f"Roles esperados: {', '.join(sorted(ROLES))}; encontrados: {', '.join(sorted(found))}"
        )
    for path in sorted(roles.glob("*.md")):
        try:
            _, header, body = path.read_text(encoding="utf-8").split("---", 2)
            metadata = yaml.safe_load(header)
            if (
                metadata["name"] != path.stem
                or not isinstance(metadata.get("description"), str)
                or not metadata["description"].strip()
            ):
                raise ValueError("name y description deben identificar el rol")
            if not isinstance(metadata.get("tools"), str):
                raise ValueError("tools debe declarar las herramientas de Claude")
        except (ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: frontmatter inválido: {exc}")
            continue
        for target in re.findall(ROLE_PATH, body):
            found_target = (
                (root / target).is_dir()
                if target.endswith("/")
                else (root / target).is_file()
            )
            if not found_target:
                errors.append(f"{path.relative_to(root)}: ruta inexistente: {target}")
        owned = re.search(
            r"^## Sos dueño de\n(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL
        )
        if owned:
            for target in re.findall(ROLE_PATH, owned[1]):
                claims.setdefault(target, set()).add(path.stem)
        # El TOML transporta instrucciones, no una traducción ficticia de permisos.
        instructions = (
            "Leé AGENTS.md antes de trabajar y respetá sus reglas.\n\n" + body.strip()
        )
        content = "# Generado por scripts/harness-check.py --write. No editar.\n"
        for key, value in (
            ("name", metadata["name"]),
            ("description", metadata["description"]),
            ("developer_instructions", instructions),
        ):
            content += f"{key} = {json.dumps(value, ensure_ascii=False)}\n"
        adapters[root / ".codex/agents" / f"{path.stem}.toml"] = content
    return adapters, claims, errors


def check(root, write=False):
    adapters, claims, errors = expected_adapters(root)
    if errors:
        return errors
    for path, expected in adapters.items():
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            errors.append(
                f"{path.relative_to(root)}: adaptador ausente o desactualizado; corré --write"
            )
    for path in (root / ".codex/agents").glob("*.toml"):
        if path not in adapters:
            errors.append(
                f"{path.relative_to(root)}: adaptador sin rol fuente; revisalo antes de borrarlo"
            )
    for path in sorted((root / "plan/annexes").glob("*.md")):
        if path.name.startswith("_"):
            continue
        try:
            header = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
            owner = header.get("owner")
        except (IndexError, AttributeError, yaml.YAMLError):
            errors.append(f"{path.relative_to(root)}: frontmatter inválido")
            continue
        if owner not in ROLES - {"board"}:
            errors.append(f"{path.relative_to(root)}: owner sin rol editor: {owner}")
        elif owner not in claims.get(path.relative_to(root).as_posix(), set()):
            errors.append(
                f"{path.relative_to(root)}: su dueño {owner} no declara el archivo"
            )
        elif claims[path.relative_to(root).as_posix()] != {owner}:
            errors.append(f"{path.relative_to(root)}: más de un rol reclama el anexo")
    for target, owner in SOLE_OWNER.items():
        if owner not in claims.get(target, set()):
            errors.append(f"{target}: su dueño {owner} no declara el archivo")
        elif claims[target] != {owner}:
            errors.append(f"{target}: más de un rol reclama el archivo")
    if (
        not (root / ".claude/skills").is_dir()
        or (root / ".claude/skills").resolve() != (root / ".agents/skills").resolve()
    ):
        errors.append(
            ".claude/skills: debe enlazar a .agents/skills (en Windows activá core.symlinks)"
        )
    for path in sorted((root / ".agents/skills").glob("*/SKILL.md")):
        try:
            metadata = yaml.safe_load(
                path.read_text(encoding="utf-8").split("---", 2)[1]
            )
            if not isinstance(metadata, dict):
                raise ValueError("frontmatter debe ser un mapa")
            if (
                metadata.get("name") != path.parent.name
                or not isinstance(metadata.get("description"), str)
                or not metadata["description"].strip()
            ):
                raise ValueError("name y description deben identificar el skill")
            extra = set(metadata) - {
                "name",
                "description",
                "license",
                "allowed-tools",
                "metadata",
            }
            if extra:
                raise ValueError(f"claves no portables: {', '.join(sorted(extra))}")
        except (IndexError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="regenerar los adaptadores de Codex"
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = check(root, args.write)
    for error in errors:
        print(f"✗ {error}")
    if not errors:
        print(
            "✓ harness-check: roles, rutas, dueños y adaptadores coherentes; no certifica invocación ni permisos"
        )
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
