"""Step 1 spikes (doc 23): build a throwaway copy of the project with one scratch page.

Usage: python spike_prep.py <project pbip dir> <destination dir>

Nothing in the project is touched: the Report and the model (with its data cache) are copied, spike measures are
appended to the COPY's _Measures.tmdl and a page 'spike' is added to the COPY's report.
Property names come from `powerbi-report-author formatting ...` (Microsoft's catalog), not from memory.
"""
import copy
import json
import re
import shutil
import sys
from pathlib import Path

SRC = Path(sys.argv[1])
DST = Path(sys.argv[2])
SRC_REPORT = "GoodnightInn-opzet.Report"
REPORT = "SPIKE-throwaway.Report"  # same stem as the .pbip, or `powerbi-desktop reload` finds no report folder
MODEL = "PillowKey.SemanticModel"
SCHEMA_VC = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.11.0/schema.json"
FONT = "'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"
FONT_SB = "'''Segoe UI Semibold'', wf_segoe-ui_semibold, helvetica, arial, sans-serif'"
NIGHT, SLATE, RULE, TANGERINE, BLUE, GREY = "#12233D", "#4B5466", "#E3DFD3", "#E05A22", "#2589D8", "#8E897D"

REPORT_ONLY = "--report-only" in sys.argv  # rewrite the scratch page only (Desktop is open: then `powerbi-desktop reload`)
if not REPORT_ONLY:
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    shutil.copytree(SRC / SRC_REPORT, DST / REPORT)
    shutil.copytree(SRC / MODEL, DST / MODEL)
    pbip = (SRC / "GoodnightInn-opzet.pbip").read_text(encoding="utf-8").replace(SRC_REPORT, REPORT)
    (DST / "SPIKE-throwaway.pbip").write_text(pbip, encoding="utf-8")

# ---------------------------------------------------------------- model: spike measures (copy only)
MINUS = "UNICHAR ( 8722 )"
WJ = "UNICHAR ( 8288 )"
def three(text_expr):
    """Format string with the same literal in all three sections, so a negative value gets no extra sign."""
    return ('VAR t = ' + text_expr + ' RETURN """" & t & """;""" & t & """;""" & t & """"')


NPS_T = '( VAR v = [NPS 2025 (signed)] RETURN IF ( v < 0, ' + MINUS + ', "+" ) & FORMAT ( ABS ( v ), "0.0", "en-US" ) )'
NPV_T = ('( VAR v = ROUND ( [NPV @ 8%] / 100000, 0 ) / 10 RETURN IF ( v = 0, "$0.0M", IF ( v < 0, ' + MINUS + ', "+" ) & ' + WJ
         + ' & "$" & FORMAT ( ABS ( v ), "0.0", "en-US" ) & "M" ) )')
