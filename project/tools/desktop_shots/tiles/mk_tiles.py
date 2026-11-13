"""Tile pages for a high-resolution render of P1 in the throwaway copy: 16 pages of 480 x 270 (t_<row>_<col>), each holding
the P1 visuals that touch its region, shifted so the region's corner is the page origin. A narrow Desktop window shows a
480 px page at about 1.8 capture px per page px (a 1920 px page at 0.46). Plus t_cal: one Tangerine frame on the whole
page, to find the page in a capture. usage: mk_tiles.py <copy .Report dir> [rows cols]"""
import json, os, shutil, sys, copy
rep = sys.argv[1]; D = rep + "/definition/pages"
TW, TH = 480, 270
src = D + "/p1-brand-review/visuals"
vis = [json.load(open(f"{src}/{n}/visual.json", encoding="utf-8")) for n in sorted(os.listdir(src))]
L = lambda s: {"expr": {"Literal": {"Value": s}}}
def page(name, visuals):
    pg = f"{D}/{name}"
    if os.path.exists(pg): shutil.rmtree(pg)
    os.makedirs(pg + "/visuals")
    json.dump({"$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json", "name": name, "displayName": name,
               "displayOption": "FitToWidth", "height": TH, "width": TW,
               "objects": {"background": [{"properties": {"color": {"solid": {"color": L("'#F3F1EA'")}}, "transparency": L("0D")}}]}},
              open(pg + "/page.json", "w", encoding="utf-8"), indent=2)
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
        n = f"t_{r}_{c}"; page(n, out); names.append(n)
cal = {"$schema": vis[0]["$schema"], "name": "cal", "position": {"x": 0, "y": 0, "z": 1, "width": TW, "height": TH, "tabOrder": 0},
       "visual": {"visualType": "textbox", "objects": {"general": [{"properties": {"paragraphs": [{"textRuns": [{"value": "", "textStyle": {"fontSize": "16px"}}]}]}}]},
                  "visualContainerObjects": {"background": [{"properties": {"show": L("true"), "color": {"solid": {"color": L("'#E05A22'")}}, "transparency": L("0D")}}],
                                             "border": [{"properties": {"show": L("false")}}], "title": [{"properties": {"show": L("false")}}],
                                             "padding": [{"properties": {k: L("0D") for k in ("top", "bottom", "left", "right")}}]},
                  "drillFilterOtherVisuals": False}}
page("t_cal", [cal]); names.append("t_cal")
pj = json.load(open(D + "/pages.json", encoding="utf-8"))
pj["pageOrder"] = [n for n in pj["pageOrder"] if not n.startswith("t_")] + names
json.dump(pj, open(D + "/pages.json", "w", encoding="utf-8"), indent=2)
print(len(names), "tile pages")
