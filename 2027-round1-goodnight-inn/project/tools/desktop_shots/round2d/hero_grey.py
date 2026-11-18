"""Review round 2, step D (DS2-04's test): in a greyscale copy of Recommended, are package A's rows the darkest marks of the
hero table's NPV panel?

usage: python hero_grey.py <render of Recommended, any scale> [<grey copy out.png>]

Reads the NPV bar column of tbl_hero (page x and rows from sketch_model's constants and the hero table's rect), turns the
render to grey (ITU-R 601 luma, as an office printer or a greyscale screenshot would), leaves the full-height zero line
out (it is Night in every row: a reference line, not a row's mark) and prints the darkest grey of each row's bar.
Exit code 1 unless the three darkest rows are package A's rows. The order of the rows is the hero's (Hero Sort):
rows 1 to 3 are package A in every case (number_checks.py asserts the order and the statuses against the spec).
"""
import sys
from pathlib import Path
from PIL import Image
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import sketch_model as sm  # noqa: E402

src = sys.argv[1]
im = Image.open(src).convert("RGB")
s = im.size[0] / 1920
g = np.asarray(im.convert("L")).astype(int)
# the hero table as built (opzet_report.p2_hero): rect 56, 244, rows of 34 px under a header of 33.5 px
X0 = sm.HERO_X + sum(sm.HERO_COLS[:5])
X1 = X0 + sm.HERO_COLS[5]
Y0, ROW = 244 + 33.5, 34
panel = g[int((Y0) * s):int((Y0 + 10 * ROW) * s), int(X0 * s):int(X1 * s)]
line = int(np.argmin(panel.mean(axis=0)))  # the zero line: the darkest column over all ten rows
rows = []
for i in range(10):
    band = g[int((Y0 + i * ROW + 9) * s):int((Y0 + i * ROW + 25) * s), int(X0 * s):int(X1 * s)].copy()
    band[:, max(0, line - 1):line + 2] = 255  # the zero line itself (1 page px) and the capture pixel either side of it
    cols = band.min(axis=0)
    mark = cols[cols < 235]
    rows.append((i + 1, int(mark.min()) if len(mark) else None, len(mark) / s))
print(f"NPV panel x {X0}..{X1} page px, zero line at page x {X0 + line / s:.1f}; grey 0 = black, 255 = white")
for i, dark, w in rows:
    what = f"darkest grey of the bar {dark:3d}, about {w:.1f} px beside the zero line" if dark is not None else "no bar wider than the zero line (the value rounds to under $0.2M)"
    print(f"  row {i:2d} {'package A' if i <= 3 else '         '}  {what}")
a = [r[1] for r in rows[:3] if r[1] is not None]
rest = [r[1] for r in rows[3:] if r[1] is not None]
# a bar of 1 to 2 px beside the line is blurred by the capture: its darkest pixel reads lighter than the fill, never darker
ok = bool(a) and max(a) < min(rest)
print("every bar of package A is darker than every other bar of the NPV panel:", "yes" if ok else "NO",
      f"(A at most {max(a)}, every other row at least {min(rest)})")
if len(sys.argv) > 2:
    x0, y0, x1, y1 = 32, 168, 1072, 656  # the hero card
    im.convert("L").crop((int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))).save(sys.argv[2])
    print("grey copy of the hero card:", sys.argv[2])
sys.exit(0 if ok else 1)
