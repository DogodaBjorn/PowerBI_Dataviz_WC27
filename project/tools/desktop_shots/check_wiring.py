"""Static wiring check of the focus swap in the committed report (not the review copy)."""
import json
from pathlib import Path

D = Path(r"E:\PowerBI_Dataviz_WC27\project\pbip\GoodnightInn-opzet.Report\definition")
P2 = D / "pages" / "p2-investment-strategy" / "visuals"
rd = lambda p: json.loads(p.read_text(encoding="utf-8"))
vis = {p.name: rd(p / "visual.json") for p in P2.iterdir()}
names = set(json.dumps(i) for i in rd(D / "bookmarks" / "bookmarks.json")["items"])
bms = {n: rd(D / "bookmarks" / f"{n}.bookmark.json") for n in ("bm_p2_shortlist", "bm_p2_plan")}
res = []


def check(label, ok, detail=""):
    res.append(ok)
    print(("PASS " if ok else "FAIL ") + label + (f"  ({detail})" if detail else ""))


for btn, target in (("btn_open_plan", "bm_p2_plan"), ("btn_back", "bm_p2_shortlist")):
    link = vis[btn]["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]
    bm = link["bookmark"]["expr"]["Literal"]["Value"].strip("'")
    check(f"{btn} -> {target}", bm == target and link["type"]["expr"]["Literal"]["Value"] == "'Bookmark'", bm)
    check(f"{target} registered in bookmarks.json", any(target in n for n in names))

hidden_in = {}
for n, bm in bms.items():
    o = bm["options"]
    check(f"{n}: selected visuals only, data off, page off",
          o.get("applyOnlyToTargetVisuals") is True and o.get("suppressData") is True and o.get("suppressActiveSection") is True, str(o)[:120])
    tv = set(o["targetVisualNames"])
    check(f"{n}: slicers and scatter outside the targets", not tv & {"sl_package", "sl_scenario", "sl_view", "hero_packages", "hero_named"})
    check(f"{n}: every target exists on P2", tv <= set(vis), str(sorted(tv - set(vis))))
    vc = bm["explorationState"]["sections"]["p2-investment-strategy"]["visualContainers"]
    hidden_in[n] = {v for v, c in vc.items() if c.get("singleVisual", {}).get("display", {}).get("mode") == "hidden"}
    shown = tv - hidden_in[n]
    check(f"{n}: exactly one button shown", len(shown & {"btn_open_plan", "btn_back"}) == 1, str(sorted(shown & {"btn_open_plan", "btn_back"})))

tv = set(bms["bm_p2_plan"]["options"]["targetVisualNames"])
check("same target set in both bookmarks", tv == set(bms["bm_p2_shortlist"]["options"]["targetVisualNames"]))
check("each target hidden in exactly one bookmark", all((v in hidden_in["bm_p2_plan"]) != (v in hidden_in["bm_p2_shortlist"]) for v in tv))
file_hidden = {n for n, v in vis.items() if v.get("isHidden")}
check("file opens in the shortlist state (isHidden == shortlist bookmark)", file_hidden == hidden_in["bm_p2_shortlist"],
      f"only in file: {sorted(file_hidden - hidden_in['bm_p2_shortlist'])}, only in bookmark: {sorted(hidden_in['bm_p2_shortlist'] - file_hidden)}")
# overlap: two visuals shown in the same state must not overlap
pos = {n: v["position"] for n, v in vis.items()}
for st, hid in hidden_in.items():
    shown = [n for n in tv if n not in hid]
    clashes = []
    for i, a in enumerate(shown):
        for b in shown[i + 1:]:
            A, B = pos[a], pos[b]
            if A["x"] < B["x"] + B["width"] and B["x"] < A["x"] + A["width"] and A["y"] < B["y"] + B["height"] and B["y"] < A["y"] + A["height"]:
                clashes.append(f"{a}/{b}")
    check(f"{st}: no overlapping visuals in the state", not clashes, ", ".join(clashes))
print(f"{sum(res)}/{len(res)} passed")
