"""Review round 2, step D: a whole-page bridge capture cut to page pixels (a wide Desktop window; no strips needed).

usage: python page_crop.py <capture.png> <out.png> [--scale 2] [--card x,y,w,h]

In a wide session window the bridge draws the 1920 x 1080 page whole, fitted to the canvas (15 Nov: 0.469 logical px per
page px, 1.41 capture px per page px at scale 3), with Desktop's wallpaper around it. The page is found through one white
card whose page rect is known (default: page 1's KPI card, 32, 168, 1856, 120; page 2 Recommended: the hero card
32, 168, 1040, 488 as --card): its four edges in the capture give the scale in x and in y and the page's origin. The
page is cut out and resampled to 1920 x 1080 times --scale (default 2: a pixel reference for 1 px of the page).
Prints the scales; x and y within 0.5 % of each other is a sound capture.
"""
import sys
from PIL import Image
import numpy as np

src, out = sys.argv[1], sys.argv[2]
scale = int(sys.argv[sys.argv.index("--scale") + 1]) if "--scale" in sys.argv else 2
card = tuple(int(v) for v in sys.argv[sys.argv.index("--card") + 1].split(",")) if "--card" in sys.argv else (32, 168, 1856, 120)
im = Image.open(src).convert("RGB")
a = np.asarray(im).astype(int)
white = (a.min(axis=2) >= 250)
H, W = white.shape
# the card: the longest white run on any row is its width; rows that carry such a run are its height
best = (0, 0, 0)
for y in range(0, H, 4):
    row = white[y]
    edges = np.flatnonzero(np.diff(np.concatenate(([0], row.view(np.int8), [0]))))
    runs = edges.reshape(-1, 2)
    if len(runs):
        i = np.argmax(runs[:, 1] - runs[:, 0])
        if runs[i, 1] - runs[i, 0] > best[1] - best[0]:
            best = (runs[i, 0], runs[i, 1], y)
x0, x1, yref = best
want = card[2] / card[3]
# its height: the white run of a column inside the card's right padding (past the corner radius, clear of any text);
# of the cards that share that column, the one whose aspect is the card's
col = white[:, x1 - 14]
edges = np.flatnonzero(np.diff(np.concatenate(([0], col.view(np.int8), [0])))).reshape(-1, 2)
runs = [(int(a_), int(b_)) for a_, b_ in edges if b_ - a_ > 20]
y0, y1 = min(runs, key=lambda r: abs((x1 - x0) / (r[1] - r[0]) - want))
# The card's shadow blurs its top and bottom edge by a pixel or two, so its height is a poor scale (1.39 where the width
# gave 1.405; the F1 and F4 cards of the same capture gave 1.405 and 1.402). The capture's pixels are square: the scale is
# the width's, and the page's origin in y comes from the card's centre.
sx = sy = (x1 - x0) / card[2]
ox, oy = x0 - card[0] * sx, (y0 + y1) / 2 - (card[1] + card[3] / 2) * sy
print(f"card in the capture: x {x0}..{x1}, y {y0}..{y1}; scale {sx:.4f} capture px per page px (the card's height alone: {(y1 - y0) / card[3]:.4f}); page origin {ox:.1f}, {oy:.1f}")
box = (ox, oy, ox + 1920 * sx, oy + 1080 * sy)
page = im.transform((1920 * scale, 1080 * scale), Image.EXTENT, box, Image.BICUBIC)
page.save(out)
print("written", out, page.size)
