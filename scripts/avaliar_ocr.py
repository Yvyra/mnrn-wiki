"""Avalia custo de conversao PDF->TXT: conta paginas e detecta se cada PDF
tem texto embutido (extracao direta) ou e' imagem escaneada (precisa OCR)."""
import io
import sys
import zipfile
from pathlib import Path

import pymupdf

RAW = Path("raw")
SCAN_THRESHOLD = 30  # chars/pagina abaixo disso => tratar como escaneado


def classify(data: bytes):
    doc = pymupdf.open(stream=data, filetype="pdf")
    n = doc.page_count
    chars = 0
    for page in doc:
        chars += len(page.get_text())
    doc.close()
    return n, chars


def scan_pdf_paths(paths, sample=None):
    rows = []
    for p in paths:
        try:
            n, c = classify(p.read_bytes())
        except Exception as e:
            rows.append((p.name, 0, 0, "ERRO", str(e)[:60]))
            continue
        scanned = "SCAN" if (n and c / n < SCAN_THRESHOLD) else "TXT"
        rows.append((p.name, n, c, scanned, ""))
        if sample and len(rows) >= sample:
            break
    return rows


def scan_zip_entries(zpath, max_scan=6, prefer=None):
    rows = []
    with zipfile.ZipFile(zpath) as z:
        pdfs = [e for e in z.infolist() if e.filename.lower().endswith(".pdf") and e.file_size > 0]
        chosen = pdfs
        if prefer:
            chosen = [e for e in pdfs if any(k in e.filename for k in prefer)]
        if max_scan and len(chosen) > max_scan:
            # pega os maiores + menores para amostrar diversidade
            by_size = sorted(pdfs, key=lambda e: e.file_size)
            chosen = by_size[: max_scan // 2] + by_size[-max_scan // 2 :]
        for e in chosen:
            try:
                n, c = classify(z.read(e))
            except Exception as ex:
                rows.append((e.filename, 0, 0, "ERRO", str(ex)[:60]))
                continue
            scanned = "SCAN" if (n and c / n < SCAN_THRESHOLD) else "TXT"
            rows.append((e.filename, n, c, scanned, ""))
    return rows


def emit(title, rows):
    print(f"\n=== {title} ===")
    tot_pages = sum(r[1] for r in rows if r[3] != "ERRO")
    tot_chars = sum(r[2] for r in rows if r[3] != "ERRO")
    n_scan = sum(1 for r in rows if r[3] == "SCAN")
    n_txt = sum(1 for r in rows if r[3] == "TXT")
    print(f"arquivos analisados: {len(rows)} | paginas: {tot_pages} | chars: {tot_chars} | SCAN: {n_scan} | TXT: {n_txt}")
    for r in rows:
        flag = r[3]
        note = f" [{r[4]}]" if r[4] else ""
        print(f"  {flag:5} {r[1]:>6}p {r[2]:>12,}c  {r[0]}{note}")


if __name__ == "__main__":
    # 1) raiz raw
    root_pdfs = sorted(RAW.glob("*.pdf"))
    emit("RAW raiz (todos os PDFs)", scan_pdf_paths(root_pdfs))

    # 2) clipping zip (todo, e' pequeno)
    clip = RAW / "4.2.Clipping-20261110T200638Z-1-001.zip"
    emit("ZIP Clipping (todos os PDFs)", scan_zip_entries(clip, max_scan=0))

    # 3) lote 34 (amostra diversa)
    lote = RAW / "Lote 34 - Ecovias Raposo-Castelo.zip"
    emit("ZIP Lote 34 (AMOSTRA)", scan_zip_entries(lote, max_scan=8))
