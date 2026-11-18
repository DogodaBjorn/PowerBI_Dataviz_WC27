"""Build step 9 of doc 23: the Build renders against the comp, one line per slot and view (render minus comp, page px).
usage: summary.py <renders dir> <comp dir> [view ...]     renders dir holds f_<view>/<view>.png, comp dir comp_<view>.png
Text slots: the number of text rows in the render and in the comp, and the largest difference in y, left edge and right
edge over the paired rows (tiles/slotdiff.py). Marks: bars, boxes and the plan dot by colour (step9/marks.py)."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(path, name):
    argv, sys.argv = sys.argv, [str(path)]  # both scripts run on import; keep them quiet
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except (IndexError, ValueError):
        pass
    sys.argv = argv
    return mod


ink = load(HERE.parent / "tiles" / "slotdiff.py", "slotdiff").ink
runs = load(HERE / "marks.py", "marks").runs
TEXT = {  # slot: (x, y, w, h)
    "c_scatter_sub": (56, 240, 672, 24), "c_build_head": (792, 180, 600, 60), "sl_moves names": (822, 282, 180, 316), "tbl_moves header": (1010, 244, 345, 30),
    "tbl_moves Answers": (1010, 282, 90, 316), "tbl_moves Capex": (1104, 282, 58, 316), "tbl_moves NPV": (1165, 282, 72, 316), "tbl_moves A year": (1240, 282, 112, 316),
    "c_sel_footer": (792, 606, 400, 28), "c_you_title": (1398, 256, 450, 40), "c_you_nums values": (1384, 304, 464, 28), "c_you_nums labels": (1384, 332, 464, 46),
    "c_you_range": (1384, 384, 300, 24), "c_you_rules": (1384, 408, 464, 48), "ch_build_bars names": (1386, 466, 170, 165), "ch_cmp_build title": (56, 688, 1500, 30),
    "tag_cmp_build": (1722, 694, 136, 26),
}
MARKS = {  # name: (x, y, w, h, hex, tolerance)
    "sl_moves boxes (unchecked, Dusk)": (796, 282, 26, 316, "#4B5466", 60), "ch_build_bars Tangerine bars": (1560, 460, 288, 170, "#E05A22", 30),
    "alarm band": (1370, 250, 490, 50, "#E05A22", 30),
}
rd, cd = Path(sys.argv[1]), Path(sys.argv[2])
for view in sys.argv[3:]:
    r, c = str(rd / f"f_{view}" / f"{view}.png"), str(cd / f"comp_{view}.png")
    print(f"== {view}")
    for slot, (x, y, w, h) in TEXT.items():
        a, b = ink(r, x, y, w, h), ink(c, x, y, w, h)
        n = min(len(a), len(b))
        if not a and not b:
            print(f"  {slot:28} empty in both")
            continue
        dy = max((abs(a[i][0] - b[i][0]) for i in range(n)), default=0)
        dl = max((abs(a[i][2] - b[i][2]) for i in range(n)), default=0)
        dr = max((abs(a[i][3] - b[i][3]) for i in range(n)), default=0)
        print(f"  {slot:28} rows {len(a)}/{len(b)}  max dy {dy:.1f}  left {dl}  right {dr}")
    for name, (x, y, w, h, hexv, tol) in MARKS.items():
        rgb = tuple(int(hexv[i:i + 2], 16) for i in (1, 3, 5))
        a, b = runs(r, x, y, w, h, rgb, tol), runs(c, x, y, w, h, rgb, tol)
        n = min(len(a), len(b))
        d = [max((abs(a[i][k] - b[i][k]) for i in range(n)), default=0) for k in range(4)]
        print(f"  {name:28} runs {len(a)}/{len(b)}  max d: top {d[0]:.1f} bottom {d[1]:.1f} left {d[2]:.1f} right {d[3]:.1f}")
