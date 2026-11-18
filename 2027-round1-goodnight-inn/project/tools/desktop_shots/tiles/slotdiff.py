"""Ink of a page rectangle in two page images (render, comp), on any background: the text rows (y centre and height) and
the left and right edge of the ink, in page px, and the differences render minus comp. Ink = a pixel that differs from the
rectangle's most frequent colour (build step 6: bands.py reads dark ink on light only, and page 2 has light text on Night).
The render may be the stitched capture at its own resolution (page.png, about 1.84 px per page px): it is then measured
there and reported in page px, which is finer than the resampled page_1920.png.
usage: slotdiff.py <render png> <comp_page.png> name,x,y,w,h [name,x,y,w,h ...]"""
import sys
from collections import Counter
from PIL import Image


def ink(path, x, y, w, h, thr=90):
    im = Image.open(path).convert("RGB")
    s = im.size[0] / 1920  # capture px per page px
    im = im.crop((round(x * s), round(y * s), round((x + w) * s), round((y + h) * s))); px = im.load()
    W, H = im.size
    bg = Counter(px[i, j] for j in range(0, H, 2) for i in range(0, W, 2)).most_common(1)[0][0]
    on = [[sum(abs(a - b) for a, b in zip(px[i, j], bg)) > thr for i in range(W)] for j in range(H)]
    rows = [sum(r) for r in on]
    bands, st = [], None
    for k, d in enumerate(rows + [0]):
        if d > 1 and st is None:
            st = k
        if d <= 1 and st is not None:
            if (k - st) / s >= 4:
                cols = [i for i in range(W) if any(on[j][i] for j in range(st, k))]
                bands.append((round(y + (st + k) / 2 / s, 1), round((k - st) / s), round(x + cols[0] / s), round(x + (cols[-1] + 1) / s)))
            st = None
    return bands


a, b = sys.argv[1], sys.argv[2]
for spec in sys.argv[3:]:
    n, x, y, w, h = spec.split(","); x, y, w, h = map(int, (x, y, w, h))
    ra, rb = ink(a, x, y, w, h), ink(b, x, y, w, h)
    print(n)
    for i in range(max(len(ra), len(rb))):
        r_, c_ = (ra[i] if i < len(ra) else None), (rb[i] if i < len(rb) else None)
        d = f"  dy {r_[0] - c_[0]:+.1f}  dx left {r_[2] - c_[2]:+d}  right {r_[3] - c_[3]:+d}" if r_ and c_ else ""
        print(f"  render {r_}  comp {c_}{d}")
