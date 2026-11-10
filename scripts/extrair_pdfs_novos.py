"""Extrai PDFs especificos da raiz raw para txt e atualiza o manifesto.json,
sem reprocessar os demais. Reusa a logica de extracao de extrair_txt.py."""
import json
import sys
from pathlib import Path

from extrair_txt import OUT, extract_pdf


def main(paths):
    manifesto_path = OUT / "manifesto.json"
    mani = json.loads(manifesto_path.read_text(encoding="utf-8"))
    for src in paths:
        src = Path(src)
        text, n, n_ocr = extract_pdf(src.read_bytes())
        dest = OUT / "raw" / (src.stem + ".txt")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        metodo = "texto_embutido" if n_ocr == 0 else ("ocr" if n_ocr == n else "misto")
        mani.append({
            "origem": str(src), "destino": str(dest.relative_to(OUT)),
            "tipo": "pdf", "metodo": metodo, "paginas": n,
            "chars": len(text), "bytes": len(text.encode("utf-8")),
        })
        print(f"{src.name}: {n} pags | {n_ocr} ocr | {len(text)} chars -> {dest.name}")
    manifesto_path.write_text(
        json.dumps(mani, ensure_ascii=False, indent=1), encoding="utf-8")
    print("manifesto atualizado:", len(mani), "itens")


if __name__ == "__main__":
    main(sys.argv[1:])
