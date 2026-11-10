"""Extrai texto de todos os arquivos de raw/ para dados/extraidos/.

- PDFs com texto embutido -> extracao direta (pymupdf)
- PDFs escaneados / imagens -> OCR tesseract (lang=por), pagina a pagina quando a
  pagina nao tem texto vetorial
- .docx -> texto do word/document.xml
- .xlsx -> um .csv por aba
- .txt  -> copiado
- .jpeg -> OCR
- .dwg / .md vazio -> nao convertido (registrado em nao-convertidos.md)

Gera dados/extraidos/manifesto.json mapeando destino -> origem.
"""
import io
import json
import re
import subprocess
import sys
import time
import zipfile
from pathlib import Path

import pymupdf
import pandas as pd

RAW = Path("raw")
OUT = Path("dados/extraidos")
LANG = "por"
SCAN_THRESHOLD = 30  # chars/pagina abaixo disso => OCR na pagina
TESSERACT = "tesseract"

T0 = time.time()
manifesto = []
nao_convertidos = []
erros = []
stats = {"pdf_texto": 0, "pdf_ocr": 0, "pdf_misto": 0,
         "docx": 0, "xlsx": 0, "txt": 0, "jpeg": 0, "ignorado": 0,
         "paginas_ocr": 0, "total_chars": 0, "total_bytes": 0}


def safe_component(s: str) -> str:
    s = re.sub(r'[<>:"|?*]', "_", s)
    s = s.rstrip(". ")
    return s or "_"


def fix_cp850(name: str) -> str:
    """Lote 34 foi zipado em CP850; zipfile decodifica como CP437. Reverte."""
    try:
        return name.encode("cp437").decode("cp850", errors="replace")
    except UnicodeEncodeError:
        return name


def ocr_bytes(img: bytes) -> str:
    p = subprocess.run(
        [TESSERACT, "stdin", "stdout", "-l", LANG, "--psm", "3"],
        input=img, capture_output=True, timeout=600,
    )
    return p.stdout.decode("utf-8", errors="replace")


def render_page(page) -> bytes:
    pix = page.get_pixmap(dpi=300, alpha=False)
    return pix.tobytes("png")


def extract_pdf(data: bytes):
    """Retorna (texto, n_paginas, n_paginas_ocr)."""
    doc = pymupdf.open(stream=data, filetype="pdf")
    parts = []
    n_ocr = 0
    for page in doc:
        txt = page.get_text()
        if len(txt.strip()) < SCAN_THRESHOLD:
            try:
                txt = ocr_bytes(render_page(page))
                n_ocr += 1
            except Exception as e:
                erros.append(f"OCR {page.number + 1}: {e}")
        parts.append(txt)
    n = doc.page_count
    doc.close()
    return "\n\n".join(parts), n, n_ocr


def extract_docx(data: bytes) -> str:
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    import html
    return html.unescape(xml)


def write_text(dest: Path, text: str, origem: str, tipo: str, metodo: str,
               paginas: int = 0):
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8", errors="replace")
    dest.write_bytes(data)
    manifesto.append({
        "origem": origem, "destino": str(dest.relative_to(OUT)),
        "tipo": tipo, "metodo": metodo, "paginas": paginas,
        "chars": len(text), "bytes": len(data),
    })
    stats["total_chars"] += len(text)
    stats["total_bytes"] += len(data)


def process_pdf(data: bytes, origem: str, dest: Path):
    try:
        text, n, n_ocr = extract_pdf(data)
    except Exception as e:
        erros.append(f"{origem}: {e}")
        return
    if n_ocr == 0:
        stats["pdf_texto"] += 1
        metodo = "texto_embutido"
    elif n_ocr == n:
        stats["pdf_ocr"] += 1
        metodo = "ocr"
    else:
        stats["pdf_misto"] += 1
        metodo = "misto"
    stats["paginas_ocr"] += n_ocr
    write_text(dest, text, origem, "pdf", metodo, paginas=n)


def process_zip(zpath: Path, fix: bool):
    with zipfile.ZipFile(zpath) as z:
        for e in z.infolist():
            name = e.filename
            if fix:
                name = fix_cp850(name)
            if name.endswith("/") or e.file_size == 0:
                stats["ignorado"] += 1
                continue
            comps = [safe_component(c) for c in name.split("/")]
            rel = Path(*comps)
            lower = name.lower()
            origem = f"{zpath.name}::{name}"
            try:
                if lower.endswith(".pdf"):
                    dest = rel.with_suffix(".txt")
                    process_pdf(z.read(e), origem, OUT / dest)
                elif lower.endswith(".docx"):
                    stats["docx"] += 1
                    text = extract_docx(z.read(e))
                    write_text(OUT / rel.with_suffix(".txt"), text, origem,
                               "docx", "docx_xml")
                elif lower.endswith(".xlsx"):
                    stats["xlsx"] += 1
                    process_xlsx(z.read(e), origem, OUT / rel)
                elif lower.endswith(".jpeg") or lower.endswith(".jpg"):
                    stats["jpeg"] += 1
                    text = ocr_bytes(z.read(e))
                    write_text(OUT / rel.with_suffix(".txt"), text, origem,
                               "jpeg", "ocr")
                elif lower.endswith(".txt"):
                    stats["txt"] += 1
                    write_text(OUT / rel, z.read(e).decode("utf-8", errors="replace"),
                               origem, "txt", "copia")
                elif lower.endswith(".dwg"):
                    nao_convertidos.append(f"{zpath.name}::{name} (CAD .dwg)")
                else:
                    nao_convertidos.append(f"{zpath.name}::{name} ({e.file_size}b)")
            except Exception as ex:
                erros.append(f"{origem}: {ex}")


def process_xlsx(data: bytes, origem: str, dest_base: Path):
    import io as _io
    xls = pd.ExcelFile(_io.BytesIO(data))
    stem = dest_base.with_suffix("")
    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        buf = _io.StringIO()
        df.to_csv(buf, index=False)
        dest = Path(f"{stem}__{safe_component(sheet)}.csv")
        write_text(dest, buf.getvalue(), origem, "xlsx", "csv")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # 1) PDFs da raiz raw
    for p in sorted(RAW.glob("*.pdf")):
        dest = OUT / "raw" / (p.stem + ".txt")
        process_pdf(p.read_bytes(), str(p), dest)

    # 2) clipping zip (UTF-8 ok)
    process_zip(RAW / "4.2.Clipping-20261110T200638Z-1-001.zip", fix=False)

    # 3) lote 34 (CP850)
    process_zip(RAW / "Lote 34 - Ecovias Raposo-Castelo.zip", fix=True)

    # manifesto
    with open(OUT / "manifesto.json", "w", encoding="utf-8") as f:
        json.dump(manifesto, f, ensure_ascii=False, indent=1)

    # nao-convertidos
    if nao_convertidos:
        lines = ["# Arquivos nao convertidos para texto\n",
                 "Os itens abaixo estao em raw/ mas nao geraram .txt "
                 "(CAD/desenho tecnico ou vazios).\n"]
        lines += [f"- {x}" for x in sorted(nao_convertidos)]
        (OUT / "nao-convertidos.md").write_text("\n".join(lines) + "\n",
                                                encoding="utf-8")

    print("=== RESUMO ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print(f"arquivos no manifesto: {len(manifesto)}")
    print(f"nao-convertidos: {len(nao_convertidos)}")
    print(f"erros: {len(erros)}")
    for e in erros[:20]:
        print("  ERRO:", e)
    print(f"tempo: {time.time() - T0:.1f}s")


if __name__ == "__main__":
    main()
