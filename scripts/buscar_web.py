"""Busca simples no DuckDuckGo (HTML) e lista titulos + URLs."""
import html
import re
import sys
import urllib.parse
import urllib.request


def search(q: str, n: int = 8):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
    hits = []
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        link = html.unescape(m.group(1))
        tit = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if tit and link.startswith("http"):
            hits.append((tit, link))
        if len(hits) >= n:
            break
    return hits


if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    for i, (t, u) in enumerate(search(q), 1):
        print(f"{i}. {t}\n   {u}\n")
