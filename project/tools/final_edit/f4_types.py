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
  c_f4_rows_lab_*  "Airport ●", "City ■", "Highway ▲": the row's own mark in its own colour, where the Dusk ◆ stood.
  Age Band Color   (model) the bar of the oldest hotels in card III in Burnt Tangerine, was Tangerine.
  F4 Dot Color     (model) removed: nothing binds it any more.
  sl_scenario  opens on Expected again (the save of 11:32 carried High, the case that was clicked last).
"""
import json
import re
import sys
from pathlib import Path

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P1 = REPORT / "definition" / "pages" / "p1-brand-review" / "visuals"
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy" / "visuals"

COFFEE_BLUE, WARM_GREY, TANGERINE_BRIGHT, BURNT, TANGERINE, DUSK = "#2589D8", "#8E897D", "#FF783D", "#A63F0E", "#E05A22", "#4B5466"
# location type: (colour, the scatter's marker shape, the same mark as a character, its size in the label in px)
TYPES = {"Airport": (COFFEE_BLUE, "circle", "●", 16), "City": (WARM_GREY, "square", "■", 16), "Highway": (TANGERINE_BRIGHT, "triangle", "▲", 16)}
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


def label(name, mark, colour, px):
    def fn(v):
        par = v["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]
        style = dict(par["textRuns"][0]["textStyle"])
        par["textRuns"] = [{"value": name + " ", "textStyle": dict(style, color=DUSK)},
                           {"value": mark, "textStyle": dict(style, color=colour, fontSize=f"{px}px")}]
    return fn


def scenario(v):
    v["visual"]["objects"]["general"][0]["properties"]["filter"]["filter"]["Where"][0]["Condition"]["In"]["Values"] = [[{"Literal": {"Value": "'Expected'"}}]]


edit(P1 / "ch_f4_dots" / "visual.json", dots)
edit(P1 / "ch_f4_avg" / "visual.json", avg)
for t, (colour, _, mark, px) in TYPES.items():
    edit(P1 / f"c_f4_rows_lab_{t.lower()}" / "visual.json", label(t, mark, colour, px))
edit(P2 / "sl_scenario" / "visual.json", scenario)

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
