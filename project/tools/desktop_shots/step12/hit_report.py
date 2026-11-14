"""Build step 12 of doc 23: read hit_test.js's result against the report files and name who blinds whom.

usage: python hit_report.py <hit.json> <report dir> <page id> [--state <bookmark name>] [--all]

Containers are matched to the page's visuals by their rectangle; --state leaves out the visuals that bookmark hides
(without it the page as saved). Listed: every LIVE visual (a button, a slicer, a visual that opens a tooltip: the
definition of tools/strip_check.py) that is not the topmost container over its whole area, with who covers it:
"strip" = the 20 px above another visual (its header strip), "body" = the other visual itself; and every mark of a
live visual (dot, column, bar, tile, button) whose centre does not reach it. --all lists every visual.
Last line: "hit_report: clear" or the counts. A live visual under another live one (the scatter's layers) is not counted.
"""
import json
import sys
from pathlib import Path

hit = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
hit = hit.get("value", hit)
REPORT, PAGE = Path(sys.argv[2]), sys.argv[3]
ALL = "--all" in sys.argv
STATE = sys.argv[sys.argv.index("--state") + 1] if "--state" in sys.argv else None
MOUSE_TYPES = {"actionButton", "advancedSlicerVisual", "slicer"}

hidden = None
if STATE:
    bm = json.loads((REPORT / "definition" / "bookmarks" / f"{STATE}.bookmark.json").read_text(encoding="utf-8"))
    cons = bm["explorationState"]["sections"][PAGE]["visualContainers"]
    hidden = {n for n, c in cons.items() if c.get("singleVisual", {}).get("display", {}).get("mode") == "hidden"}
    targets = set(cons)

vis = []
for f in (REPORT / "definition" / "pages" / PAGE / "visuals").glob("*/visual.json"):
    d = json.loads(f.read_text(encoding="utf-8")); p = d["position"]; v = d.get("visual", {})
    if (hidden is not None and (d["name"] in hidden or (d.get("isHidden") and d["name"] not in targets))) or (hidden is None and d.get("isHidden")):
        continue
    tt = (v.get("visualContainerObjects", {}).get("visualTooltip") or [{}])[0].get("properties", {})
    live = v.get("visualType") in MOUSE_TYPES or tt.get("show", {}).get("expr", {}).get("Literal", {}).get("Value") == "true"
    vis.append({"name": d["name"], "rect": [round(p["x"]), round(p["y"]), round(p["width"]), round(p["height"])], "live": live, "z": p.get("z", 0)})


def candidates(c):
    x, y, w, h = c["rect"]
    return [v for v in vis if abs(v["rect"][0] - x) <= 2 and abs(v["rect"][2] - w) <= 3 and abs(v["rect"][1] + v["rect"][3] - y - h) <= 3]


# Visuals stacked on one rectangle (the scatter layers) cannot be told apart by their box: the page draws them in
# z-order, so the n-th container on a rectangle is the n-th of its visuals by z.
names, stacks = [None] * len(hit["containers"]), {}
for i, c in enumerate(hit["containers"]):
    m = sorted(candidates(c), key=lambda v: v["z"])
    stacks.setdefault(tuple(v["name"] for v in m), []).append(i)
for key, idx in stacks.items():
    m = sorted((v for v in vis if v["name"] in key), key=lambda v: v["z"])
    for n, i in enumerate(sorted(idx, key=lambda i: (hit["containers"][i].get("z", 0), i))):  # the page's own z-index, then DOM order
        names[i] = (f"?{hit['containers'][i]['rect']}", False) if not m else (m[min(n, len(m) - 1)]["name"], m[min(n, len(m) - 1)]["live"])

who = lambda j: names[j][0] if j >= 0 else "outside"
bad = 0
print(f"{len(hit['containers'])} containers on the page, scale {hit['scale']:.3f}")
for c, (name, live) in zip(hit["containers"], names):
    if not (live or ALL):
        continue
    # under the BODY of another live visual: by design (the scatter's layers); its strip is never by design
    lost = {k: n for k, n in c["by"].items() if not (int(k.split(":")[0]) >= 0 and names[int(k.split(":")[0])][1] and k.endswith(":body") and not ALL)}
    share = 100 * sum(lost.values()) / max(1, c["total"])
    if share < 2:
        continue
    by = ", ".join(f"{who(int(k.split(':')[0]))} ({k.split(':')[1]}) {100 * n / c['total']:.0f}%" for k, n in sorted(lost.items(), key=lambda kv: -kv[1])[:5])
    print(f"  {name:24} {c['rect']} loses {share:4.1f}% to {by}")
    bad += 1
AXIS = ("text.setFocusRing", "DIV.small-multiples")  # axis words and card texts: nothing to hover
marks = [m for m in hit["marks"] if not m["kind"].startswith(AXIS) and (names[m["of"]][1] or ALL)]
blind = [m for m in marks if not m["ok"] and not (m["by"] >= 0 and names[m["by"]][1] and m["where"] == "body" and not ALL)]
groups = {}
for m in blind:
    groups.setdefault((names[m["of"]][0], m["kind"][:24], who(m["by"]), m["where"]), []).append(m)
for (of, kind, by, where), ms in groups.items():
    print(f"  {of:24} {len(ms):4} x {kind:24} under {by} ({where})  e.g. " + ", ".join(str(m["at"]) for m in ms[:4]))
print("hit_report: " + (f"clear ({sum(1 for n in names if n[1])} live visuals, {len(marks)} marks)" if not bad and not blind
                        else f"{bad} live visual(s) lose 2% or more, {len(blind)} of {len(marks)} marks blind"))
