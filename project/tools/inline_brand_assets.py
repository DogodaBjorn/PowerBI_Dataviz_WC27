"""Embed SVG logo files into brand HTML pages so each page is self-contained.

A page that references `assets/x.svg` breaks the moment it is opened outside the
repo (sent as a single file, attached, previewed). This rewrites every
<img src="....svg"> into a base64 data URI and keeps the original path in
data-src, so re-running after a logo change (project/tools/brand_logos.py)
re-embeds the current file. Idempotent.

Usage: python project/tools/inline_brand_assets.py <page.html> [<page.html> ...]
"""
import base64
import os
import re
import sys

IMG = re.compile(r'<img\b([^>]*?)>', re.S)
SRC = re.compile(r'\ssrc="([^"]+)"')
DATA_SRC = re.compile(r'\sdata-src="([^"]+)"')


def inline(page):
    base = os.path.dirname(os.path.abspath(page))
    html = open(page, encoding="utf-8").read()
    count = 0

    def fix(m):
        nonlocal count
        attrs = m.group(1)
        ds = DATA_SRC.search(attrs)
        s = SRC.search(attrs)
        path = ds.group(1) if ds else (s.group(1) if s else None)
        if not path or not path.endswith(".svg"):
            return m.group(0)
        full = os.path.normpath(os.path.join(base, path))
        with open(full, "rb") as f:
            uri = "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")
        attrs = SRC.sub("", attrs)
        attrs = DATA_SRC.sub("", attrs)
        count += 1
        return f'<img data-src="{path}" src="{uri}"{attrs}>'

    html = IMG.sub(fix, html)
    with open(page, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{page}: {count} logo(s) embedded")


for p in sys.argv[1:]:
    inline(p)
