"""Renomeia referências a `wiki/` para `mnrn/` nos arquivos de config/scripts
(após a pasta de conteúdo ter sido renomeada). Idempotente."""
from pathlib import Path

TARGETS = ["README.md", "AGENTS.md", ".gitignore", "scripts/auditar_wiki.py"]
REPLS = [
    ("-d wiki", "-d mnrn"),
    ("wiki/", "mnrn/"),
    ('Path("wiki")', 'Path("mnrn")'),
]

for f in TARGETS:
    p = Path(f)
    if not p.exists():
        print("skip (nao existe):", f)
        continue
    t = p.read_text(encoding="utf-8")
    for a, b in REPLS:
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8")
    print("ok:", f)
