"""Review round 2, step D: the contrast of a piece of text as it is DRAWN (text under a tinted band, a glyph from a fallback
font): the darkest pixel of a page rectangle against the rectangle's most common colour, as a WCAG ratio.

usage: python contrast_probe.py <render> name,x,y,w,h [name,x,y,w,h ...]      page px; the render at any scale

a11y_check.py reads colours from the files, so it sees Night on a white card for F1's "Commissions"; the label lies
under the chart's band (Warm Grey at 30 %). This reads what the render shows. A stroke's core is the darkest pixel; at
1.84 px per page px a 12 pt stroke has one, so the figure is the text colour's, a little lighter if anything.
"""
import sys
from collections import Counter
from PIL import Image


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


im = Image.open(sys.argv[1]).convert("RGB")
s = im.size[0] / 1920
for arg in sys.argv[2:]:
    name, x, y, w, h = arg.split(",")
    x, y, w, h = (float(v) for v in (x, y, w, h))
    raw = im.crop((int(x * s), int(y * s), int((x + w) * s), int((y + h) * s))).tobytes()
    px = list(zip(raw[0::3], raw[1::3], raw[2::3]))
    bg = Counter(px).most_common(1)[0][0]
    ink = min(px, key=lum)
    a, b = sorted((lum(bg), lum(ink)), reverse=True)
    print(f"{name:22s} ink #{ink[0]:02X}{ink[1]:02X}{ink[2]:02X} on #{bg[0]:02X}{bg[1]:02X}{bg[2]:02X}: {(a + 0.05) / (b + 0.05):.1f}:1")
