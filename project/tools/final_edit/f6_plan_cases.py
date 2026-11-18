"""Edit on the hand-finished report (16 Nov 2026, doc 34): the capital plan's cash chart reads by case.

  python f6_plan_cases.py <.Report dir> <.SemanticModel dir>

Bjorn, 16 Nov: "it's too much grey: the gridlines, the two different scenario lines and the cash positive line all the
same colour". Until now the chart had one colour for "the case in view" (Coffee Blue, 3 px) and Warm Grey for the two
other cases, on a Dusk zero line and hairline gridlines. This script edits the saved report in place and can be run
again (it sets, it does not add). What it sets:

  ch_plan_cum   each case its own colour, in view or not: Low Burnt Tangerine (the report's colour for "bad": the one
                line that ends under zero), Expected Coffee Blue, High Night. The dash stays the second signal (Low dashed,
                Expected solid, High dotted), so no reader needs the colour. The case in view is the thick line (3.5 px),
                the other two 2 px (were 1.5: a thin dotted line was hard to follow). That takes one emphasised series
                per case: one series has one colour.
                The zero line Night and 1.5 px, its name in Night, and the area under it lightly shaded: under water is a
                region, not a line to find among the gridlines.
  ch_plan_cum_e1..3, _s1..3   the end labels in the colour of their line (the Expected one in Deep Coffee, the text blue);
                semibold for the case in view, as it was.
  A Cumulative In View (Low | Expected | High)   (model, new) a case's own line while it is the case in view, blank
                otherwise. They replace Preset A Cumulative Net (sel) in this chart only.
"""
import json
import re
import sys
import uuid
from pathlib import Path

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy" / "visuals"

NIGHT, COFFEE_BLUE, DEEP_COFFEE, BURNT, TANGERINE = "#12233D", "#2589D8", "#1763A8", "#A63F0E", "#E05A22"
# case: (the line's colour, its label's colour, the dash, the two label cards)
CASES = {"Low": (BURNT, BURNT, "dashed", ("ch_plan_cum_e1", "ch_plan_cum_s1")),
         "Expected": (COFFEE_BLUE, DEEP_COFFEE, "solid", ("ch_plan_cum_e3", "ch_plan_cum_s3")),
         "High": (NIGHT, NIGHT, "dotted", ("ch_plan_cum_e2", "ch_plan_cum_s2"))}
THIN, THICK = 2, 3.5
ZERO_W, SHADE, SHADE_TRANSPARENCY = 1.5, TANGERINE, 93
NS = uuid.UUID("5d3c1d2e-7c4f-4d2a-9b1e-9a0f6f1e2c01")  # sketch_model.py's, so the lineage tags equal the generator's
FMT = "+\\$#,0,,.\\M;−\\$#,0,,.\\M;\\$0\\M"  # sketch_model.SUSDM0: whole $M


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
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


def thin(c):
    return f"A Cumulative Line ({c})"


def thick(c):
    return f"A Cumulative In View ({c})"


def proj(measure, shown):
    return {"field": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}},
            "queryRef": f"_Measures.{measure}", "nativeQueryRef": measure, "displayName": shown}


def chart(v):
    q, o = v["visual"]["query"]["queryState"], v["visual"]["objects"]
    # the three thin lines first: the value axis prints its first series' format on every tick (build step 7)
    q["Y"]["projections"] = [proj(thin(c), f"{c} case") for c in CASES] + [proj(thick(c), f"{c} case, in view") for c in CASES]
    o["dataPoint"] = [{"properties": {"fill": solid(col)}, "selector": {"metadata": f"_Measures.{fn(c)}"}} for fn in (thin, thick) for c, (col, _, _, _) in CASES.items()]
    base = next(e for e in o["lineStyles"] if "selector" not in e)
    o["lineStyles"] = [base] + [{"properties": {"strokeWidth": lit(f"{w}D"), "lineStyle": lit(f"'{dash}'")}, "selector": {"metadata": f"_Measures.{fn(c)}"}}
                                for fn, w in ((thin, THIN), (thick, THICK)) for c, (_, _, dash, _) in CASES.items()]
    zero = next(e for e in o["y1AxisReferenceLine"] if e["selector"]["id"] == "1")["properties"]
    zero.update({"lineColor": solid(NIGHT), "dataLabelColor": solid(NIGHT), "width": lit(f"{ZERO_W}D"),
                 "shadeShow": lit("true"), "shadeRegion": lit("'before'"), "shadeColor": solid(SHADE), "shadeTransparency": lit(f"{SHADE_TRANSPARENCY}D")})


def label(colour):
    def fn(v):
        v["visual"]["objects"]["value"][0]["properties"]["fontColor"] = solid(colour)
    return fn


edit(P2 / "ch_plan_cum" / "visual.json", chart)
for c, (_, text_colour, _, cards) in CASES.items():
    for n in cards:
        bound = json.loads((P2 / n / "visual.json").read_text(encoding="utf-8-sig"))
        assert f" {c} (text)" in json.dumps(bound["visual"]["query"]), f"{n} is not the {c} label"
        edit(P2 / n / "visual.json", label(text_colour))

# ---- the model: one emphasised line per case, after the three thin ones
F = MODEL / "definition" / "tables" / "_Measures.tmdl"
raw = F.read_bytes()
s = raw.decode("utf-8")
nl = "\r\n" if "\r\n" in s else "\n"
anchor = re.search(r"\tmeasure 'A Cumulative Line \(High\)' = .*?\r?\n\r?\n(?=\t)", s, re.S)
assert anchor, "A Cumulative Line (High) not found"
new = ""
for c in CASES:
    name = thick(c)
    if f"measure '{name}'" in s:
        continue
    new += nl.join([f"\t/// Capital plan chart: package A's cumulative net impact in the {c} case while {c} is the case in view, blank otherwise: "
                    "the thick line, in the case's own colour (16 Nov, doc 34). Whole $M, as the three thin lines.",
                    f"\tmeasure '{name}' = IF ( [Selected Scenario] = \"{c}\", [TT Year A ({c})] )",
                    f"\t\tformatString: {FMT}", "\t\tdisplayFolder: 15 Storytelling rebuild",
                    f"\t\tlineageTag: {uuid.uuid5(NS, 'measure.' + name)}", "", ""])
if new:
    F.write_bytes((s[:anchor.end()] + new + s[anchor.end():]).encode("utf-8"))
print(f"f6_plan_cases: three case colours, the case in view thick, the zero line Night with the area under it shaded; {new.count('measure ')} measure(s) added")
