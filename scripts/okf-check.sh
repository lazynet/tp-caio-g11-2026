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
