#!/usr/bin/env bash
# Python evita diferencias de arrays entre Bash 3.2 y Bash 5.
# --strict exige denylist; el default admite una revisión parcial de borradores.
# CAIO_PYTHON elige el intérprete: en Windows suele ser python, no python3.
set -euo pipefail
exec "${CAIO_PYTHON:-python3}" - "$@" <<'PY'
import os
import stat
import subprocess
import sys
import tempfile


def fail(message):
    print("✗ leak-check: " + message, file=sys.stderr)
    sys.exit(2)


def run_git(args, data=None, allowed=(0,), cwd=None):
    result = subprocess.run(
        ["git", *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd,
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
        ("clave privada", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        ("confidencialidad", r"^confidential:[[:space:]]*true"),
        ("CUIT", r"(^|[^0-9])(20|23|24|27|30|33|34)-[0-9]{8}-[0-9]([^0-9]|$)"),
    ]
    found = False
    omitted = False

    def report(category, number, line=None):
        nonlocal found
        location = "archivo #" + str(number)
        if line is not None:
            location += ", línea " + str(line)
        # Ordinal del listado NUL de Git: no exponemos nombres sensibles.
        print("✗ " + location + ": " + category, file=sys.stderr)
        found = True

    def omission(category, number):
        nonlocal omitted
        print("⚠ archivo #" + str(number) + ": omisión; " + category, file=sys.stderr)
        omitted = True

    def payload(path):
        if mode == "--staged":
            entry = run_git(["ls-files", "--stage", "-z", "--", path]).stdout
            metadata, separator, _ = entry.partition(b"\t")
            fields = metadata.split()
            if not separator or len(fields) != 3 or fields[2] != b"0":
                fail("índice ambiguo; revisión incompleta")
            if fields[0] not in (b"100644", b"100755", b"120000"):
                return None, False
            return run_git(["cat-file", "blob", fields[1].decode("ascii")]).stdout, fields[0] == b"120000"
        # No abrir archivos a través de directorios reemplazados por enlaces.
        parent = os.path.dirname(path)
        while parent:
            if os.path.islink(parent):
                return None, False
            parent = os.path.dirname(parent)
        info = os.lstat(path)
        if stat.S_ISLNK(info.st_mode):
            return os.fsencode(os.readlink(path)), True
        if not stat.S_ISREG(info.st_mode):
            return None, False
        with open(path, "rb") as handle:
            return handle.read(), False

    def scan_checks(scope, path, number, cwd=None):
        checks = [(category, ["-E", "-e", pattern], None) for category, pattern in patterns]
        if terms:
            checks.append(("denylist privada", ["-i", "-w", "-F", "-f", "-"],
                           ("\n".join(terms) + "\n").encode()))
        for category, options, data in checks:
            result = run_git(["grep", *scope, "-n", "-z", "-I", *options, "--", path],
                             data, allowed=(0, 1), cwd=cwd)
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

    for number, path in enumerate(paths, 1):
        if path.startswith("private/"):
            report("archivo privado versionado", number)
        content, symlink = payload(path)
        try:
            if content is None:
                raise ValueError
            content.decode("utf-8")
            if b"\0" in content or content.startswith(b"%PDF-"):
                raise ValueError
        except (UnicodeError, ValueError):
            omission("formato fuera del alcance textual UTF-8", number)
            continue
        if path == "scripts/leak-check.sh":
            continue
        scope = ["--cached"] if mode == "--staged" else []
        # Git omite symlinks: inspeccionamos su payload, nunca su destino.
        with tempfile.TemporaryDirectory() as directory:
            scan_path = path
            scan_cwd = None
            if symlink:
                scan_path, scan_cwd = "payload", directory
                with open(os.path.join(directory, scan_path), "wb") as handle:
                    handle.write(content)
                scope = ["--no-index"]
            probe = run_git(["grep", *scope, "-l", "-z", "-I", "-e", "", "--", scan_path],
                            allowed=(0, 1), cwd=scan_cwd)
            if content and probe.returncode == 1:
                omission("contenido excluido por Git grep", number)
                continue
            scan_checks(scope, scan_path, number, cwd=scan_cwd)
    if found:
        print("Datos privados detectados: anonimizá o movelos a private/.", file=sys.stderr)
        return 1
    if omitted and strict:
        fail("omisiones de contenido; modo estricto rechazado")
    state = "COMPLETA" if terms and not omitted else "PARCIAL"
    print("✓ leak-check: revisión " + state + "; sin hallazgos")
    return 0

try:
    sys.exit(main())
except (OSError, ValueError, UnicodeError):
    fail("error de lectura o ejecución; revisión incompleta")
PY
