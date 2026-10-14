#!/usr/bin/env bash
# Renderiza plan/slides.md con cada renderer disponible para comparar alternativas,
# y arma out/entrega.pdf (deck + anexos, menos de 10 MB), que es lo que se entrega.
# La salida va a out/ (fuera de git): los decks son artefactos generados, nunca se editan a mano.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/plan/slides.md"
out="$root/out"

renderer="${1:-all}"
if [[ $# -gt 1 ]]; then
  echo "Uso: $0 [all|entrega|marp|pandoc|html]" >&2
  exit 2
fi
case "$renderer" in
  all|entrega|marp|pandoc|html) ;;
  *) echo "Renderer inválido: $renderer. Usá all, entrega, marp, pandoc o html." >&2; exit 2 ;;
esac
# CAIO_PYTHON elige el intérprete: en Windows suele ser python, no python3.
"${CAIO_PYTHON:-python3}" "$root/scripts/plan-check.py" --mode draft
mkdir -p "$out"

# Versión de Marp fija para que todo el equipo genere el mismo deck. El tema
# vive en plan/theme y el diseño necesita los bloques HTML de slides.md.
marp() {
  # --theme-set acepta varios paths: va al final para no tragarse la entrada.
  npx -y @marp-team/marp-cli@4.1.2 --allow-local-files --html --no-stdin \
    "$@" --theme-set "$root/plan/theme"
}

if [[ "$renderer" == all || "$renderer" == marp || "$renderer" == html ]]; then
  marp "$src" -o "$out/deck-marp.html"
fi
if [[ "$renderer" == all || "$renderer" == marp || "$renderer" == entrega ]]; then
  marp "$src" --pdf -o "$out/deck-marp.pdf"
fi
if [[ "$renderer" == all || "$renderer" == marp ]]; then
  marp "$src" --pptx -o "$out/deck-marp.pptx"
fi
if [[ "$renderer" == all || "$renderer" == entrega ]]; then
  "${CAIO_PYTHON:-python3}" "$root/scripts/build-delivery.py"
fi

if [[ "$renderer" == all || "$renderer" == pandoc ]]; then
  # El pptx de pandoc deja el texto editable; el de Marp exporta las slides como imagen.
  pandoc "$src" -o "$out/deck-pandoc.pptx"
fi

ls -1 "$out"
