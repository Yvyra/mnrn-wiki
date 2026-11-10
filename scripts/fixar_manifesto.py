"""Corrige (sem refazer OCR) o campo 'origem' do manifesto.json e o
nao-convertidos.md, aplicando cp850 aos nomes do Lote 34."""
import json
import zipfile
from pathlib import Path

RAW = Path("raw")
OUT = Path("dados/extraidos")
LOTE = "Lote 34 - Ecovias Raposo-Castelo.zip"


def fix_cp850(name: str) -> str:
    try:
        return name.encode("cp437").decode("cp850", errors="replace")
    except UnicodeEncodeError:
        return name


# 1) corrigir manifesto
p = OUT / "manifesto.json"
d = json.loads(p.read_text(encoding="utf-8"))
for item in d:
    o = item["origem"]
    if o.startswith(LOTE + "::"):
        item["origem"] = LOTE + "::" + fix_cp850(o.split("::", 1)[1])
p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

# 2) regenerar nao-convertidos.md com nomes corrigidos
conv = (".pdf", ".docx", ".xlsx", ".jpeg", ".jpg", ".txt")
nc = []
with zipfile.ZipFile(RAW / LOTE) as z:
    for e in z.infolist():
        name = fix_cp850(e.filename)
        if name.endswith("/") or e.file_size == 0:
            continue
        low = name.lower()
        if low.endswith(".dwg"):
            nc.append(f"{LOTE}::{name} (CAD .dwg)")
        elif not low.endswith(conv):
            nc.append(f"{LOTE}::{name} ({e.file_size}b)")

lines = [
    "# Arquivos nao convertidos para texto",
    "",
    "Os itens abaixo estao em raw/ mas nao geraram .txt "
    "(CAD/desenho tecnico ou vazios).",
    "",
]
lines += [f"- {x}" for x in sorted(nc)]
(OUT / "nao-convertidos.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print("manifesto corrigido:", len(d), "itens")
print("nao-convertidos:", len(nc), "itens")
