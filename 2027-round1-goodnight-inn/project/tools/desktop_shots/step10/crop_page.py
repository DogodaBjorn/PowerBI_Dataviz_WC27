"""Crop a bridge capture of a small page to the page (build step 10).

In the narrow session window a capture is 1200 x 5142 px: the page fitted to the width, Night margin above and under
it, and the collapsed Filters pane as a white strip at the right. The page is the rows that are not Night at one x,
between the left edge and the pane.

  python crop_page.py <out dir> <capture.png>[=<page width>] ...     writes <out dir>/<name>.png and prints the scale
"""
import sys
from pathlib import Path

from PIL import Image

NIGHT = (18, 35, 61)


def night(c):
    return sum(abs(a - b) for a, b in zip(c[:3], NIGHT)) < 40


out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
for arg in sys.argv[2:]:
    f, _, pw = arg.partition("=")
    im = Image.open(f).convert("RGB")
    w, h = im.size
    pane = next((x for x in range(w) if not night(im.getpixel((x, 40)))), w)   # the Filters pane starts here
    xs = range(4, pane - 4, 16)
    rows = [y for y in range(h) if sum(1 for x in xs if not night(im.getpixel((x, y)))) > len(xs) // 3]
    y0, y1 = rows[0], rows[-1] + 1
    cols = [x for x in range(pane) if not night(im.getpixel((x, (y0 + y1) // 2)))]
    x0, x1 = cols[0], cols[-1] + 1
    page = im.crop((x0, y0, x1, y1))
    page.save(out / Path(f).name)
    print(Path(f).name, (x0, y0, x1, y1), page.size, (f"{page.size[0] / int(pw):.3f} px per page px" if pw else ""))
