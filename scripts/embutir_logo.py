"""Substitui o logo placeholder no HTML pelos paths do SVG original do NRN."""
import re
from pathlib import Path

svg_path = Path("raw/imagens/NRN-Logo-2024.svg")
html_path = Path("dados/dossie/nova-raposo-efeitos-sp.html")

svg = svg_path.read_text(encoding="utf-8")
html = html_path.read_text(encoding="utf-8")

# limpa o SVG original: remove declaração XML, tag <svg> externa e fechamento
body = re.sub(r"<\?xml[^>]*\?>", "", svg, flags=re.S)
body = re.sub(r"<svg[^>]*>", "", body, count=1, flags=re.S)
body = re.sub(r"</svg>\s*$", "", body, flags=re.S).strip()

new_block = (
    '<svg width="0" height="0" style="position:absolute">\n'
    '  <symbol id="nrn" viewBox="0 0 800 800">\n'
    f"{body}\n"
    '  </symbol>\n'
    "</svg>"
)

marker_in = '<svg width="0" height="0" style="position:absolute">'
marker_out = '<div class="deck">'
i = html.find(marker_in)
j = html.find(marker_out)
if i < 0 or j < 0 or j <= i:
    raise SystemExit("marcadores do bloco do logo não encontrados")

html2 = html[:i] + new_block + "\n\n" + html[j:]
html_path.write_text(html2, encoding="utf-8")
print(f"logo embutido: {len(body)} chars de SVG -> {html_path}")
