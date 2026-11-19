"""Build step 11 of doc 23: every slot of a page view, render against comp, one line each (render minus comp, page px).

usage: slot_sheet.py <render png> <comp png> <page> [state]        page: p1-brand-review | p2-investment-strategy
                                                                   state (page 2): rec | alts | build

For every slot of the slot map (design-prototypes/opzet-layout.json) that the view shows: the number of text rows in
the render and in the comp, and the largest difference in y, left edge and right edge over the paired rows
(tiles/slotdiff.py's ink). A text slot within 2 px on all three is "ok"; anything else is listed with its numbers.
Charts, tables and the selector are listed apart: their rows of ink are marks, ticks and labels together, so the
figures there only say where to look (the logs of steps 5 to 9 measured those on scratch pages).
Give the stitched render at its own resolution (about 1.84 px per page px) or the 1920 px version.
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def load(path, name):
    argv, sys.argv = sys.argv, [str(path)]  # slotdiff.py runs on import; keep it quiet
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except (IndexError, ValueError):
        pass
    sys.argv = argv
    return mod


ink = load(HERE.parent / "tiles" / "slotdiff.py", "slotdiff").ink
render, comp, page = sys.argv[1], sys.argv[2], sys.argv[3]
state = sys.argv[4] if len(sys.argv) > 4 else None
pages = json.loads((ROOT / "project" / "design-prototypes" / "opzet-layout.json").read_text(encoding="utf-8"))["pages"]
pages = pages if isinstance(pages, list) else list(pages.values())
slots = next(p for p in pages if p["name"] == page)["visuals"]
MARKS = ("ch_", "tbl_", "sl_", "hero_s_", "img_")
ok, text_dev, marks = 0, [], []
for v in slots:
    if v.get("state") and state not in v["state"]:
        continue
    x, y, w, h = v["x"], v["y"], v["w"], v["h"]
    a, b = ink(render, x, y, w, h), ink(comp, x, y, w, h)
    n = min(len(a), len(b))
    dy = max((abs(a[i][0] - b[i][0]) for i in range(n)), default=0)
    dl = max((abs(a[i][2] - b[i][2]) for i in range(n)), default=0)
    dr = max((abs(a[i][3] - b[i][3]) for i in range(n)), default=0)
    line = f"{v['name']:26} rows {len(a)}/{len(b)}  max dy {dy:4.1f}  left {dl:3d}  right {dr:3d}"
    if v["name"].startswith(MARKS):
        marks.append(line)
    elif len(a) == len(b) and dy <= 2 and dl <= 2 and dr <= 2:
        ok += 1
    else:
        text_dev.append(line)
print(f"text slots within 2 px: {ok}; outside: {len(text_dev)}")
for ln in text_dev:
    print("  " + ln)
print("charts, tables, selector (indicative):")
for ln in marks:
    print("  " + ln)
