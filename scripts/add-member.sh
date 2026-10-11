#!/usr/bin/env bash
# Suma a un integrante del equipo como colaborador con permiso de escritura.
# GitHub le manda una invitación que tiene que aceptar (vence a los 7 días).
#
#   scripts/add-member.sh <usuario-github> [número-de-issue]
#
# Si se pasa el issue de "Sumarme al equipo", lo comenta y lo cierra.
# Requiere gh logueado con la cuenta dueña del repo (lazynet).
set -euo pipefail

repo="lazynet/tp-caio-g11-2026"
user="${1:?uso: $0 <usuario-github> [número-de-issue]}"
issue="${2:-}"

gh api --silent -X PUT "repos/$repo/collaborators/$user" -f permission=push
echo "✓ invitación enviada a @$user (permiso: escritura)"

if [[ -n "$issue" ]]; then
  gh issue comment "$issue" --repo "$repo" --body "@$user te mandamos la invitación: aceptala en https://github.com/$repo/invitations y después seguí los pasos de \"Primeros 15 minutos\" del README."
  gh issue close "$issue" --repo "$repo"
fi

echo "Colaboradores e invitaciones pendientes:"
gh api "repos/$repo/collaborators" --jq '.[].login' | sed 's/^/  /'
gh api "repos/$repo/invitations" --jq '.[] | "  " + .invitee.login + " (pendiente)"'
