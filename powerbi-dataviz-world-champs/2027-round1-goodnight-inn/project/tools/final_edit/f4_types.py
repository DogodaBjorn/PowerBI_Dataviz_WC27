"""The last edit on the hand-finished report (16 Nov 2026, doc 32): card IV's hotels by location type, card III's bar.

  python f4_types.py <.Report dir> <.SemanticModel dir>

Since Bjorn's Desktop save of 16 Nov 11:32 the report is no longer what opzet_report.py writes: he moved visuals, took
two out and reworded the link lines. This script edits that saved report in place, and can be run again (it sets, it
does not add). What it sets:

  ch_f4_dots   the 50 hotels by location type (Hotels[LocationType] as the series): Airport a Coffee Blue circle, City a
               Warm Grey square, Highway a triangle in the logo's bright Tangerine. Was: Night for the seven fullest,
               Warm Grey for the rest, all circles.
  ch_f4_avg    its three average diamonds are no longer drawn (markers 100 % transparent): the row's label carries the
               average as a number. The layer stays for the gridlines and the 90 % line.
  c_f4_rows_lab_*  the row's name alone ("Airport"); the Dusk ◆ behind it is gone.
  c_f4_rows_mark_* new: the row's own mark before its name, a shape visual of 10 x 10 px (oval, rectangle, triangle) in the
               row's colour: the same shape and colour as its hotels in the plot, whatever font the reader has.
  c_f4_rows*   the three values stand one space behind their name (they stood behind the ◆).
  Age Band Color   (model) the bar of the oldest hotels in card III in Burnt Tangerine, was Tangerine.
  F4 Dot Color     (model) removed: nothing binds it any more.
  sl_scenario  opens on Expected again (the save of 11:32 carried High, the case that was clicked last).
  lnk_f1..3    their alt text says what the line shows ("Investment Option: ..."; it still read "Page 2: ...").
  ch_f4_dots   one layer above the title's box, which its top now lies under (the top row of hotels keeps its tooltip).
  page 1       "no filter" entries from every chart to the three new marks.
  bookmarks    the two visuals Bjorn took out in Desktop no longer stand in the three bookmarks' target lists.
"""
import json
import re
import sys
from pathlib import Path

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P1 = REPORT / "definition" / "pages" / "p1-brand-review" / "visuals"
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy" / "visuals"

COFFEE_BLUE, WARM_GREY, TANGERINE_BRIGHT, BURNT, TANGERINE, DUSK = "#2589D8", "#8E897D", "#FF783D", "#A63F0E", "#E05A22", "#4B5466"
# location type: (colour, the scatter's marker shape, the same shape as a shape visual, where the value starts after the name in px)
TYPES = {"Airport": (COFFEE_BLUE, "circle", "oval", 54), "City": (WARM_GREY, "square", "rectangle", 31), "Highway": (TANGERINE_BRIGHT, "triangle", "triangleIsoc", 66)}
MARK, MARK_GAP, MARK_DY, VALUE_GAP = 10, 6, 8, 5  # the mark's side, its distance to the name, its top under the row's top, the space before the value
MARKER_SIZE = -5  # the scatter's size multiplier (was -10): a square and a triangle need a little more than a dot to read as one


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def solid(hexv):
    return {"solid": {"color": lit(f"'{hexv}'")}}


def series(value):
    return {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "Hotels"}}, "Property": "LocationType"}},
                                                 "Right": {"Literal": {"Value": f"'{value}'"}}}}}]}


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


def dots(v):
    q, o = v["visual"]["query"]["queryState"], v["visual"]["objects"]
    q["Series"] = {"projections": [{"field": {"Column": {"Expression": {"SourceRef": {"Entity": "Hotels"}}, "Property": "LocationType"}},
                                    "queryRef": "Hotels.LocationType", "nativeQueryRef": "LocationType", "displayName": "Location type"}]}
    o["dataPoint"] = [{"properties": {"fill": solid(c)}, "selector": series(t)} for t, (c, _, _, _) in TYPES.items()]
    base = next(b_ for b_ in o["bubbles"] if "selector" not in b_)
    base["properties"]["bubbleSize"] = lit(f"{MARKER_SIZE}L")
    base["properties"]["showSeries"] = lit("true")
    o["bubbles"] = [base] + [{"properties": {"markerShape": lit(f"'{shape}'")}, "selector": series(t)} for t, (_, shape, _, _) in TYPES.items()]


def avg(v):
    v["visual"]["objects"]["markers"][0]["properties"]["transparency"] = lit("100D")


