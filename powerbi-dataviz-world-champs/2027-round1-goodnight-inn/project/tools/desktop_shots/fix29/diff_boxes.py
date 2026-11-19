"""Fix round of doc 29: where two stitched renders of the same view differ, in page pixels.

  python diff_boxes.py <before.png> <after.png> [--tol 40] [--out diff.png]

Both renders at the same scale (the 1.84 px per page px of the strips). Prints the page rectangles (x, y, w, h) that
hold every pixel whose colour differs by more than --tol in any channel, joined when they lie within 12 page px of
each other; --out writes the after render with those rectangles outlined. A fix that moved one thing shows one or two
rectangles; anything else on the list is a regression to look at."""
import sys
from PIL import Image, ImageDraw
import numpy as np

a, c = (Image.open(p).convert("RGB") for p in sys.argv[1:3])
tol = int(sys.argv[sys.argv.index("--tol") + 1]) if "--tol" in sys.argv else 40
assert a.size == c.size, (a.size, c.size)
k = a.size[0] / 1920
d = (np.abs(np.asarray(a).astype(int) - np.asarray(c).astype(int)).max(axis=2) > tol)
G = 12  # page px per cell
gh, gw = int(1080 / G) + 1, int(1920 / G) + 1
cells = np.zeros((gh, gw), bool)
ys, xs = np.nonzero(d)
cells[(ys / k / G).astype(int), (xs / k / G).astype(int)] = True
seen = np.zeros_like(cells)
boxes = []
for y in range(gh):
    for x in range(gw):
        if cells[y, x] and not seen[y, x]:
            stack, x0, x1, y0, y1 = [(y, x)], x, x, y, y
            seen[y, x] = True
            while stack:
                cy, cx = stack.pop()
                x0, x1, y0, y1 = min(x0, cx), max(x1, cx), min(y0, cy), max(y1, cy)
                for ny in range(cy - 1, cy + 2):
                    for nx in range(cx - 1, cx + 2):
                        if 0 <= ny < gh and 0 <= nx < gw and cells[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            stack.append((ny, nx))
            boxes.append((x0 * G, y0 * G, (x1 - x0 + 1) * G, (y1 - y0 + 1) * G))
print(f"{int(d.sum())} px differ; {len(boxes)} rectangle(s), page px:")
for b_ in boxes:
    print("  x %d y %d w %d h %d" % b_)
if "--out" in sys.argv:
    im = c.copy()
    dr = ImageDraw.Draw(im)
    for x, y, w, h in boxes:
        dr.rectangle((x * k, y * k, (x + w) * k, (y + h) * k), outline=(255, 0, 255), width=3)
    im.save(sys.argv[sys.argv.index("--out") + 1])
