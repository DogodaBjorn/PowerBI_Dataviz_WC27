"""Scratch pages in the throwaway copy that show the hero table without a tile seam through its header:
h_a: table at (-300, 20)   h_b: table at (-300, 22)   h_c: table at (-300, -110), so its last rows and its end show.
Each page carries a Tangerine marker 4 px high at a known y (y 4..8) to anchor the measurement."""
import copy
import json
import os
import shutil
import sys

rep = sys.argv[1]; D = rep + "/definition/pages"
src = json.load(open(f"{D}/p2-investment-strategy/visuals/tbl_hero/visual.json", encoding="utf-8"))
pfilters = json.load(open(f"{D}/p2-investment-strategy/page.json", encoding="utf-8")).get("filterConfig", {}).get("filters", [])
L = lambda s: {"expr": {"Literal": {"Value": s}}}  # noqa: E731


def box(name, x, y, w, h, hexv):
    return {"$schema": src["$schema"], "name": name, "position": {"x": x, "y": y, "z": 5, "width": w, "height": h, "tabOrder": -9000},
            "visual": {"visualType": "textbox", "objects": {"general": [{"properties": {"paragraphs": [{"textRuns": [{"value": "", "textStyle": {"fontSize": "16px"}}]}]}}]},
                       "visualContainerObjects": {"background": [{"properties": {"show": L("true"), "color": {"solid": {"color": L(f"'{hexv}'")}}, "transparency": L("0D")}}],
                                                  "border": [{"properties": {"show": L("false")}}], "title": [{"properties": {"show": L("false")}}],
                                                  "padding": [{"properties": {k: L("0D") for k in ("top", "bottom", "left", "right")}}]},
                       "drillFilterOtherVisuals": False}}


names = []
for name, x, y in (("h_a", -300, 20), ("h_b", -300, 22), ("h_c", -300, -110), ("h_d", -560, 20)):
    pg = f"{D}/{name}"
    if os.path.exists(pg):
        shutil.rmtree(pg)
    os.makedirs(pg + "/visuals")
    pj = {"$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json", "name": name, "displayName": name,
          "displayOption": "FitToWidth", "height": 270, "width": 480,
          "objects": {"background": [{"properties": {"color": {"solid": {"color": L("'#FFFFFF'")}}, "transparency": L("0D")}}]},
          "filterConfig": {"filters": copy.deepcopy(pfilters)}}
    json.dump(pj, open(pg + "/page.json", "w", encoding="utf-8"), indent=2)
    v = copy.deepcopy(src); v["position"]["x"], v["position"]["y"] = x, y
    v.pop("isHidden", None)
    for w in (v, box("mark", 0, 4, 40, 4, "#E05A22")):
        os.makedirs(f"{pg}/visuals/{w['name']}")
        json.dump(w, open(f"{pg}/visuals/{w['name']}/visual.json", "w", encoding="utf-8"), indent=2)
    names.append(name)
pj = json.load(open(D + "/pages.json", encoding="utf-8"))
pj["pageOrder"] = [n for n in pj["pageOrder"] if n not in names] + names
json.dump(pj, open(D + "/pages.json", "w", encoding="utf-8"), indent=2)
print("pages", names, "table height", src["position"]["height"])
