"""Final round (16 Nov 2026): where the cards begin and end on a page render, measured in the picture.

  python gaps.py <page render at 1920> [x ...]

Walks down the render at the given page x (default 46 and 1874: inside the first and the last card column, clear of
their content) and prints every run of card white (#FFFFFF within 3 levels) of 40 px or more as "top to bottom",
and the gaps between the runs. The render is 1916 or 1920 px wide for a 1920 px page; y is page px."""
import sys
from PIL import Image

im = Image.open(sys.argv[1]).convert("RGB")
w, h = im.size
sx = w / 1920
for x in [int(a) for a in sys.argv[2:]] or [46, 1874]:
    col = [min(im.getpixel((round(x * sx), y))) >= 252 for y in range(h)]
    runs, y = [], 0
    while y < h:
        if col[y]:
            y0 = y
            while y < h and col[y]:
                y += 1
            if y - y0 >= 40:
                runs.append((y0, y))
        else:
            y += 1
    gaps = [b[0] - a[1] for a, b in zip(runs, runs[1:])]
    print(f"x {x}: cards " + ", ".join(f"{a} to {b}" for a, b in runs) + f" | gaps {gaps} | under the last card {h - runs[-1][1] if runs else '-'}")
