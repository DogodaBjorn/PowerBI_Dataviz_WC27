"""Edit on the hand-finished report (16 Nov 2026 night, doc 37): the rows of step 2 and step 3 get a ground as package A's
have, and the same three grounds stand behind the labels over the $60M plan bar.

  python f8_step_tints.py <.Report dir> <.SemanticModel dir>

Bjorn, 16 Nov, on doc 36: "the way we highlight with light blue the top 3 of package A, can we also do that for step 2
and step 3, but then a lighter grade of their respective colours? And would it be possible and look ok if we have the
highlight colours on the stacked bar chart (the 60M plan) below, adding the background colour there too." This script
edits the saved report in place and can be run again (it sets, it does not add). What it sets:

  the model     Move Row Tint gives a ground to every row that is in the plan (package A light blue, step 2 a light Night,
                step 3 a light slate); Move NPV Bar Color gives the NPV bar of a step its step's colour, as the bar of
                'a year on cost' has (the light neutral bar would fade on a ground).
  plan_tint_1..3   (page 2, new) three rectangles behind the labels over the plan bar, each as wide as its segment and
                standing on it, in the ground of its rows in the table. Shown with the plan bar (hidden in the two other
                views), out of the tab order, under the labels.
  c_plan_t1.._t3_3   the labels of the three steps 10 px inside their ground (they stood on the segment's left edge).
  page.json     "no filter" from every chart to the three grounds, as every other visual of the page has.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model_sync import sync_measures  # noqa: E402

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy"

# The plan bar as Desktop draws it (measured on the page, doc 37): the segments' left and right edges, and its top.
# Capex does not follow the case, so the edges are fixed. Half a pixel inside, so no ground shows beside its segment.
SEGMENTS = {1: (52.7, 337.0), 2: (340.3, 711.6), 3: (715.8, 1603.9)}
BAR_TOP = 795.3
TINT = {1: "#EAF2FB", 2: "#DEE0E4", 3: "#E8EAEC"}  # sketch_model.TINT, STEP2_TINT, STEP3_TINT
TOP, PAD, INSET = 702, 10, 0.5
LABELS = {1: ("c_plan_t1", "c_plan_t1_2"), 2: ("c_plan_t2", "c_plan_t2_2", "c_plan_t2_3"), 3: ("c_plan_t3", "c_plan_t3_2", "c_plan_t3_3")}
NAMES = [f"plan_tint_{k}" for k in SEGMENTS]


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


# ---- the model
changed, added = sync_measures(MODEL)

# ---- the grounds over the plan bar
bar = load(P2 / "visuals" / "ch_plan_bar" / "visual.json")
card_z = load(P2 / "visuals" / "z_card_bottom" / "visual.json")["position"]["z"]
low = min(v["position"]["tabOrder"] for d in (P2 / "visuals").iterdir() if d.name not in NAMES
          for v in [load(d / "visual.json")] if "tabOrder" in v["position"])
off = {"properties": {"show": lit("false")}}
for i, (k, (x0, x1)) in enumerate(SEGMENTS.items()):
    v = {"$schema": bar["$schema"], "name": f"plan_tint_{k}",
         "position": {"x": x0 + INSET, "y": TOP, "z": card_z + 100 + i, "height": round(BAR_TOP + 1 - TOP, 1), "width": round(x1 - x0 - 2 * INSET, 1),
                      "tabOrder": low - 1000 * (i + 1)},
         "visual": {"visualType": "shape",
                    "objects": {"shape": [{"properties": {"tileShape": lit("'rectangle'")}}],
                                "fill": [{"properties": {"show": lit("true")}},
                                         {"properties": {"fillColor": {"solid": {"color": lit(f"'{TINT[k]}'")}}, "transparency": lit("0D")}, "selector": {"id": "default"}}],
                                "outline": [off], "text": [off]},
                    "visualContainerObjects": {n: [off] for n in ("title", "background", "border", "dropShadow", "visualHeader", "subTitle", "visualTooltip")}
                    | {"padding": [{"properties": {s_: lit("0D") for s_ in ("top", "bottom", "left", "right")}}]}}}
    d = P2 / "visuals" / f"plan_tint_{k}"
    d.mkdir(exist_ok=True)
    (d / "visual.json").write_text(json.dumps(v, indent=2, ensure_ascii=False), encoding="utf-8", newline="\r\n")


    def inside(v, x=x0 + PAD, w=x1 - x0 - PAD - 4):
        v["position"]["x"], v["position"]["width"] = round(x, 1), round(w, 1)


    for name in LABELS[k]:
        edit(P2 / "visuals" / name / "visual.json", inside)


def with_the_bar(bm):
    """A ground is shown where the plan bar is shown and hidden where it is hidden."""
    o = bm.get("options", {})
    if "targetVisualNames" in o:
        o["targetVisualNames"] = [n for n in o["targetVisualNames"] if n not in NAMES] + NAMES
    for sec in bm["explorationState"]["sections"].values():
        vc = sec.get("visualContainers", {})
        if "ch_plan_bar" in vc:
            for n in NAMES:
                vc[n] = {"singleVisual": {"visualType": "shape", **({"display": dict(vc["ch_plan_bar"]["singleVisual"]["display"])} if "display" in vc["ch_plan_bar"]["singleVisual"] else {})}}


for f in sorted((REPORT / "definition" / "bookmarks").glob("*.bookmark.json")):
    edit(f, with_the_bar)


def no_filter(page):
    """No chart filters a ground (strip_check.py: every source has an entry for every visual on the page)."""
    have = {(i["source"], i["target"]) for i in page["visualInteractions"]}
    for src in sorted({i["source"] for i in page["visualInteractions"]}):
        page["visualInteractions"] += [{"source": src, "target": n, "type": "NoFilter"} for n in NAMES if (src, n) not in have]


edit(P2 / "page.json", no_filter)
print(f"f8_step_tints: grounds for step 2 and step 3 in the table, three grounds over the plan bar; model: {len(changed)} set {changed}, {len(added)} added {added}")
