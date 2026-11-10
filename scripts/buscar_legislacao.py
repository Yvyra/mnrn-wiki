"""Baixa paginas do Catalogo de Legislacao Municipal (SP) e extrai o texto."""
import html
import re
import sys
import urllib.request


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        raw = r.read().decode("utf-8", errors="replace")
    raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<style.*?</style>", " ", raw, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


if __name__ == "__main__":
    for url in sys.argv[1:]:
        print("\n" + "=" * 70)
        print("URL:", url)
        try:
            print(fetch_text(url)[:4200])
        except Exception as e:
            print("ERRO:", e)
