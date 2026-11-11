"""Adiciona a marca d'água (logo NRN) ao custom.scss do Quartz, via data URI."""
import base64
from pathlib import Path

svg = Path("raw/imagens/NRN-Logo-2024.svg").read_bytes()
b64 = base64.b64encode(svg).decode("ascii")

css_path = Path("quartz/styles/custom.scss")
css = css_path.read_text(encoding="utf-8")

marker = "// Marca d'água"
if marker in css:
    css = css.split(marker)[0].rstrip() + "\n\n"

css += marker + " — logo do Movimento Nova Raposo, NÃO!\n"
css += "// ajuste a opacidade (0.06) e o tamanho (42vmin) conforme necessário\n"
css += "body::after {\n"
css += '  content: "";\n'
css += "  position: fixed;\n"
css += "  inset: 0;\n"
css += '  background-image: url("data:image/svg+xml;base64,' + b64 + '");\n'
css += "  background-repeat: no-repeat;\n"
css += "  background-position: center;\n"
css += "  background-size: 42vmin;\n"
css += "  opacity: 0.06;\n"
css += "  pointer-events: none;\n"
css += "  z-index: 2147483647;\n"
css += "}\n"

css_path.write_text(css, encoding="utf-8")
print("marca d'água adicionada; base64:", len(b64), "chars")
