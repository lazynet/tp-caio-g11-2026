#!/usr/bin/env bash
# Se corre una vez después de clonar: activa el chequeo de datos privados en cada commit.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git config core.hooksPath .githooks
mkdir -p private
echo "✓ hook pre-commit activo (core.hooksPath=.githooks)"
echo "✓ carpeta private/ lista (no se versiona)"
[[ -f .leak-denylist ]] || echo "ⓘ si tenés la denylist privada, guardala en .leak-denylist"
