"""Edit on the hand-finished report (16 Nov 2026 night, doc 38): step 3 in clay, the plans highlighted in the table only.

  python f9_step3_clay.py <.Report dir> <.SemanticModel dir>

Bjorn, 16 Nov, on doc 37 ("that doesn't seem right") and on the sketch of options: "Let's go with clay indeed and do
highlight the plans in the top left visual but do not update the bar chart below with highlights." This script edits the
saved report in place and can be run again (it sets, it does not add). What it sets:

  the model     every measure as the generator's model has it: step 3 is clay (Burnt Tangerine at 75 % on white) in the
                table's two bars, its row stands on a light clay, its status word is Burnt Tangerine.
  ch_plan_bar   the third segment clay ("not needed" stays Warm Grey).
  c_plan_t3     "Step 3 · the refresh" in Burnt Tangerine, as step 1's label is Deep Coffee.
  plan_tint_1..3   (doc 37) removed, with their bookmark states and their "no filter" entries.
  c_plan_t1.._t3_3   back on their segment's left edge, where Bjorn's save of 21:48 had them.
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model_sync import sync_measures  # noqa: E402

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy"

CLAY, WARM_GREY, BURNT = "#BC6F4A", "#8E897D", "#A63F0E"  # sketch_model.STEP3, SLATE (Warm Grey), BAD
FILLS = {"_Measures.Tranche 3 Capex": CLAY, "_Measures.Not Needed Capex": WARM_GREY}  # "not needed" stays Warm Grey: the light neutral is 1.7:1 on the card (a11y_check)
TINTS = [f"plan_tint_{k}" for k in (1, 2, 3)]
# the labels' x and width in the save of 21:48 (commit 7569ef6)
LABELS = {"c_plan_t1": (56, 275), "c_plan_t1_2": (55.713526971702926, 275),
          "c_plan_t2": (339, 366), "c_plan_t2_2": (338.7135269717029, 366), "c_plan_t2_3": (338.7135269717029, 366),
          "c_plan_t3": (713, 881), "c_plan_t3_2": (712.713526971703, 881), "c_plan_t3_3": (712.713526971703, 881)}


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def solid(hexv):
    return {"solid": {"color": lit(f"'{hexv}'")}}


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    if out.encode("utf-8") != raw[3 if bom else 0:]:
        path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


changed, added = sync_measures(MODEL)


def plan_bar(v):
    for e in v["visual"]["objects"]["dataPoint"]:
        if e.get("selector", {}).get("metadata") in FILLS:
            e["properties"]["fill"] = solid(FILLS[e["selector"]["metadata"]])


def step3_label(v):
    v["visual"]["objects"]["value"][0]["properties"]["fontColor"] = solid(BURNT)


edit(P2 / "visuals" / "ch_plan_bar" / "visual.json", plan_bar)
edit(P2 / "visuals" / "c_plan_t3" / "visual.json", step3_label)
for name, (x, w) in LABELS.items():
    def back(v, x=x, w=w):
        v["position"]["x"], v["position"]["width"] = x, w
    edit(P2 / "visuals" / name / "visual.json", back)

# ---- the grounds over the plan bar go
for n in TINTS:
    shutil.rmtree(P2 / "visuals" / n, ignore_errors=True)


def without_tints(bm):
    o = bm.get("options", {})
    if "targetVisualNames" in o:
        o["targetVisualNames"] = [n for n in o["targetVisualNames"] if n not in TINTS]
    for sec in bm["explorationState"]["sections"].values():
        for n in TINTS:
            sec.get("visualContainers", {}).pop(n, None)


def no_entries(page):
    page["visualInteractions"] = [i for i in page["visualInteractions"] if i["target"] not in TINTS and i["source"] not in TINTS]


for f in sorted((REPORT / "definition" / "bookmarks").glob("*.bookmark.json")):
    edit(f, without_tints)
edit(P2 / "page.json", no_entries)
left = [str(f.relative_to(REPORT)) for f in REPORT.rglob("*.json") if ".pbi" not in f.parts and "plan_tint_" in f.read_text(encoding="utf-8-sig")]
assert not left, f"a ground is still named in {left}"
print(f"f9_step3_clay: step 3 clay, the grounds over the plan bar gone, labels back; model: {len(changed)} set {changed}, {len(added)} added {added}")
