"""Where Power BI drew the plan chart's plot: the +20 gridline, the zero line, the gate line, the first and last x of the
emphasised line. Page px, from the stitched capture. usage: scan_cum.py <page.png> [line hex]"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB"); s = im.size[0] / 1920; px = im.load()
LINE = sys.argv[2] if len(sys.argv) > 2 else "#2589D8"


def near(p, h, t=14):
    c = tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)); return all(abs(a - b) < t for a, b in zip(p, c))


def rows(xp, hexv, t, y0=822, y1=985):
    x = int(xp * s); ys = [y for y in range(int(y0 * s), int(y1 * s)) if near(px[x, y], hexv, t)]
    groups = []
    for y in ys:
        if groups and y - groups[-1][-1] <= 1:
            groups[-1].append(y)
        else:
            groups.append([y])
    return [round((g[0] + g[-1] + 1) / 2 / s, 1) for g in groups]


def cols(yp, hexv, t, x0=790, x1=1880):
    y = int(yp * s); xs = [x for x in range(int(x0 * s), int(x1 * s)) if near(px[x, y], hexv, t)]
    groups = []
    for x in xs:
        if groups and x - groups[-1][-1] <= 1:
            groups[-1].append(x)
        else:
            groups.append([x])
    return [(round(g[0] / s, 1), round((g[-1] + 1) / s, 1)) for g in groups]


for xq in (960, 1400):
    print("x", xq, "seam rows", rows(xq, "#E3DFD3", 8), "dusk rows", rows(xq, "#4B5466", 22))
# the gate line: Night pixels in a row between the top gridline and the zero line, away from text
for yq in (875, 925, 940):
    print("y", yq, "night cols", cols(yq, "#12233D", 40)[:8])
# the emphasised line: leftmost and rightmost pixel of its colour anywhere in the plot
xs = [x for x in range(int(790 * s), int(1880 * s)) if any(near(px[x, y], LINE, 18) for y in range(int(840 * s), int(955 * s)))]
print("line x", round(xs[0] / s, 1), round((xs[-1] + 1) / s, 1))
ys0 = [y for y in range(int(840 * s), int(955 * s)) if near(px[xs[0] + 3, y], LINE, 18)]
ys1 = [y for y in range(int(840 * s), int(955 * s)) if near(px[xs[-1] - 3, y], LINE, 18)]
print("line y at start", round(sum(ys0) / len(ys0) / s, 1), "at end", round(sum(ys1) / len(ys1) / s, 1))
