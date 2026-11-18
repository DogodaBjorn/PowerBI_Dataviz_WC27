"""Step 2 spikes: measure a bridge screenshot of a scratch page (page 1920 x 1080; any capture scale).

Usage: python measure.py hero <png>        row pitch, header height, reference-line continuity, scrollbars
       python measure.py selector <png>    slicer tile pitch against table row pitch
Coordinates are printed in page pixels (the capture is scaled back by width / 1920).
"""
import sys
from PIL import Image

mode, path = sys.argv[1], sys.argv[2]
im = Image.open(path).convert("RGB")
px = im.load()


def _night(c):
    return abs(c[0] - 0x12) < 12 and abs(c[1] - 0x23) < 12 and abs(c[2] - 0x3D) < 12


def _fiducials():
    """The scratch pages carry a Night 16 px square in the top-left and the bottom-right page corner: the capture also
    holds Desktop's canvas margin and the filter-pane strip, so the page is located from the two squares."""
    w, h = im.size
    tl = [(x, y) for y in range(0, h // 4) for x in range(0, w // 4) if _night(px[x, y])]
    br = [(x, y) for y in range(h - h // 4, h) for x in range(w - w // 4, w) if _night(px[x, y])]
    ox, oy = min(x for x, _ in tl), min(y for _, y in tl)
    bx, by = max(x for x, _ in br) + 1, max(y for _, y in br) + 1
    return ox, oy, (bx - ox) / 1920, (by - oy) / 1080


OX, OY, _KX, K = _fiducials()
# the page is scaled evenly; the vertical measure is the reliable one (the page's right edge sits under the pane strip)
print(f"page origin in the capture ({OX}, {OY}), scale {K:.4f} (horizontal fiducial distance gives {_KX:.4f})")


class _Px:
    """Pixel access in page-scaled capture coordinates: px[x, y] with the page origin taken out."""
    def __getitem__(self, xy):
        return _raw[min(im.size[0] - 1, xy[0] + OX), min(im.size[1] - 1, xy[1] + OY)]


_raw = px
px = _Px()


def dark(c, limit=200):
    return min(c) < limit


def rows_with_ink(x0, x1, y0, y1, limit=200):
    """Page-y runs (start, end) in which any pixel between page x0..x1 is darker than the limit."""
    runs, start = [], None
    for y in range(int(y0 * K), int(y1 * K)):
        ink = any(dark(px[x, y], limit) for x in range(int(x0 * K), int(x1 * K)))
        if ink and start is None:
            start = y
        if not ink and start is not None:
            runs.append((start / K, y / K))
            start = None
    if start is not None:
        runs.append((start / K, y1))
    return runs


def cols_with_colour(y0, y1, x0, x1, test):
    """Page-x runs in which every pixel between page y0..y1 passes the colour test (a full-height vertical line)."""
    runs, start = [], None
    for x in range(int(x0 * K), int(x1 * K)):
        full = all(test(px[x, y]) for y in range(int(y0 * K), int(y1 * K)))
        if full and start is None:
            start = x
        if not full and start is not None:
            runs.append((start / K, x / K))
            start = None
    return runs


def is_night(c):
    return abs(c[0] - 0x12) < 40 and abs(c[1] - 0x23) < 40 and abs(c[2] - 0x3D) < 40


def is_scroll(c):
    return abs(c[0] - c[1]) < 6 and abs(c[1] - c[2]) < 6 and 150 < c[0] < 200


if mode == "hero":
    X, Y, W, H = 56, 240, int(sys.argv[3]) if len(sys.argv) > 3 else 1000, 372
    # text rows in the Move column
    runs = rows_with_ink(X + 4, X + 270, Y, Y + H + 60)
    mids = [(a + b) / 2 for a, b in runs if b - a > 5]
    print("text rows (page y mid):", [round(m, 1) for m in mids])
    if len(mids) > 2:
        pitches = [round(mids[i + 1] - mids[i], 2) for i in range(1, len(mids) - 1)]
        print("row pitch (data rows):", pitches, "| header mid to first row mid:", round(mids[1] - mids[0], 2))
    # the header rule: a full-width horizontal dark line
    for y in range(int(Y * K), int((Y + 60) * K)):
        if all(dark(px[x, y], 170) for x in range(int((X + 8) * K), int((X + 400) * K), 3)):
            print("header rule at page y", round(y / K, 2))
            break
    # reference lines: columns that are Night over the full height of the ten rows
    y_first = Y + 36
    # at a fractional zoom the image edges blend for one capture pixel per row boundary: a line counts as unbroken
    # when every sampled pixel is Night or that blend (never white)
    def is_line(c):
        return c[0] < 150 and c[1] < 160 and c[2] < 175

    for label, x0, x1 in (("8 %", X + 480, X + 676), ("0", X + 740, X + 920)):
        for depth in (340, 300, 200, 100, 34):
            lines = cols_with_colour(y_first, y_first + depth - 4, x0, x1, is_line)
            if lines:
                print(f"reference line {label}: unbroken over {depth} px at page x", [(round(a, 2), round(b, 2)) for a, b in lines])
                break
        else:
            print(f"reference line {label}: NOT found as an unbroken line")
    # scrollbars: grey bars at the right and bottom edge of the slot
    v = cols_with_colour(Y + 100, Y + 200, X + W - 20, X + W + 4, is_scroll)
    hbar = any(all(is_scroll(px[x, y]) for x in range(int((X + 100) * K), int((X + 300) * K), 5)) for y in range(int((Y + H - 16) * K), int((Y + H + 2) * K)))
    print("vertical scrollbar:", bool(v), "| horizontal scrollbar:", hbar)

if mode == "selector":
    # usage: measure.py selector <png> [table y] [capex column offset] — tiles are measured by their check boxes,
    # table rows by the Capex column (every value has the same glyph heights: "$", digits, "M")
    SX, SY, SW, SH = 792, 280, 216, 320
    TX = 1008
    ty = float(sys.argv[3]) if len(sys.argv) > 3 else 248
    cx = float(sys.argv[4]) if len(sys.argv) > 4 else 92
    boxes = [(a, b) for a, b in rows_with_ink(SX + 6, SX + 26, SY - 6, SY + SH + 6, 120) if b - a > 8]
    rows = [(a, b) for a, b in rows_with_ink(TX + cx + 6, TX + cx + 62, ty + 30, SY + SH + 12) if b - a > 5]
    b_mid = [round((a + b) / 2, 2) for a, b in boxes]
    r_mid = [round((a + b) / 2, 2) for a, b in rows]
    print("check boxes (page y):", [(round(a, 1), round(b, 1)) for a, b in boxes][:3], "... count", len(boxes))
    print("tile centres:", b_mid)
    print("row centres: ", r_mid)
    if len(b_mid) == 10 and len(r_mid) == 10:
        d = [round(r - b, 2) for b, r in zip(b_mid, r_mid)]
        print("row minus tile, per row:", d, "| spread:", round(max(d) - min(d), 2))
        print("tile pitch:", round((b_mid[9] - b_mid[0]) / 9, 3), "| row pitch:", round((r_mid[9] - r_mid[0]) / 9, 3))
    hdr = [(a, b) for a, b in rows_with_ink(TX + cx + 6, TX + cx + 62, ty, ty + 44) if b - a > 5]
    print("header text (page y):", [(round(a, 1), round(b, 1)) for a, b in hdr][:1])
    for y in range(int(ty * K), int((ty + 60) * K)):
        if all(dark(px[x, y], 170) for x in range(int((TX + 8) * K), int((TX + 300) * K), 3)):
            print("header rule at page y", round(y / K, 2), "-> header height", round(y / K - ty, 2))
            break
    v = cols_with_colour(SY + 60, SY + 160, TX + 300, TX + 380, is_scroll)
    print("vertical scrollbar:", bool(v))
