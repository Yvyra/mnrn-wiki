"""Audita wikilinks do wiki: reporta links cujo alvo nao tem arquivo .md."""
import re
from pathlib import Path

WIKI = Path("wiki")
files = {p.stem for p in WIKI.rglob("*.md")}

link_re = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
missing = {}
orphans_candidates = {}
inbound = {}

for p in sorted(WIKI.rglob("*.md")):
    text = p.read_text(encoding="utf-8")
    for m in link_re.finditer(text):
        target = m.group(1).strip()
        inbound.setdefault(target, set()).add(p.stem)
        if target not in files:
            missing.setdefault(str(p), set()).add(target)

print("== wikilinks sem alvo (quebrados) ==")
if missing:
    for p, tgts in sorted(missing.items()):
        print(f"  {p}: {sorted(tgts)}")
else:
    print("  nenhum")

print(f"\n== total de arquivos .md: {len(files)} ==")
