#!/usr/bin/env bash
# Python evita diferencias de arrays entre Bash 3.2 y Bash 5.
# --strict exige denylist; el default admite una revisión parcial de borradores.
set -euo pipefail
exec python3 - "$@" <<'PY'
import os
import subprocess
import sys


def fail(message):
    print("✗ leak-check: " + message, file=sys.stderr)
    sys.exit(2)


def run_git(args, data=None, allowed=(0,)):
    result = subprocess.run(
        ["git", *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=dict(os.environ, GIT_LITERAL_PATHSPECS="1"),
    )
    if result.returncode not in allowed:
        # Git puede incluir nombres y contenido privado en sus diagnósticos.
        fail("error de Git/scanner; revisión incompleta")
    return result


def main():
    mode, strict, seen_mode = "--staged", False, False
    for arg in sys.argv[1:]:
        if arg in ("--staged", "--all") and not seen_mode:
            mode, seen_mode = arg, True
        elif arg == "--strict" and not strict:
            strict = True
        else:
            fail("uso: scripts/leak-check.sh [--staged|--all] [--strict]")
    os.chdir(run_git(["rev-parse", "--show-toplevel"]).stdout.rstrip(b"\n"))
    listing = (["diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"]
               if mode == "--staged" else ["ls-files", "-z"])
    paths = [os.fsdecode(p) for p in run_git(listing).stdout.split(b"\0") if p]
    denylist = os.environ.get("LEAK_DENYLIST", "")
    if not denylist and os.path.exists(".leak-denylist"):
        with open(".leak-denylist", encoding="utf-8") as handle:
            denylist = handle.read()
    terms = [line for line in denylist.splitlines()
             if line.strip() and not line.startswith("#")]
    if not terms:
        if strict:
            fail("denylist ausente o vacía; modo estricto rechazado")
        print("⚠ leak-check: revisión PARCIAL; sin denylist privada", file=sys.stderr)
    patterns = [
        ("mail corporativo", r"[A-Za-z0-9._%+-]+@flexibility(services)?\.com\.ar"),
        ("clave privada", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        ("confidencialidad", r"^confidential:[[:space:]]*true"),
        ("CUIT", r"(^|[^0-9])(20|23|24|27|30|33|34)-[0-9]{8}-[0-9]([^0-9]|$)"),
    ]
    found = False

    def report(category, number, line=None):
        nonlocal found
        location = "archivo #" + str(number)
        if line is not None:
            location += ", línea " + str(line)
        # Ordinal del listado NUL de Git: no exponemos nombres sensibles.
        print("✗ " + location + ": " + category, file=sys.stderr)
        found = True

    for number, path in enumerate(paths, 1):
        if path.startswith("private/"):
            report("archivo privado versionado", number)
        if path == "scripts/leak-check.sh":
            continue
        scope = ["--cached"] if mode == "--staged" else []
        checks = [(category, ["-E", "-e", pattern], None) for category, pattern in patterns]
        if terms:
            checks.append(("denylist privada", ["-i", "-w", "-F", "-f", "-"],
                           ("\n".join(terms) + "\n").encode()))
        for category, options, data in checks:
            result = run_git(["grep", *scope, "-n", "-z", "-I", *options, "--", path],
                             data, allowed=(0, 1))
            if result.returncode == 0:
                if not result.stdout:
                    fail("respuesta inválida del scanner")
                remaining = result.stdout
                while remaining:
                    _, separator, remaining = remaining.partition(b"\0")
                    line, separator2, remaining = remaining.partition(b"\0")
                    if not separator or not separator2 or not line.isdigit():
                        fail("respuesta inválida del scanner")
                    report(category, number, int(line))
                    _, _, remaining = remaining.partition(b"\n")
    if found:
        print("Datos privados detectados: anonimizá o movelos a private/.", file=sys.stderr)
        return 1
    state = "COMPLETA" if terms else "PARCIAL"
    print("✓ leak-check: revisión " + state + "; sin hallazgos")
    return 0


try:
    sys.exit(main())
except (OSError, ValueError, UnicodeError):
    fail("error de lectura o ejecución; revisión incompleta")
PY
