#!/usr/bin/env bash
# Frena datos privados de Flexibility antes de que lleguen al repo público.
#
#   scripts/leak-check.sh            revisa lo que está en staging (lo usa el pre-commit)
#   scripts/leak-check.sh --all      revisa todos los archivos versionados (lo usa CI)
#
# Dos capas:
#   1. Patrones fijos: mails corporativos, claves privadas, CUIT, archivos marcados
#      como confidenciales y cualquier cosa versionada bajo private/.
#   2. Denylist privada (clientes, personas, proyectos internos): se lee de la
#      variable LEAK_DENYLIST (secreto de GitHub en CI) o del archivo .leak-denylist
#      (local, fuera de git). Una entrada por línea, se compara como palabra
#      completa y sin distinguir mayúsculas. La lista nunca se versiona porque
#      ella misma es el dato a proteger.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

mode="${1:---staged}"
case "$mode" in
  --staged) scope=(--cached) ;;
  --all) scope=() ;;
  *) echo "uso: $0 [--staged|--all]" >&2; exit 2 ;;
esac

# Este script contiene los patrones; si se escaneara a sí mismo, fallaría siempre.
exclude=(':!scripts/leak-check.sh')
found=0

report() {
  echo "✗ $1" >&2
  sed 's/^/    /' >&2
  found=1
}

if [[ "$mode" == --staged ]]; then
  tracked_private=$(git diff --cached --name-only --diff-filter=ACMR -- private/ || true)
else
  tracked_private=$(git ls-files -- private/)
fi
if [[ -n "$tracked_private" ]]; then
  report "archivos bajo private/ en git (esa carpeta es solo local)" <<<"$tracked_private"
fi

fixed_patterns=(
  '[A-Za-z0-9._%+-]+@flexibility(services)?\.com\.ar'
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'
  '^confidential:[[:space:]]*true'
  '(^|[^0-9])(20|23|24|27|30|33|34)-[0-9]{8}-[0-9]([^0-9]|$)'
)
for pattern in "${fixed_patterns[@]}"; do
  if hits=$(git grep "${scope[@]}" -n -I -E -e "$pattern" -- . "${exclude[@]}"); then
    report "patrón prohibido: $pattern" <<<"$hits"
  fi
done

denylist="${LEAK_DENYLIST:-}"
if [[ -z "$denylist" && -f .leak-denylist ]]; then
  denylist="$(cat .leak-denylist)"
fi
terms=$(grep -v -e '^[[:space:]]*$' -e '^#' <<<"$denylist" || true)
if [[ -n "$terms" ]]; then
  if hits=$(git grep "${scope[@]}" -n -I -i -w -F -f <(printf '%s\n' "$terms") -- . "${exclude[@]}"); then
    report "términos de la denylist privada" <<<"$hits"
  fi
else
  echo "⚠ sin denylist privada (LEAK_DENYLIST o .leak-denylist): solo se revisaron los patrones fijos" >&2
fi

if [[ $found -ne 0 ]]; then
  echo >&2
  echo "Datos privados de Flexibility detectados: anonimizá (rangos, 'Cliente A') o movelo a private/." >&2
  exit 1
fi
echo "✓ leak-check: sin datos privados"
