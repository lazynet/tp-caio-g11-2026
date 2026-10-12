#!/usr/bin/env bash
# PyYAML es obligatorio: no degradar silenciosamente la validación del contrato.
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
exec python3 "$root/scripts/okf-check.py" --root "$root" "$@"