TOK = MINUS + " & " + WJ + ' & "$0.6M "'
TOK_NJ = MINUS + ' & "$0.6M "'
measures = [
    ("S1 NPS (label-safe)", "[NPS 2025 (signed)]", three(NPS_T)),
    ("S1 NPS (one section)", "[NPS 2025 (signed)]", '"""" & ' + NPS_T + ' & """"'),
    ("S1 NPV (label-safe)", "[NPV @ 8%]", three(NPV_T)),
    ("S1 NPV (one section)", "[NPV @ 8%]", '"""" & ' + NPV_T + ' & """"'),
    ("S1 Minus 0.6M (label-safe)", "-600000", three("( " + MINUS + " & " + WJ + ' & "$0.6M" )')),
    ("S1 Zero (label-safe)", "0", three('"$0.0M"')),
    ("S1 Tokens (text)", "REPT ( " + TOK + ", 14 )", None),
    ("S1 Tokens no joiner (text)", "REPT ( " + TOK_NJ + ", 14 )", None),
    ("S5 Commission Take GI", "[Trend Margin before GI] - [Trend Margin after GI]", None),
    ("S7 Cell (text)", 'VAR n = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) RETURN IF ( ISBLANK ( n ), BLANK (), '
     '"First line " & n & UNICHAR ( 10 ) & "Second line" )', None),
    ("S7 Card LF (text)", '"LF 10: first line" & UNICHAR ( 10 ) & "second line"', None),
    ("S7 Card CRLF (text)", '"CRLF 13+10: first line" & UNICHAR ( 13 ) & UNICHAR ( 10 ) & "second line"', None),
    ("S7 Card LS (text)", '"LS 8232: first line" & UNICHAR ( 8232 ) & "second line"', None),
    ("S7 Card PS (text)", '"PS 8233: first line" & UNICHAR ( 8233 ) & "second line"', None),
    ("S8 Definitions (text)", 'UNICHAR ( 9432 ) & " Definitions"', None),
]
lines = []
for name, expr, fmt_def in measures:
    lines.append(f"\tmeasure '{name}' = {expr}")
    lines.append("\t\tdisplayFolder: 99 Spike")
    if fmt_def:
        # TMDL: formatStringDefinition is a child object, so it comes AFTER the measure's own properties
        # (Desktop: "Invalid indentation" on the property that followed it). Backtick block = verbatim text.
        lines.append("")
        lines.append("\t\tformatStringDefinition = ```")
        lines.append(f"\t\t\t\t{fmt_def}")
        lines.append("\t\t\t\t```")
    lines.append("")
block = "\r\n".join(lines) + "\r\n"
tm = DST / MODEL / "definition" / "tables" / "_Measures.tmdl"
text = tm.read_bytes().decode("utf-8")
m = re.search(r"\r\n\tcolumn ", text)
assert m, "no column block found in _Measures.tmdl"
text = text[: m.start() + 2] + block + text[m.start() + 2:]
if not REPORT_ONLY:
    tm.write_bytes(text.encode("utf-8"))


# ---------------------------------------------------------------- report helpers
def lit(v):
    return {"expr": {"Literal": {"Value": v}}}


def col(hex_):
    return {"solid": {"color": lit(f"'{hex_}'")}}


