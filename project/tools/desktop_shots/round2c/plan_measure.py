"""The plan chart of Recommended in a stitched strip render, in page px (review round 2, step C of doc 25).

  python plan_measure.py <rec_<case>.png>      the stitched render of step9/round.py shoot, at its own resolution

Prints where the six year labels stand, where the gate line and the emphasised line run, how far the gridlines reach,
and the ink box of each end label card. Read against opzet_report.py: PLAN_END_X (the last year), PLAN_CUM_W (171 px a
year), PLAN_END_GAP (label clear of the gridlines' ends). A strip render snaps a chart by up to 2 px (step 9), so y
readings settle nothing finer than that; the typed ticks and the label heights hang on the published capture
(PLAN_TICK_ZERO_Y).
"""
import sys

import numpy as np
from PIL import Image

im = Image.open(sys.argv[1]).convert("RGB")
s = im.width / 1920
a = np.asarray(im).astype(int)


def near(hexv, tol):
    r, g, b = (int(hexv[i:i + 2], 16) for i in (1, 3, 5))
    return (abs(a[..., 0] - r) + abs(a[..., 1] - g) + abs(a[..., 2] - b)) < tol


def span(mask, x0, x1, y0, y1):
    sub = mask[round(y0 * s):round(y1 * s), round(x0 * s):round(x1 * s)]
    ys, xs = np.where(sub.any(axis=1))[0], np.where(sub.any(axis=0))[0]
    if not len(ys):
        return None
    return tuple(round(float(v), 1) for v in (x0 + xs.min() / s, x0 + (xs.max() + 1) / s, y0 + ys.min() / s, y0 + (ys.max() + 1) / s))


dusk, night, blue, hair, deep = near("#4B5466", 120), near("#12233D", 60), near("#2589D8", 50), near("#E3DFD3", 20), near("#1763A8", 80)
for yr, cx in zip(range(2027, 2033), [864 + i * 171 for i in range(6)]):
    sp = span(dusk, cx - 30, cx + 30, 953, 972)
    print(yr, "tick label", sp, "centre", None if not sp else round((sp[0] + sp[1]) / 2, 1))
print("gate line                  ", span(night, 1100, 1126, 880, 900))
print("emphasised line (x0 x1 y0 y1)", span(blue, 850, 1724, 836, 952))
print("gridline at +$10M          ", span(hair, 850, 1760, 876, 882))
print("zero line                  ", span(near("#4B5466", 40), 850, 1760, 911, 917))
for name, (y0, y1) in {"High": (836, 864), "Expected": (878, 908), "Low": (917, 946)}.items():
    print(f"end label {name:9}", span(dusk | deep, 1726, 1880, y0, y1))
