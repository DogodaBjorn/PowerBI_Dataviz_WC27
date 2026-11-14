"""Does the mouse reach every live visual in the PUBLISHED report? A check from the report files (build step 12).

usage: python project/tools/strip_check.py [report dir] [--strip 36]

In the Power BI service every visual container is 20 screen px taller than its visual: a strip above it, for the
visual header, that takes the mouse even when the header is switched off (measured on the published report with
tools/desktop_shots/step12/hit_test.js; Desktop's edit mode does not show it). A visual higher in the z-order so
blinds whatever lies under the strip above it. The strip is 20 SCREEN px: 31 page px in a 1366 px window, so the
check takes 36 page px unless told otherwise.

Live = a button, a slicer, or a visual that opens a tooltip. For every page and state (the bookmarks' display
states) the check lists each live visual that has, higher in the z-order and on screen with it,
  - the strip of another visual reaching into it (fails when it takes more than 2 % of the live visual's area), or
  - a visual that is not live lying over it (fails: its body and its strip take the mouse there).
Two live visuals that overlap (the scatter's layers) are a design decision and are listed as a note.
It also fails when a chart or a table has no interaction list: a click on a mark or a row would cross-filter the page.
Exit code 1 on a failure.
"""
import json
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
REPORT = Path(args[0]) if args else Path(__file__).resolve().parents[1] / "pbip" / "GoodnightInn-opzet.Report"
STRIP = float(sys.argv[sys.argv.index("--strip") + 1]) if "--strip" in sys.argv else 36
if "--strip" in sys.argv and args and args[-1] == sys.argv[sys.argv.index("--strip") + 1]:
    args.pop(); REPORT = Path(args[0]) if args else Path(__file__).resolve().parents[1] / "pbip" / "GoodnightInn-opzet.Report"
DEF = REPORT / "definition"
MOUSE_TYPES = {"actionButton", "advancedSlicerVisual", "slicer"}
SELECTABLE = {"lineChart", "clusteredColumnChart", "clusteredBarChart", "barChart", "scatterChart", "tableEx", "stackedAreaChart", "waterfallChart"}


def lit(o):
    return ((o or {}).get("expr", {}).get("Literal", {}) or {}).get("Value")


def load(page):
    out = []
    for f in sorted((DEF / "pages" / page / "visuals").glob("*/visual.json")):
        d = json.loads(f.read_text(encoding="utf-8")); p = d["position"]; v = d.get("visual", {})
        tt = (v.get("visualContainerObjects", {}).get("visualTooltip") or [{}])[0].get("properties", {})
        out.append({"name": d["name"], "type": v.get("visualType", ""), "z": p.get("z", 0), "hidden": d.get("isHidden", False),
                    "box": (p["x"], p["y"], p["x"] + p["width"], p["y"] + p["height"]),
                    "live": v.get("visualType") in MOUSE_TYPES or lit(tt.get("show")) == "true"})
    return out


def states(page):
    """{state name: set of hidden visual names} from the bookmarks that show and hide this page's visuals; the page as
    saved (isHidden) when no bookmark touches it."""
    out = {}
    for f in sorted((DEF / "bookmarks").glob("*.bookmark.json")):
        bm = json.loads(f.read_text(encoding="utf-8"))
        sec = bm.get("explorationState", {}).get("sections", {}).get(page)
        if sec:
            out[bm["name"]] = {n for n, c in sec.get("visualContainers", {}).items() if c.get("singleVisual", {}).get("display", {}).get("mode") == "hidden"}
    return out


pages = json.loads((DEF / "pages" / "pages.json").read_text(encoding="utf-8"))["pageOrder"]
fails, notes = 0, 0
for page in pages:
    pj = json.loads((DEF / "pages" / page / "page.json").read_text(encoding="utf-8"))
    if pj.get("type") == "Tooltip":
        continue
    vis = load(page)
    sts = states(page) or {"as saved": {v["name"] for v in vis if v["hidden"]}}
    in_bookmarks = set().union(*[set(json.loads(f.read_text(encoding="utf-8")).get("options", {}).get("targetVisualNames", [])) for f in (DEF / "bookmarks").glob("*.bookmark.json")] or [set()])
    for st, hidden in sts.items():
        shown = [v for v in vis if v["name"] not in hidden and not (v["hidden"] and v["name"] not in in_bookmarks)]
        lines = []
        for a in (v for v in shown if v["live"]):
            ax0, ay0, ax1, ay1 = a["box"]; area = (ax1 - ax0) * (ay1 - ay0)
            for c in shown:
                if c is a or c["z"] <= a["z"]:
                    continue
                cx0, cy0, cx1, cy1 = c["box"]
                w = min(ax1, cx1) - max(ax0, cx0)
                if w <= 0:
                    continue
                body = max(0, min(ay1, cy1) - max(ay0, cy0))
                strip = max(0, min(ay1, cy0) - max(ay0, cy0 - STRIP))
                if body and c["live"]:
                    lines.append(("note", f"{a['name']} lies under the live {c['name']} ({100 * w * body / area:.0f}% of it): by design?"))
                elif body:
                    lines.append(("FAIL", f"{a['name']} lies under {c['name']} ({100 * w * (body + strip) / area:.0f}% of it with the strip)"))
                elif strip and 100 * w * strip / area > 2:
                    lines.append(("FAIL", f"{a['name']} loses {100 * w * strip / area:.0f}% to the strip above {c['name']}"))
        f_ = sum(1 for k, _ in lines if k == "FAIL"); fails += f_; notes += len(lines) - f_
        print(f"{page} · {st}: {sum(1 for v in shown if v['live'])} live visuals, {f_} blinded" + ("" if not lines else ""))
        for k, l in lines:
            print(f"  {k:4} {l}")
    # cross-filter: every chart and table needs its NoFilter list
    inter = pj.get("visualInteractions", [])
    names = {v["name"] for v in vis}
    for v in vis:
        if v["type"] in SELECTABLE:
            mine = {i["target"] for i in inter if i["source"] == v["name"]}
            missing = names - mine - {v["name"]}
            if missing:
                fails += 1
                print(f"  FAIL {page}: a click in {v['name']} can filter {len(missing)} visual(s) (no interaction entry), e.g. {sorted(missing)[:3]}")
print(f"strip_check: {fails} failure(s), {notes} note(s) at a strip of {STRIP:g} page px over {REPORT.name}")
sys.exit(1 if fails else 0)
