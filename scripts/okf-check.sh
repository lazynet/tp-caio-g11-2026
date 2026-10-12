#!/usr/bin/env bash
# PyYAML es obligatorio: no degradar silenciosamente la validación del contrato.
# CAIO_PYTHON elige el intérprete: en Windows suele ser python, no python3.
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
exec "${CAIO_PYTHON:-python3}" "$root/scripts/okf-check.py" --root "$root" "$@"
