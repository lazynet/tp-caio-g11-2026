#!/usr/bin/env bash
# Render plan/slides.md with every available renderer so alternatives can be compared.
# Output goes to out/ (gitignored): decks are build artifacts, never edited by hand.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/plan/slides.md"
out="$root/out"
mkdir -p "$out"

renderer="${1:-all}"

# Marp version pinned so every teammate renders the same deck.
marp() { npx -y @marp-team/marp-cli@4.1.2 --allow-local-files "$@"; }

if [[ "$renderer" == all || "$renderer" == marp ]]; then
  marp "$src" -o "$out/deck-marp.html"
  marp "$src" --pdf -o "$out/deck-marp.pdf"
  marp "$src" --pptx -o "$out/deck-marp.pptx"
fi

if [[ "$renderer" == all || "$renderer" == pandoc ]]; then
  # Pandoc pptx keeps text editable; Marp pptx exports slides as images.
  pandoc "$src" -o "$out/deck-pandoc.pptx"
fi

ls -1 "$out"
