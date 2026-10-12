#!/usr/bin/env bash
# Verifica que las bases de conocimiento del repo cumplan OKF v0.2 (§11 de la spec):
# cada concepto tiene frontmatter YAML con un `type` no vacío, y los index.md no
# llevan frontmatter salvo `okf_version` en la raíz del bundle.
#
#   scripts/okf-check.sh             revisa todos los bundles
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

bundles=(context material defense/evidence)
found=0

fail() {
  echo "✗ $1: $2" >&2
  found=1
}

# Imprime el frontmatter (sin los ---) o nada si el archivo no arranca con ---.
frontmatter() {
  awk 'NR == 1 { if ($0 != "---") exit; next } $0 == "---" { exit } { print }' "$1"
}

# Un frontmatter que el grep acepta puede no parsear (comillas sin escapar) y romper
# a cualquier consumidor. Si hay PyYAML se valida; CI lo exige con OKF_STRICT=1.
parse_yaml='import sys, yaml
try:
    yaml.safe_load(sys.stdin)
except yaml.YAMLError as e:
    sys.exit(str(e).splitlines()[0])'
yaml_ok=""
if python3 -c 'import yaml' 2>/dev/null; then
  yaml_ok=1
elif [[ "${OKF_STRICT:-}" == 1 ]]; then
  echo "✗ OKF_STRICT=1 necesita python3 con PyYAML" >&2
  exit 1
else
  echo "ⓘ sin PyYAML: no se valida la sintaxis YAML (pip install pyyaml)" >&2
fi

for bundle in "${bundles[@]}"; do
  [[ -d "$bundle" ]] || continue
  while IFS= read -r file; do
    name="$(basename "$file")"
    fm="$(frontmatter "$file")"
    case "$name" in
      log.md) ;;
      index.md)
        if [[ -n "$fm" ]]; then
          if [[ "$file" != "$bundle/index.md" ]]; then
            fail "$file" "un index.md que no está en la raíz del bundle no lleva frontmatter"
          elif grep -qv '^okf_version:' <<<"$fm"; then
            fail "$file" "el index.md raíz solo admite okf_version en el frontmatter"
          fi
        fi
        ;;
      *)
        if [[ "$(head -n1 "$file")" != "---" ]]; then
          fail "$file" "falta el frontmatter YAML"
        elif ! grep -qE '^type:[[:space:]]*[^[:space:]]' <<<"$fm"; then
          fail "$file" "falta type en el frontmatter"
        elif [[ -n "$yaml_ok" ]] && ! err="$(python3 -c "$parse_yaml" <<<"$fm" 2>&1)"; then
          fail "$file" "el frontmatter no es YAML válido: $err"
        fi
        ;;
    esac
  done < <(find "$bundle" -name '*.md' -type f | sort)
done

if [[ $found -eq 1 ]]; then
  echo "Ver la sección \"Bases de conocimiento (OKF)\" en AGENTS.md." >&2
  exit 1
fi
echo "✓ okf-check: bundles conformes"
