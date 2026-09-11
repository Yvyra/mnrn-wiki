"""Extrai o texto de um PDF para ingestão na wiki.

Ferramenta do toolchain mnrn-wiki. Automatiza a primeira etapa do fluxo de
ingestão descrito em `contexto_mnrn_wiki.md`: lê a fonte inteira, extrai o
texto página a página com PyMuPDF e sinaliza páginas digitalizadas (só
imagem). A saída é um Markdown intermediário para o agente ler antes de
executar os passos seguintes (mapeamento de citações, AIL, criação de página,
atualização dos índices), que continuam sendo trabalho de análise, não de script.

Nunca modifica nada em `raw/`; escreve apenas em `scripts/output/` (git-ignored).

Uso:
    uv run python scripts/ingest_pdf.py <pdf> [--out-dir DIR] [--max-pages N] [--ocr]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pymupdf  # `import fitz` está deprecado no PyMuPDF 1.28+

# Páginas com menos caracteres que isso são tratadas como somente-imagem.
SCAN_THRESHOLD_CHARS = 40


def extract_text(pdf_path: Path) -> dict[int, str]:
    """Retorna {número_da_página: texto} para todas as páginas do PDF."""
    doc = pymupdf.open(pdf_path)
    try:
        return {i + 1: page.get_text() for i, page in enumerate(doc)}
    finally:
        doc.close()


def page_is_scanned(text: str) -> bool:
    return len(text.strip()) < SCAN_THRESHOLD_CHARS


def ocr_pages(
    pdf_path: Path, page_texts: dict[int, str], scanned: list[int]
) -> dict[int, str]:
    """Aplica OCR (pytesseract) nas páginas digitalizadas, se disponível."""
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        print(
            "OCR solicitado, mas pytesseract/pillow não está instalado.\n"
            "Rode:  uv add pytesseract pillow\n"
            "e instale o binário do Tesseract no sistema.",
            file=sys.stderr,
        )
        return page_texts

    doc = pymupdf.open(pdf_path)
    try:
        for num in scanned:
            pix = doc[num - 1].get_pixmap(dpi=200)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            page_texts[num] = pytesseract.image_to_string(img, lang="por")
    finally:
        doc.close()
    return page_texts


def render_markdown(page_texts: dict[int, str], source_name: str) -> str:
    lines = [f"# Texto extraído — {source_name}", ""]
    for num in sorted(page_texts):
        text = page_texts[num]
        heading = f"## Página {num}"
        if page_is_scanned(text):
            heading += " (digitalizada — sem texto)"
        lines += [heading, "", text.strip(), ""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extrai texto de um PDF para ingestão na wiki mnrn-wiki."
    )
    parser.add_argument("pdf", type=Path, help="Caminho do PDF (geralmente em raw/).")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("scripts/output"),
        help="Diretório de saída (default: scripts/output).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Limita a extração às N primeiras páginas.",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Aplica OCR (pytesseract) nas páginas sem texto.",
    )
    args = parser.parse_args(argv)

    pdf = args.pdf
    if not pdf.is_file():
        print(f"Erro: arquivo não encontrado: {pdf}", file=sys.stderr)
        return 2

    page_texts = extract_text(pdf)
    scanned = [n for n, t in page_texts.items() if page_is_scanned(t)]
    total = len(page_texts)

    print(f"Fonte: {pdf}")
    print(f"Páginas: {total}")
    print(f"Páginas com texto: {total - len(scanned)}")
    print(f"Páginas digitalizadas (sem texto): {len(scanned)}")
    if scanned:
        print(f"  Páginas: {scanned}")

    if args.ocr and scanned:
        before = len(scanned)
        page_texts = ocr_pages(pdf, page_texts, scanned)
        after = len([t for t in page_texts.values() if page_is_scanned(t)])
        print(f"OCR: {before - after} página(s) preenchida(s).")

    if args.max_pages:
        page_texts = {n: t for n, t in page_texts.items() if n <= args.max_pages}

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{pdf.stem}.md"
    out_path.write_text(render_markdown(page_texts, pdf.name), encoding="utf-8")
    print(f"Saída: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
