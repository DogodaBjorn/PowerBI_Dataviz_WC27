"""Coloured marks of a page rectangle in two page images (render, comp), in page px: for each colour asked, the runs of rows
that hold it (y from, y to) with the x extent of the colour in that run. Build step 9 of doc 23: the build bars (Night and
Tangerine bars, the Dusk zero line), the selector's boxes, the plan dot.
usage: marks.py <render png> <comp png> x,y,w,h hex[,tolerance] [hex ...]
The render may be the stitched capture at its own resolution (it is measured there and reported in page px)."""
import sys
from PIL import Image


def runs(path, x, y, w, h, rgb, tol):
    im = Image.open(path).convert("RGB")
    s = im.size[0] / 1920
    im = im.crop((round(x * s), round(y * s), round((x + w) * s), round((y + h) * s))); px = im.load()
    W, H = im.size
    on = [[all(abs(a - b) <= tol for a, b in zip(px[i, j], rgb)) for i in range(W)] for j in range(H)]
    out, st = [], None
    for j in range(H + 1):
        hit = j < H and sum(on[j]) >= 2
        if hit and st is None:
            st = j
        if not hit and st is not None:
            cols = [i for i in range(W) if any(on[k][i] for k in range(st, j))]
            out.append((round(y + st / s, 1), round(y + j / s, 1), round(x + cols[0] / s, 1), round(x + (cols[-1] + 1) / s, 1)))
            st = None
    return out


a, b = sys.argv[1], sys.argv[2]
x, y, w, h = map(int, sys.argv[3].split(","))
for spec in sys.argv[4:]:
    hexv, _, tol = spec.partition(",")
    rgb = tuple(int(hexv.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    ra, rb = runs(a, x, y, w, h, rgb, int(tol or 40)), runs(b, x, y, w, h, rgb, int(tol or 40))
    print(hexv)
    for i in range(max(len(ra), len(rb))):
        r_, c_ = (ra[i] if i < len(ra) else None), (rb[i] if i < len(rb) else None)
        d = "  d " + " ".join(f"{p - q:+.1f}" for p, q in zip(r_, c_)) if r_ and c_ else ""
        print(f"  render y {r_[0]}-{r_[1]} x {r_[2]}-{r_[3]}" if r_ else "  render -", f" comp y {c_[0]}-{c_[1]} x {c_[2]}-{c_[3]}" if c_ else " comp -", d)
