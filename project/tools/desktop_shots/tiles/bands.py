"""Text row bands (y centre, page px) inside a page rectangle, for two page images (render, comp)."""
import sys
from PIL import Image
def bands(path, x, y, w, h, thr):
    im = Image.open(path).convert("RGB"); px = im.load()
    rows = [sum(1 for i in range(x, x + w) if sum(px[i, j]) < thr) for j in range(y, y + h)]
    out = []; inb = False
    for k, d in enumerate(rows):
        if d > 2 and not inb: st = k; inb = True
        if d <= 2 and inb: out.append((st, k)); inb = False
    if inb: out.append((st, len(rows)))
    return [(round(y + (a + b) / 2, 1), b - a) for a, b in out if b - a >= 4]
a, b = sys.argv[1], sys.argv[2]
for spec in sys.argv[3:]:
    n, x, y, w, h = spec.split(","); x, y, w, h = map(int, (x, y, w, h))
    ra, rb = bands(a, x, y, w, h, 600), bands(b, x, y, w, h, 600)
    print(n); print("  render", ra); print("  comp  ", rb)
