"""Reancla scripts/delivery-findings.json al árbol actual.

Cada entrada y cada cita se buscan por su texto exacto; se actualizan línea y sha256.
Las entradas cuyo texto ya no existe se descartan (la detección desapareció) y se listan.
Con --add <json> suma entradas nuevas: [{path, line, category, blocking, reason,
basis: {clave: {path, line, nlines}}}]; texto y sha256 salen del árbol.

Uso: python3 scripts/rebase-findings.py . [--add nuevas.json]
Correlo después de editar cualquier archivo clasificado, antes del gate de entrega:
el sha256 cubre el documento entero y una sola entrada vencida anula todo el catálogo.
"""
import hashlib
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
catalog_path = root / "scripts/delivery-findings.json"
data = json.loads(catalog_path.read_text(encoding="utf-8"))
cache = {}


def doc(name):
    if name not in cache:
        text = (root / name).read_text(encoding="utf-8")
        cache[name] = (
            text,
            text.splitlines(),
            hashlib.sha256(text.encode()).hexdigest(),
        )
    return cache[name]


def anchor(item, hint=None):
    text, lines, sha = doc(item["path"])
    want = item["text"].split("\n")
    hits = [
        i + 1
        for i in range(len(lines) - len(want) + 1)
        if lines[i : i + len(want)] == want
    ]
    if not hits:
        return None
    line = min(hits, key=lambda n: abs(n - (hint or item["line"])))
    return {**item, "line": line, "sha256": sha}


def cite(path, line, nlines=1):
    text, lines, sha = doc(path)
    return {
        "path": path,
        "line": line,
        "text": "\n".join(lines[line - 1 : line - 1 + nlines]),
        "sha256": sha,
    }


kept, dropped = [], []
for entry in data["entries"]:
    new = anchor(entry)
    basis = {}
    ok = new is not None
    for key, c in entry["basis"].items():
        b = anchor(c) if ok else None
        if b is None:
            ok = False
            break
        basis[key] = b
    if ok:
        new["basis"] = basis
        kept.append(new)
    else:
        dropped.append(f"{entry['path']}:{entry['line']} [{entry['category']}]")

if "--add" in sys.argv:
    for add in json.loads(Path(sys.argv[sys.argv.index("--add") + 1]).read_text()):
        c = cite(add["path"], add["line"])
        entry = {
            **c,
            "category": add["category"],
            "blocking": add["blocking"],
            "reason": add["reason"],
            "basis": {
                k: cite(v["path"], v["line"], v.get("nlines", 1))
                for k, v in add.get("basis", {}).items()
            },
        }
        kept = [
            e for e in kept if (e["path"], e["line"]) != (entry["path"], entry["line"])
        ]
        kept.append(entry)

data["entries"] = kept
catalog_path.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"kept={len(kept)} dropped={len(dropped)}")
for d in dropped:
    print("DROPPED", d)
