#!/usr/bin/env bash
# Renderiza plan/slides.md con cada renderer disponible para comparar alternativas,
# y arma el PDF de entrega (deck + anexos, menos de 10 MB): con --delivery es
# out/Grupo11-AcmeLabs-PlanMaestroCAIO.pdf, el que se entrega; sin él, el -borrador.pdf.
# La salida va a out/ (fuera de git): los decks son artefactos generados, nunca se editan a mano.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/plan/slides.md"
out="$root/out"

renderer="${1:-all}"
mode=draft
if [[ $# -gt 2 || ( $# -eq 2 && ( "$renderer" != entrega || "$2" != --delivery ) ) ]]; then
  echo "Uso: $0 [all|entrega|marp|pandoc|html] [--delivery solo con entrega]" >&2
  exit 2
fi
if [[ $# -eq 2 ]]; then mode=delivery; fi
case "$renderer" in
  all|entrega|marp|pandoc|html) ;;
  *) echo "Renderer inválido: $renderer. Usá all, entrega, marp, pandoc o html." >&2; exit 2 ;;
esac
# CAIO_PYTHON elige el intérprete: en Windows suele ser python, no python3.
"${CAIO_PYTHON:-python3}" "$root/scripts/plan-check.py" --mode "$mode"
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
  # El borrador lleva otro nombre para que un build sin --delivery no pise el final.
  pdf_name=Grupo11-AcmeLabs-PlanMaestroCAIO
  [[ "$mode" == delivery ]] || pdf_name=$pdf_name-borrador
  "${CAIO_PYTHON:-python3}" "$root/scripts/build-delivery.py" --output "$out/$pdf_name.pdf"
fi

if [[ "$renderer" == all || "$renderer" == pandoc ]]; then
  # El pptx de pandoc deja el texto editable; el de Marp exporta las slides como imagen.
  pandoc "$src" -o "$out/deck-pandoc.pptx"
fi

ls -1 "$out"