def meas(name):
    return {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": name}}


def proj_m(name, display=None):
    p = {"field": meas(name), "queryRef": f"_Measures.{name}", "nativeQueryRef": name}
    if display:
        p["displayName"] = display
    return p


def proj_c(entity, column, display=None):
    p = {"field": {"Column": {"Expression": {"SourceRef": {"Entity": entity}}, "Property": column}},
         "queryRef": f"{entity}.{column}", "nativeQueryRef": column}
    if display:
        p["displayName"] = display
    return p


def vco(header=False, background=None, border=None, radius=None):
    o = {
        "title": [{"properties": {"show": lit("false")}}],
        "background": [{"properties": {"show": lit("false")}}],
        "border": [{"properties": {"show": lit("false")}}],
        "dropShadow": [{"properties": {"show": lit("false")}}],
        "visualHeader": [{"properties": {"show": lit("true" if header else "false")}}],
        "subTitle": [{"properties": {"show": lit("false")}}],
        "padding": [{"properties": {k: lit("0D") for k in ("top", "bottom", "left", "right")}}],
        "visualTooltip": [{"properties": {"show": lit("false")}}],
    }
    if background:
        o["background"] = [{"properties": {"show": lit("true"), "color": col(background), "transparency": lit("0D")}}]
    if border:
        props = {"show": lit("true"), "color": col(border), "width": lit("1D")}
        if radius is not None:
            props["radius"] = lit(f"{radius}D")
        o["border"] = [{"properties": props}]
    return o


PAGE = DST / REPORT / "definition" / "pages" / "spike"
P1 = DST / REPORT / "definition" / "pages" / "p1-brand-review" / "visuals"
z = [1000]


def write(name, x, y, w, h, visual, filters=None):
    z[0] += 1000
    d = {"$schema": SCHEMA_VC, "name": name,
         "position": {"x": x, "y": y, "z": z[0], "width": w, "height": h, "tabOrder": z[0]},
         "visual": visual}
    if filters:
        d["filterConfig"] = {"filters": filters}
    p = PAGE / "visuals" / name
    p.mkdir(parents=True, exist_ok=True)
    (p / "visual.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def textbox(runs, background=None, border=None, radius=None, align="left"):
    return {"visualType": "textbox",
            "objects": {"general": [{"properties": {"paragraphs": [{
                "textRuns": [{"value": t, "textStyle": {
                    "fontFamily": "'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif",
                    "fontSize": size, "color": c}} for t, c, size in runs],
                "horizontalTextAlignment": align}]}}]},
            "visualContainerObjects": vco(background=background, border=border, radius=radius),
            "drillFilterOtherVisuals": False}


def note(name, x, y, w, text, h=24):
    write(name, x, y, w, h, textbox([(text, SLATE, "16px")]))


def card(measure, color=NIGHT, wrap=True, background=None, border=None, radius=None, align="left"):
    src = json.loads((P1 / "c_f1_note" / "visual.json").read_text(encoding="utf-8"))["visual"]
    v = copy.deepcopy(src)
    v["query"]["queryState"]["Data"]["projections"] = [proj_m(measure)]
    val = v["objects"]["value"][0]["properties"]
    val["fontColor"] = col(color)
    val["textWrap"] = lit("true" if wrap else "false")
    val["horizontalAlignment"] = lit(f"'{align}'")
    v["visualContainerObjects"] = vco(background=background, border=border, radius=radius)
    v["visualContainerObjects"]["general"] = [{"properties": {"altText": {"expr": meas(measure)}}}]
    return v


# ---------------------------------------------------------------- the page
if PAGE.exists():
    shutil.rmtree(PAGE)
PAGE.mkdir(parents=True)
(PAGE / "page.json").write_text(json.dumps({
    "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json",
    "name": "spike", "displayName": "SPIKE (throwaway)", "displayOption": "FitToPage", "height": 1080, "width": 1920,
    "objects": {"background": [{"properties": {"color": col("#FFFFFF"), "transparency": lit("0D")}}]},
}, indent=2) + "\n", encoding="utf-8")
pj = DST / REPORT / "definition" / "pages" / "pages.json"
pages = json.loads(pj.read_text(encoding="utf-8"))
if "spike" not in pages["pageOrder"]:
    pages["pageOrder"].insert(0, "spike")
pages["activePageName"] = "spike"
pj.write_text(json.dumps(pages, indent=2) + "\n", encoding="utf-8")

# ---- S-1 (left column) -------------------------------------------------------
note("n_s1", 40, 24, 600, "S-1 · today (comma) · one-section format · three-section format")
f3 = json.loads((P1 / "ch_f3_age" / "visual.json").read_text(encoding="utf-8"))
f3_filters = f3["filterConfig"]["filters"]
gi = [f for f in f3_filters if f["name"].startswith("flt_gi")]
for i, (nm, ms) in enumerate([("s1_f3_today", "NPS 2025 (signed)"), ("s1_f3_one", "S1 NPS (one section)"),
                              ("s1_f3_three", "S1 NPS (label-safe)")]):
    v = copy.deepcopy(f3["visual"])
    v["query"]["queryState"]["Y"]["projections"] = [proj_m(ms, "NPS 2025")]
    v["visualContainerObjects"] = vco(header=True)
    write(nm, 40 + i * 200, 56, 192, 232, v, f3_filters)


def bars(ms, vtype="clusteredBarChart", cat=("InvestmentProjects", "ProjectID", "Initiative")):
    v = copy.deepcopy(f3["visual"])
    v["visualType"] = vtype
    v["query"] = {"queryState": {"Category": {"projections": [proj_c(*cat)]},
                                 "Y": {"projections": [proj_m(ms, "NPV through 2032")]}}}
    v["objects"] = {k: x for k, x in v["objects"].items() if k in ("categoryAxis", "valueAxis", "labels", "legend", "general")}
    v["objects"]["dataPoint"] = [{"properties": {"fill": col(BLUE)}}]
    v["visualContainerObjects"] = vco(header=True)
    return v


note("n_s1m", 40, 296, 600, "Money by initiative: one-section (left), three-section (right)")
write("s1_bar_one", 40, 328, 296, 300, bars("S1 NPV (one section)"), gi)
write("s1_bar_three", 344, 328, 296, 300, bars("S1 NPV (label-safe)"), gi)
note("n_s1f", 40, 636, 600, "Fixed −$0.6M and $0.0M: column, bar, card (three-section)")
write("s1_col_minus", 40, 668, 176, 150, bars("S1 Minus 0.6M (label-safe)", "clusteredColumnChart", ("Scenario", "Scenario", "Scenario")))
write("s1_bar_minus", 224, 668, 200, 150, bars("S1 Minus 0.6M (label-safe)", "clusteredBarChart", ("Scenario", "Scenario", "Scenario")))
write("s1_card_num", 440, 668, 96, 32, card("S1 Minus 0.6M (label-safe)", border=RULE))
write("s1_card_zero", 544, 668, 96, 32, card("S1 Zero (label-safe)", border=RULE))
write("s1_col_zero", 440, 708, 200, 110, bars("S1 Zero (label-safe)", "clusteredColumnChart", ("Scenario", "Scenario", "Scenario")))
note("n_s1c", 40, 826, 600, "Wrap test, 14 × '−$0.6M ': with U+2060 (left), without (right)")
write("s1_card_joiner", 40, 858, 296, 96, card("S1 Tokens (text)", border=RULE))
write("s1_card_nojoiner", 344, 858, 296, 96, card("S1 Tokens no joiner (text)", border=RULE))

# ---- S-5 (middle column) -----------------------------------------------------
note("n_s5", 680, 24, 560, "S-5 · stacked area, per-series area (top: candidate from the catalog, bottom: untouched)")
f1 = json.loads((P1 / "ch_f1_margin" / "visual.json").read_text(encoding="utf-8"))
f1_filters = f1["filterConfig"]["filters"]


def area(candidate):
    v = copy.deepcopy(f1["visual"])
    v["visualType"] = "stackedAreaChart"
    v["query"]["queryState"]["Y"]["projections"] = [
        proj_m("Trend Margin after GI", "After commissions"),
        proj_m("S5 Commission Take GI", "Commissions")]
    o = v["objects"]
    o["dataPoint"] = [
        {"properties": {"fill": col(BLUE)}, "selector": {"metadata": "_Measures.Trend Margin after GI"}},
        {"properties": {"fill": col(GREY)}, "selector": {"metadata": "_Measures.S5 Commission Take GI"}}]
    o["lineStyles"] = [
        {"properties": {"strokeWidth": lit("2D"), "showMarker": lit("false"), "lineChartType": lit("'linear'")}},
        {"properties": {"strokeWidth": lit("3D")}, "selector": {"metadata": "_Measures.Trend Margin after GI"}},
        {"properties": {"strokeWidth": lit("2D")}, "selector": {"metadata": "_Measures.S5 Commission Take GI"}}]
    if candidate:
        # catalog: lineStyles.areaShow ("Shade area", bool), dataPoint.transparency ("Area transparency", numeric)
        o["lineStyles"][1]["properties"]["areaShow"] = lit("false")
        o["lineStyles"][2]["properties"]["areaShow"] = lit("true")
        o["dataPoint"].insert(0, {"properties": {"transparency": lit("70D")}})
    v["visualContainerObjects"] = vco(header=True)
    return v


write("s5_area_candidate", 680, 56, 560, 248, area(True), f1_filters)
write("s5_area_plain", 680, 320, 560, 248, area(False), f1_filters)

# ---- S-6 (middle column, below) ----------------------------------------------
note("n_s6", 680, 592, 560, "S-6 · page-navigation button (candidate; Ctrl+click goes to The Investment Strategy)")
btn = json.loads((DST / REPORT / "definition" / "pages" / "p2-investment-strategy" / "visuals" / "tab_alts_off"
                  / "visual.json").read_text(encoding="utf-8"))["visual"]
b = copy.deepcopy(btn)
for t in b["objects"]["text"]:
    if "text" in t["properties"]:
        t["properties"]["text"] = lit("'→ Page 2: the plan'")
b["visualContainerObjects"]["visualLink"] = [{"properties": {
    "show": lit("true"), "type": lit("'PageNavigation'"), "navigationSection": lit("'p2-investment-strategy'")}}]
b["visualContainerObjects"]["general"] = [{"properties": {"altText": lit("'Go to page 2, The Investment Strategy'")}}]
write("s6_nav_candidate", 680, 624, 248, 32, b)
note("n_s6b", 680, 672, 560, "Bjorn: insert your own page-navigation button below this line (only if asked)", h=24)

# ---- S-7 (right column) ------------------------------------------------------
note("n_s7", 1320, 24, 560, "S-7 · UNICHAR(10) in a table cell (wrap on) and card values (four break characters)")
tbl = json.loads((P1 / "tbl_f2_folio" / "visual.json").read_text(encoding="utf-8"))["visual"]
t = copy.deepcopy(tbl)
t["query"]["queryState"]["Values"]["projections"] = [
    proj_c("InvestmentProjects", "ProjectID", "ID"), proj_m("S7 Cell (text)", "Two-line cell"),
    proj_m("S1 Tokens (text)", "Wrap, joiner"), proj_m("S1 Tokens no joiner (text)", "Wrap, no joiner")]
t["objects"]["values"][0]["properties"]["wordWrap"] = lit("true")
t["objects"]["columnHeaders"][0]["properties"]["wordWrap"] = lit("true")
t["objects"]["columnHeaders"][0]["properties"]["autoSizeColumnWidth"] = lit("false")
t["objects"]["columnFormatting"] = []
t["objects"]["columnWidth"] = [
    {"properties": {"value": lit(f"{w}D")}, "selector": {"metadata": q}} for q, w in [
        ("InvestmentProjects.ProjectID", 64), ("_Measures.S7 Cell (text)", 232),
        ("_Measures.S1 Tokens (text)", 122), ("_Measures.S1 Tokens no joiner (text)", 122)]]
t["visualContainerObjects"] = vco(header=True)
write("s7_table", 1320, 56, 560, 150, t, gi)
# the card's fallback: a table with the measure only (one row), same break
t1 = copy.deepcopy(tbl)
t1["query"]["queryState"]["Values"]["projections"] = [proj_m("S7 Card LF (text)", "One-row table on the card measure")]
t1["objects"]["values"][0]["properties"]["wordWrap"] = lit("true")
t1["objects"]["columnFormatting"] = []
t1["visualContainerObjects"] = vco(header=False)
write("s7_table_one", 1320, 212, 560, 76, t1)
for i, k in enumerate(["LF", "CRLF", "LS", "PS"]):
    write(f"s7_card_{k.lower()}", 1320 + (i % 2) * 284, 296 + (i // 2) * 64, 276, 56, card(f"S7 Card {k} (text)", border=RULE))

# ---- S-8 (right column, below) -----------------------------------------------
note("n_s8", 1320, 440, 560, "S-8 · ⓘ (U+24D8) from the Segoe UI stack: hover tag (text box) and chip (card)")
write("s8_tag", 1320, 480, 144, 28, textbox([("ⓘ", TANGERINE, "16px"), (" Hover a bar", NIGHT, "16px")],
                                             background="#FFFFFF", border=RULE, radius=14, align="center"))
write("s8_chip", 1480, 480, 144, 28, card("S8 Definitions (text)", background="#FFFFFF", border=RULE, radius=14,
                                          wrap=False, align="center"))
write("s8_big", 1320, 524, 560, 64, textbox([("ⓘ", TANGERINE, "40px"), (" ⓘ Hover a bar · 30 pt", NIGHT, "40px")]))
write("s8_tag_night", 1320, 604, 144, 28, textbox([("ⓘ", "#F7F5EE", "16px"), (" Hover a dot", "#F7F5EE", "16px")],
                                                   background=NIGHT, radius=14, align="center"))
print("copy ready:", DST)
