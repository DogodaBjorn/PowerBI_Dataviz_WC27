"""Tile pages for a high-resolution render of one report page in the throwaway copy: 16 pages of 480 x 270 (t_<row>_<col>),
each holding the page's visuals that touch its region, shifted so the region's corner is the page origin. A narrow Desktop
window shows a 480 px page at about 1.8 capture px per page px (a 1920 px page at 0.46). Plus t_cal: one Tangerine frame on
the whole page, to find the page in a capture.

usage: mk_tiles.py <copy .Report dir> [--page NAME] [--scenario Low|Expected|High] [--mast PX]
  --page      the source page folder (default p1-brand-review)
  --scenario  build step 6: page 2 follows the Scenario slicer, and a slicer only reaches its own page. The tile that holds
              sl_scenario gets the slicer with that case selected; every other tile gets the case as a page filter (the
              measures read the same SELECTEDVALUE either way). The source page's own filters are copied to every tile.
  --mast      build step 6: draw the Night header zone (0 to PX page px) as a rectangle under the tile's visuals, because a
              tile page has no background image and light text on Oat cannot be read or measured. 168 for both pages."""
import copy
import json
import os
import shutil
import sys

rep = sys.argv[1]; D = rep + "/definition/pages"
opt = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d  # noqa: E731
SRC, SCEN, MAST = opt("--page", "p1-brand-review"), opt("--scenario"), int(opt("--mast", "0"))
TW, TH = 480, 270
src = f"{D}/{SRC}/visuals"
vis = [json.load(open(f"{src}/{n}/visual.json", encoding="utf-8")) for n in sorted(os.listdir(src))]
src_filters = json.load(open(f"{D}/{SRC}/page.json", encoding="utf-8")).get("filterConfig", {}).get("filters", [])
L = lambda s: {"expr": {"Literal": {"Value": s}}}  # noqa: E731
SCEN_FILTER = {"name": "flt_tile_scenario", "field": {"Column": {"Expression": {"SourceRef": {"Entity": "Scenario"}}, "Property": "Scenario"}}, "type": "Categorical",
               "filter": {"Version": 2, "From": [{"Name": "f", "Entity": "Scenario", "Type": 0}],
                          "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "f"}}, "Property": "Scenario"}}],
                                                          "Values": [[{"Literal": {"Value": f"'{SCEN}'"}}]]}}}]}, "howCreated": "User"}


def box(name, x, y, w, h, hexv, z):
    return {"$schema": vis[0]["$schema"], "name": name, "position": {"x": x, "y": y, "z": z, "width": w, "height": h, "tabOrder": -9000},
            "visual": {"visualType": "textbox", "objects": {"general": [{"properties": {"paragraphs": [{"textRuns": [{"value": "", "textStyle": {"fontSize": "16px"}}]}]}}]},
                       "visualContainerObjects": {"background": [{"properties": {"show": L("true"), "color": {"solid": {"color": L(f"'{hexv}'")}}, "transparency": L("0D")}}],
                                                  "border": [{"properties": {"show": L("false")}}], "title": [{"properties": {"show": L("false")}}],
                                                  "padding": [{"properties": {k: L("0D") for k in ("top", "bottom", "left", "right")}}]},
                       "drillFilterOtherVisuals": False}}


def page(name, visuals, filters=None):
    pg = f"{D}/{name}"
    if os.path.exists(pg):
        shutil.rmtree(pg)
    os.makedirs(pg + "/visuals")
    pj = {"$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json", "name": name, "displayName": name,
          "displayOption": "FitToWidth", "height": TH, "width": TW,
          "objects": {"background": [{"properties": {"color": {"solid": {"color": L("'#F3F1EA'")}}, "transparency": L("0D")}}]}}
    if filters:
        pj["filterConfig"] = {"filters": filters}
    json.dump(pj, open(pg + "/page.json", "w", encoding="utf-8"), indent=2)
    for v in visuals:
        os.makedirs(f"{pg}/visuals/{v['name']}")
        json.dump(v, open(f"{pg}/visuals/{v['name']}/visual.json", "w", encoding="utf-8"), indent=2)


names = []
for r in range(4):
    for c in range(4):
        tx, ty = c * TW, r * TH
        out = []
        for v in vis:
            p = v["position"]
            if p["x"] < tx + TW and p["x"] + p["width"] > tx and p["y"] < ty + TH and p["y"] + p["height"] > ty:
                w = copy.deepcopy(v); w["position"]["x"] -= tx; w["position"]["y"] -= ty
                out.append(w)
        filters = copy.deepcopy(src_filters)
        if SCEN:
            sl = next((w for w in out if w["name"] == "sl_scenario"), None)
            if sl:
                txt = json.dumps(sl)
                assert "'Expected'" in txt
                out[out.index(sl)] = json.loads(txt.replace("'Expected'", f"'{SCEN}'"))
            else:
                filters.append(SCEN_FILTER)
        if MAST > ty:
            out.append(box("tile_mast", 0, 0, TW, min(MAST - ty, TH), "#12233D", 0))
        n = f"t_{r}_{c}"; page(n, out, filters); names.append(n)
page("t_cal", [box("cal", 0, 0, TW, TH, "#E05A22", 1)]); names.append("t_cal")
pj = json.load(open(D + "/pages.json", encoding="utf-8"))
pj["pageOrder"] = [n for n in pj["pageOrder"] if not n.startswith("t_")] + names
json.dump(pj, open(D + "/pages.json", "w", encoding="utf-8"), indent=2)
print(len(names), "tile pages of", SRC, "scenario", SCEN or "as saved")
