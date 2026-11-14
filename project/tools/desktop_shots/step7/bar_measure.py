"""Measure the probe pages b_a (bar) and b_b (chart). Prints page-px positions mapped back to the real page."""
import sys
from PIL import Image
d = sys.argv[1]
x0, x1, y0, y1 = map(int, open(sys.argv[2]).read().split()); s = (x1 - x0) / 480


def near(p, h, t=30):
    c = tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)); return all(abs(a - b) < t for a, b in zip(p, c))


def groups(vals):
    g = []
    for v in vals:
        if g and v - g[-1][-1] <= 1:
            g[-1].append(v)
        else:
            g.append([v])
    return [(round(a[0] / s, 2), round((a[-1] + 1) / s, 2)) for a in g]


im = Image.open(f"{d}/b_a.png").convert("RGB").crop((x0, y0, x1, y1)); px = im.load(); W, H = im.size
mark = groups([y for y in range(H) if near(px[int(10 * s), y], "#E05A22", 20)])
off = 4 - mark[0][0]
bar = groups([y for y in range(H) if near(px[int(200 * s), y], "#2589D8", 30)])
print("bar: marker", mark, "bar rows", bar, "-> page y", [(round(a + off - 100 + 788, 1), round(b + off - 100 + 788, 1)) for a, b in bar])
im = Image.open(f"{d}/b_b.png").convert("RGB").crop((x0, y0, x1, y1)); px = im.load(); W, H = im.size
mark = groups([y for y in range(H) if near(px[int(10 * s), y], "#E05A22", 20)])
off = 4 - mark[0][0]
xq = int(300 * s)
seam = groups([y for y in range(H) if near(px[xq, y], "#E3DFD3", 8)])
dusk = groups([y for y in range(H) if near(px[xq, y], "#4B5466", 22)])
conv = lambda g: [(round(a + off - 60 + 828, 1), round(b + off - 60 + 828, 1)) for a, b in g]  # noqa: E731
print("chart: marker", mark, "seam rows", conv(seam), "dusk rows", conv(dusk))
# tick label ink rows at x 30..80 (page 802..852) and year label rows
tick = groups([y for y in range(H) if sum(1 for x in range(int(24 * s), int(86 * s)) if not near(px[x, y], "#FFFFFF", 60)) > 1])
print("tick label rows", conv(tick))
im.save(f"{d}/b_b_c.png")
