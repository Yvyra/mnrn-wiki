"""Força OCR página a página de um PDF (para PDFs cujo texto vetorial está
corrompido/ilegível). Reusa render_page/ocr_bytes de extrair_txt.py."""
import sys
from pathlib import Path

import pymupdf

from extrair_txt import ocr_bytes, render_page


def ocr_pdf(src: str, dst: str):
    doc = pymupdf.open(src)
    parts = []
    for i, page in enumerate(doc):
        txt = ocr_bytes(render_page(page))
        parts.append(f"\n===== PAGINA {i + 1} =====\n{txt}")
        print(f"pag {i + 1}/{doc.page_count}", flush=True)
    doc.close()
    Path(dst).write_text("\n".join(parts), encoding="utf-8")
    print("salvo:", dst)


if __name__ == "__main__":
    ocr_pdf(sys.argv[1], sys.argv[2])
