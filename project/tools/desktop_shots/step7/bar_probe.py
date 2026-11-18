"""Scratch pages in the throwaway copy that show the plan bar and the plan chart without a tile seam through them:
b_a: ch_plan_bar moved so its slot top (788) is at y 100; b_b: ch_plan_cum moved so page y 828 is at y 60 and page x 792 at x 20.
A Tangerine marker at y 4..8 anchors the measurement. usage: bar_probe.py <copy .Report> [Scenario]"""
import copy
import json
import os
import shutil
import sys

rep = sys.argv[1]; D = rep + "/definition/pages"
SRC = f"{D}/p2-investment-strategy"
pfilters = json.load(open(f"{SRC}/page.json", encoding="utf-8")).get("filterConfig", {}).get("filters", [])
L = lambda s: {"expr": {"Literal": {"Value": s}}}  # noqa: E731
load = lambda n: json.load(open(f"{SRC}/visuals/{n}/visual.json", encoding="utf-8"))  # noqa: E731
schema = load("ch_plan_bar")["$schema"]


def box(name, x, y, w, h, hexv):
    return {"$schema": schema, "name": name, "position": {"x": x, "y": y, "z": 5, "width": w, "height": h, "tabOrder": -9000},
            "visual": {"visualType": "textbox", "objects": {"general": [{"properties": {"paragraphs": [{"textRuns": [{"value": "", "textStyle": {"fontSize": "16px"}}]}]}}]},
                       "visualContainerObjects": {"background": [{"properties": {"show": L("true"), "color": {"solid": {"color": L(f"'{hexv}'")}}, "transparency": L("0D")}}],
                                                  "border": [{"properties": {"show": L("false")}}], "title": [{"properties": {"show": L("false")}}],
                                                  "padding": [{"properties": {k: L("0D") for k in ("top", "bottom", "left", "right")}}]},
                       "drillFilterOtherVisuals": False}}


names = []
for name, vis, dx, dy in (("b_a", "ch_plan_bar", -40, 100 - 788), ("b_b", "ch_plan_cum", 20 - 792, 60 - 828)):
    pg = f"{D}/{name}"
    if os.path.exists(pg):
        shutil.rmtree(pg)
    os.makedirs(pg + "/visuals")
    pj = {"$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json", "name": name, "displayName": name,
          "displayOption": "FitToWidth", "height": 270, "width": 480,
          "objects": {"background": [{"properties": {"color": {"solid": {"color": L("'#FFFFFF'")}}, "transparency": L("0D")}}]},
          "filterConfig": {"filters": copy.deepcopy(pfilters)}}
    json.dump(pj, open(pg + "/page.json", "w", encoding="utf-8"), indent=2)
    v = load(vis); v["position"]["x"] += dx; v["position"]["y"] += dy
    v.pop("isHidden", None)
    for w in (v, box("mark", 0, 4, 40, 4, "#E05A22")):
        os.makedirs(f"{pg}/visuals/{w['name']}")
        json.dump(w, open(f"{pg}/visuals/{w['name']}/visual.json", "w", encoding="utf-8"), indent=2)
    names.append(name)
pj = json.load(open(D + "/pages.json", encoding="utf-8"))
pj["pageOrder"] = [n for n in pj["pageOrder"] if n not in names] + names
json.dump(pj, open(D + "/pages.json", "w", encoding="utf-8"), indent=2)
print("pages", names)
