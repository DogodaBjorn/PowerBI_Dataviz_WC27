"""Cut a report page out of a bridge capture of a Desktop window (cap.mjs), whatever the window's size and zoom.

  python project/tools/desktop_shots/crop_page.py <capture.png> <page.png>

A capture holds the canvas with the page somewhere in it. The page is found from its white cards: the first pixel row
with a long white run is the top of the first card row (page y 148 on both pages of the final report), and in the row
8 px under it the first white run starts at page x 32 and the last one ends at page x 1888. From that the scale and the
page's corner follow, and the page is cut and brought to 1920 x 1080. Good to about 2 page px (the cards' rounded
corners); for a measurement, place two rectangles at known x in a throwaway copy and read their pixels (doc 39).
Only for throwaway windows: Bjorn's own window is not captured (docs 37 and 39).
"""
import sys

from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
W, H = im.size
px = im.load()
WHITE = (255, 255, 255)


def runs(y):
    out, s = [], None
    for x in range(W):
        w = px[x, y] == WHITE
        if w and s is None:
            s = x
        if not w and s is not None:
            out.append((s, x))
            s = None
    if s is not None:
        out.append((s, W))
    return out


top = None
for y in range(H):
    r = [b - a for a, b in runs(y)]
    if r and max(r) > 0.25 * W and sum(v for v in r if v > 50) > 0.4 * W:
        top = y
        break
if top is None:
    sys.exit("no card row found: is this a capture of a report page?")
rr = [(a, b) for a, b in runs(top + 8) if b - a > 50 and a < W * 0.93]
first, last = rr[0][0], rr[-1][1]
s = (last - first) / 1856
x0, y0 = first - 32 * s, top - 148 * s
box = (round(x0), round(y0), round(x0 + 1920 * s), round(y0 + 1080 * s))
print(f"{src}: {s:.4f} px per page px, the page at {box}")
im.crop(box).resize((1920, 1080), Image.LANCZOS).save(dst)
