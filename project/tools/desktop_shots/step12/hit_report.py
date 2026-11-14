"""Build step 12 of doc 23: read hit_test.js's result against the report files and name who blinds whom.

usage: python hit_report.py <hit.json> <report dir> <page id> [--all]

Containers are matched to the page's visuals by their rectangle. Listed: every visual that can be hovered or
clicked (charts, tables, slicers, buttons, and cards or text boxes that carry a tooltip or a link) and that is not the
topmost container over its whole area; and every mark (dot, column, bar, tile, button) whose centre does not reach it.
"strip" = the 20 px above another visual (its header strip); "body" = the other visual itself. --all lists
every visual, also the ones that only show text.
"""
import json
import sys
from pathlib import Path

hit = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
if "value" in hit:
    hit = hit["value"]
page = Path(sys.argv[2]) / "definition" / "pages" / sys.argv[3] / "visuals"
ALL = "--all" in sys.argv
LIVE = {"scatterChart", "lineChart", "stackedAreaChart", "clusteredColumnChart", "clusteredBarChart", "barChart", "tableEx", "slicer", "advancedSlicerVisual", "actionButton"}

vis = []
for f in page.glob("*/visual.json"):
    d = json.loads(f.read_text(encoding="utf-8")); p = d["position"]
    v = d.get("visual", {})
    txt = json.dumps(v.get("visualContainerObjects", {}))
    live = v.get("visualType") in LIVE or '"visualTooltip"' in txt or '"visualLink"' in txt
    vis.append({"name": d["name"], "rect": [round(p["x"]), round(p["y"]), round(p["width"]), round(p["height"])], "type": v.get("visualType", "group"), "live": live, "z": p.get("z", 0)})


def candidates(c):
    x, y, w, h = c["rect"]
    return [v for v in vis if abs(v["rect"][0] - x) <= 2 and abs(v["rect"][2] - w) <= 3 and abs(v["rect"][1] + v["rect"][3] - y - h) <= 3]


# Visuals stacked on one rectangle (the scatter layers) cannot be told apart by their box: the page draws them in
# z-order, so the n-th container on a rectangle is the n-th of its visuals by z.
names, seen = [], {}
for c in hit["containers"]:
    m = sorted(candidates(c), key=lambda v: v["z"])
    key = tuple(v["name"] for v in m)
    n = seen.get(key, 0); seen[key] = n + 1
    if not m:
        names.append((f"?{c['rect']}", False))
    elif len(m) > 1 and n < len(m):
        names.append((m[n]["name"], m[n]["live"]))
    else:
        names.append((m[0]["name"], m[0]["live"]))
bad = 0
print(f"{len(hit['containers'])} containers on the page, scale {hit['scale']:.3f}")
for c, (name, live) in zip(hit["containers"], names):
    if c["own"] == c["total"] or not (live or ALL):
        continue
    share = 100 * (1 - c["own"] / max(1, c["total"]))
    who = ", ".join(f"{names[int(k.split(':')[0])][0] if int(k.split(':')[0]) >= 0 else 'outside'} ({k.split(':')[1]}) {100 * n / c['total']:.0f}%"
                    for k, n in sorted(c["by"].items(), key=lambda kv: -kv[1])[:6])
    print(f"  {name:28} {c['rect']}  covered {share:4.1f}%  by {who}")
    bad += 1
AXIS = ("text.setFocusRing", "DIV.small-multiples")  # axis words and card texts: nothing to hover
marks = [m for m in hit["marks"] if not m["kind"].startswith(AXIS)]
blind = [m for m in marks if not m["ok"]]
print(f"{len(marks)} marks (dots, columns, bars, tiles, buttons), {len(blind)} do not get the mouse at their centre")
groups = {}
for m in blind:
    k = (names[m["of"]][0], m["kind"][:24], names[m["by"]][0] if m["by"] >= 0 else "outside", m["where"])
    groups.setdefault(k, []).append(m)
for (of, kind, by, where), ms in groups.items():
    eg = ", ".join(f"{m['at']}" for m in ms[:4])
    print(f"  {of:24} {len(ms):4} x {kind:24} under {by} ({where})  e.g. {eg}")
print("hit_report:", "clear" if not bad and not blind else f"{bad} live visual(s) partly covered, {len(blind)} blind mark(s)")
