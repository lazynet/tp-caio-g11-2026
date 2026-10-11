#!/usr/bin/env bash
# Renderiza plan/slides.md con cada renderer disponible para comparar alternativas.
# La salida va a out/ (fuera de git): los decks son artefactos generados, nunca se editan a mano.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/plan/slides.md"
out="$root/out"
mkdir -p "$out"

renderer="${1:-all}"

# Versión de Marp fija para que todo el equipo genere el mismo deck.
marp() { npx -y @marp-team/marp-cli@4.1.2 --allow-local-files "$@"; }

if [[ "$renderer" == all || "$renderer" == marp ]]; then
  marp "$src" -o "$out/deck-marp.html"
  marp "$src" --pdf -o "$out/deck-marp.pdf"
  marp "$src" --pptx -o "$out/deck-marp.pptx"
fi

if [[ "$renderer" == all || "$renderer" == pandoc ]]; then
  # El pptx de pandoc deja el texto editable; el de Marp exporta las slides como imagen.
  pandoc "$src" -o "$out/deck-pandoc.pptx"
fi

ls -1 "$out"
