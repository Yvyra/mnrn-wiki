"""Injeta o logo SVG do NRN nos placeholders @@LOGO@@ e @@LOGOSYM@@ do
infografico/HTML (autocontido)."""
import re
from pathlib import Path

svg = Path("raw/imagens/NRN-Logo-2024.svg").read_text(encoding="utf-8")
body = re.sub(r"<\?xml[^>]*\?>", "", svg, flags=re.S)
body = re.sub(r"<svg[^>]*>", "", body, count=1, flags=re.S)
body = re.sub(r"</svg>\s*$", "", body, flags=re.S).strip()

html_path = Path("dados/dossie/infografico-desapropriacoes.html")
html = html_path.read_text(encoding="utf-8")
html = html.replace(
    "@@LOGO@@",
    '<svg class="logo" viewBox="0 0 800 800"><use href="#nrn"/></svg>',
)
html = html.replace("@@LOGOSYM@@", body)
html_path.write_text(html, encoding="utf-8")
print("logo injetado:", len(body), "chars de SVG")
