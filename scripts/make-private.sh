#!/usr/bin/env bash
# Pasa el repo a privado cuando el equipo ya está adentro.
#
#   scripts/make-private.sh          muestra qué cambia y pide confirmación
#   scripts/make-private.sh --yes    lo hace sin preguntar
#
# Los colaboradores conservan el acceso. Lo que cambia en una cuenta GitHub Free:
#   - Los rulesets de main dejan de aplicarse (en privado requieren GitHub Pro).
#   - Secret scanning y push protection dejan de estar disponibles.
#   - Actions pasa a consumir minutos de la cuota gratuita (2000/mes).
#   - Los forks públicos que existan quedan públicos y se separan del repo.
#   - Lo que ya fue público pudo quedar clonado o cacheado: pasar a privado no
#     despublica nada.
set -euo pipefail

repo="lazynet/tp-caio-g11-2026"

sed -n '7,13p' "$0" | sed 's/^# \{0,1\}//'
if [[ "${1:-}" != --yes ]]; then
  read -r -p "Pasar $repo a privado? [s/N] " answer
  [[ "$answer" == s || "$answer" == S ]] || { echo "cancelado"; exit 1; }
fi

gh repo edit "$repo" --visibility private --accept-visibility-change-consequences
gh repo view "$repo" --json visibility --jq '"✓ visibilidad: " + .visibility'
echo "Colaboradores con acceso:"
gh api "repos/$repo/collaborators" --jq '.[].login' | sed 's/^/  /'