def label(name, pos):
    def fn(v):
        par = v["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]
        par["textRuns"] = [{"value": name, "textStyle": dict(par["textRuns"][0]["textStyle"])}]
        pos.update(v["position"])
    return fn


def value(pos, dx):
    def fn(v):
        v["position"]["x"] = pos["x"] + dx + VALUE_GAP
    return fn


def mark(name, pos, shape, colour, i):
    off = {"properties": {"show": lit("false")}}
    return {"$schema": SCHEMA, "name": name,
            "position": {"x": pos["x"] - MARK - MARK_GAP, "y": pos["y"] + MARK_DY, "z": pos["z"] + 500, "height": MARK, "width": MARK, "tabOrder": -27001 - i},
            "visual": {"visualType": "shape",
                       # tried in Desktop 2.159: the shape is taken without a selector; with {"id": "default"} every mark stays a rectangle
                       "objects": {"shape": [{"properties": {"tileShape": lit(f"'{shape}'")}}],
                                   "fill": [{"properties": {"show": lit("true")}}, {"properties": {"fillColor": solid(colour), "transparency": lit("0D")}, "selector": {"id": "default"}}],
                                   "outline": [off], "text": [off]},
                       "visualContainerObjects": {k: [off] for k in ("title", "background", "border", "dropShadow", "visualHeader", "subTitle", "visualTooltip")}
                       | {"padding": [{"properties": {s_: lit("0D") for s_ in ("top", "bottom", "left", "right")}}]}}}


def scenario(v):
    v["visual"]["objects"]["general"][0]["properties"]["filter"]["filter"]["Where"][0]["Condition"]["In"]["Values"] = [[{"Literal": {"Value": "'Expected'"}}]]


edit(P1 / "ch_f4_dots" / "visual.json", dots)
edit(P1 / "ch_f4_avg" / "visual.json", avg)
SCHEMA = json.loads((P1 / "ch_f4_dots" / "visual.json").read_text(encoding="utf-8-sig"))["$schema"]
for i, (t, (colour, _, shape, dx)) in enumerate(TYPES.items()):
    key, pos = t.lower(), {}
    edit(P1 / f"c_f4_rows_lab_{key}" / "visual.json", label(t, pos))
    edit(P1 / ("c_f4_rows" if i == 0 else f"c_f4_rows_{key}") / "visual.json", value(pos, dx))
    d = P1 / f"c_f4_rows_mark_{key}"
    d.mkdir(exist_ok=True)
    (d / "visual.json").write_text(json.dumps(mark(d.name, pos, shape, colour, i), indent=2, ensure_ascii=False), encoding="utf-8", newline=chr(13) + chr(10))
edit(P2 / "sl_scenario" / "visual.json", scenario)


def alt_is_text(v):
    """The three typed link lines were reworded in Desktop ("Investment Option: ..."); their alt text still read "Page 2: ..."."""
    shown = "".join(r["value"] for r in v["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]["textRuns"])
    v["visual"]["visualContainerObjects"]["general"][0]["properties"]["altText"] = lit("'" + shown.replace("'", "''") + "'")


for n in ("lnk_f1", "lnk_f2", "lnk_f3"):
    edit(P1 / n / "visual.json", alt_is_text)


def above(name):
    """The hotels must stay the top layer where they lie: Bjorn moved the plot 12 px up, under the title's box (1640 px wide,
    its words end before the plot), and a box on top takes the mouse, so the top row of hotels would lose its tooltip."""
    top = json.loads((P1 / name / "visual.json").read_text(encoding="utf-8-sig"))["position"]["z"]

    def fn(v):
        v["position"]["z"] = top + 500
    return fn


edit(P1 / "ch_f4_dots" / "visual.json", above("c_f4_title"))
edit(P1 / "tag_f4" / "visual.json", above("ch_f4_dots"))  # the "Hover a hotel" chip stays above the plot, as it was: a click in the plot paints a band in its header strip


def no_filter(page):
    """A click in a chart must not filter the three new marks either (strip_check: every pair has its entry)."""
    marks = [f"c_f4_rows_mark_{t.lower()}" for t in TYPES]
    have = {(i["source"], i["target"]) for i in page["visualInteractions"]}
    for src in sorted({i["source"] for i in page["visualInteractions"]}):
        page["visualInteractions"] += [{"source": src, "target": m_, "type": "NoFilter"} for m_ in marks if (src, m_) not in have]


edit(P1.parent / "page.json", no_filter)


def live_targets(bm):
    """Bjorn took c_rec_lines and c_ledger_caption out in Desktop; the three bookmarks still named them as targets."""
    here = {d.name for pg in (REPORT / "definition" / "pages").iterdir() if (pg / "visuals").is_dir() for d in (pg / "visuals").iterdir()}
    o = bm.get("options", {})
    if "targetVisualNames" in o:
        o["targetVisualNames"] = [n for n in o["targetVisualNames"] if n in here]


for f in sorted((REPORT / "definition" / "bookmarks").glob("*.bookmark.json")):
    edit(f, live_targets)


# the model: one colour, one measure out
F = MODEL / "definition" / "tables" / "_Measures.tmdl"
raw = F.read_bytes()
s = raw.decode("utf-8")
nl = "\r\n" if "\r\n" in s else "\n"
age = re.search(r"\tmeasure 'Age Band Color' = [^\r\n]*", s)
assert age, "Age Band Color not found"
line = age.group(0).replace(f'"{TANGERINE}"', f'"{BURNT}"')
assert f'"{BURNT}"' in line, line
s = s[:age.start()] + line + s[age.end():]
s = s.replace("\t/// Tangerine for the oldest band (a risk signal: the only negative NPS)", "\t/// Burnt Tangerine for the oldest band (a risk signal: the only negative NPS)")
m = re.search(r"(?:\t///[^\r\n]*\r?\n)*\tmeasure 'F4 Dot Color' = .*?\r?\n\r?\n(?=\t)", s, re.S)
if m:
    s = s[:m.start()] + s[m.end():]
assert "F4 Dot Color" not in s
F.write_bytes(s.encode("utf-8"))
print("f4_types: card IV by location type, card III's bar Burnt Tangerine, Scenario on Expected")
