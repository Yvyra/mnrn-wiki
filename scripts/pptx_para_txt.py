"""Extrai texto de um .pptx (slides + notas) para .txt, sem dependencias
externas (pptx e' um zip de XML)."""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def slide_text(xml: bytes) -> str:
    root = ET.fromstring(xml)
    parts = []
    for t in root.iter(NS + "t"):
        if t.text:
            parts.append(t.text)
    return " ".join(parts)


def extract(path: Path) -> str:
    out = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        slides = sorted(
            (n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda n: int(re.search(r"(\d+)", n).group(1)),
        )
        notes = {
            int(re.search(r"(\d+)", n).group(1)): n
            for n in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)
        }
        for n in slides:
            num = int(re.search(r"(\d+)", n).group(1))
            out.append(f"\n===== SLIDE {num} =====")
            out.append(slide_text(z.read(n)))
            if num in notes:
                out.append(f"--- notas do slide {num} ---")
                out.append(slide_text(z.read(notes[num])))
    return "\n".join(out)


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".txt")
    text = extract(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")
    print(f"extraido {src.name} -> {dst} ({len(text)} chars)")
