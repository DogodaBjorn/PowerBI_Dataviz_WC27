"""Step 2 spikes (doc 23): S-2 the hero table with SVG bar cells, S-3 the native selector (button slicer + table).

Usage: python spike2_prep.py <project pbip dir> <destination dir> [--report-only] [key=value ...]

Nothing in the project is touched: the Report and the model (with its data cache) are copied, spike columns and
measures are appended to the COPY's model, and scratch pages are added to the COPY's report.
Property names come from `powerbi-report-author formatting describe-object tableEx|advancedSlicerVisual ...`
(Microsoft's catalog) and, for the header outline values, from Desktop's own table code ('BottomOnly').

Knobs (key=value, all optional; the defaults are the values that passed on 13 Nov 2026):
  hero_pad=0  hero_img_h=34  hero_h=372  hero_w=(columns + 2)  hero_cols=280/104/96/196/64/184/74
  img_pad=7  img_w=(the comp's narrow bar column - img_pad)
  active=<page name>  moves_pad=5.36  moves_y=237  moves_h=(to the slicer's bottom)  moves_cols=92/64/74/118  tile_pad=0  icon=16  key_w=0
Flags: --report-only (Desktop is open: rewrite the pages, then `powerbi-desktop reload`), --diag (Tangerine gridlines)
"""
import json
import shutil
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--") and "=" not in a]
KNOB = dict(a.split("=", 1) for a in sys.argv[1:] if "=" in a and not a.startswith("--"))
SRC, DST = Path(args[0]), Path(args[1])
REPORT_ONLY = "--report-only" in sys.argv
DIAG = "--diag" in sys.argv
SRC_REPORT = "GoodnightInn-opzet.Report"
REPORT = "SPIKE2-throwaway.Report"  # same stem as the .pbip, or `powerbi-desktop reload` finds no report folder
MODEL = "PillowKey.SemanticModel"
SCHEMA_VC = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.11.0/schema.json"
SCHEMA_PAGE = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json"
FONT = "'''Segoe UI'', wf_segoe-ui_normal, helvetica, arial, sans-serif'"
NIGHT, DUSK, HAIR, TANGERINE, BLUE, BLUE_T, GREY, BAD = "#12233D", "#4B5466", "#E3DFD3", "#E05A22", "#2589D8", "#1763A8", "#8E897D", "#A63F0E"

# ---------------------------------------------------------------- the hero constants (spec construction.tables.tbl_hero)
SPEC_COLS = [280, 104, 96, 196, 64, 180, 72]  # the comp's widths: the bar geometry and the reference labels stay on these
# What Desktop needs (measured 13 Nov): an image column of image + 11 px (7 left, 4 right; less draws a clipped
# ellipsis beside the image) and 74 px for "−$27.3M" (cells pad 7.7 px left and 5 px right; the comp assumed 5 + 5).
HERO_COLS = [int(v) for v in KNOB.get("hero_cols", "280/104/96/196/64/184/74").split("/")]
# 2 px wider than the columns: at exactly the column sum Desktop shows a horizontal and then a vertical scrollbar
HERO = dict(x=56, y=240, w=int(KNOB.get("hero_w", sum(HERO_COLS) + 2)), h=int(KNOB.get("hero_h", 372)))
ROW_H, INSET, BAR_Y, BAR_H = 34, 4, 8, 18
# Desktop draws an image IMG_PAD px from the left edge of its cell (measured, not a setting), and `grid.imageWidth` is
# one value for the whole table. So both bar images get the same width, the narrow column minus the padding, and
# every x inside the SVG is the comp's cell x minus IMG_PAD. The reference lines then sit where the comp has them.
IMG_PAD = float(KNOB.get("img_pad", 7))
IMG_W = int(KNOB.get("img_w", 0)) or int(SPEC_COLS[5] - IMG_PAD)
YDOM, YREF = (-0.1, 0.9), 0.08
NDOM, NREF = (-32e6, 12e6), 0.0


def bar_x(v, dom, w):
    """The comp's barX(): the x of a value inside a bar cell of width w."""
    return INSET + (v - dom[0]) / (dom[1] - dom[0]) * (w - 2 * INSET)


def hero_ref_x():
    """Page x of the two reference lines; the labels lbl_hero_8 / lbl_hero_0 are placed from the same constants."""
    x_y = HERO["x"] + sum(HERO_COLS[:3]) + bar_x(YREF, YDOM, SPEC_COLS[3])
    x_n = HERO["x"] + sum(HERO_COLS[:5]) + bar_x(NREF, NDOM, SPEC_COLS[5])
    return x_y, x_n


def bar_cell(value_expr, dom, w, ref, fill_expr):
    """P-4 prototype: a DAX expression for an SVG data URI with one bar from zero and one full-height reference line.
    Fixed pixel width and fixed domain, so the reference line has the same x in every row and scenario.
    Numbers go through FORMAT ( x, "0.0", "en-US" ): a comma locale never breaks the SVG. '#' is written as %23."""
    span, inner = dom[1] - dom[0], w - 2 * INSET
    x0 = bar_x(max(dom[0], min(dom[1], 0.0)), dom, w) - IMG_PAD
    xr = bar_x(ref, dom, w) - IMG_PAD
    f = 'FORMAT ( {0}, "0.0", "en-US" )'
    return (
        f"VAR v = {value_expr} "
        f"VAR c = MIN ( MAX ( v, {dom[0]!r} ), {dom[1]!r} ) "
        f"VAR xv = {INSET - IMG_PAD!r} + ( c - ( {dom[0]!r} ) ) / {span!r} * {inner} "
        f"VAR x0 = {x0!r} "
        f'VAR fill = SUBSTITUTE ( {fill_expr}, "#", "%23" ) '
        "RETURN IF ( ISBLANK ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) ), BLANK (), "
        f"\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{IMG_W}' height='{ROW_H}' viewBox='0 0 {IMG_W} {ROW_H}'>"
        f"<rect x='\" & {f.format('MIN ( x0, xv )')} & \"' y='{BAR_Y}' width='\" & {f.format('ABS ( xv - x0 )')} & \"' height='{BAR_H}' fill='\" & fill & \"'/>"
        f"<rect x='{xr - 0.5:.2f}' y='0' width='1' height='{ROW_H}' fill='%2312233D' shape-rendering='crispEdges'/></svg>\" )"
    )


# ---------------------------------------------------------------- copy
if not REPORT_ONLY:
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    shutil.copytree(SRC / SRC_REPORT, DST / REPORT)
    shutil.copytree(SRC / MODEL, DST / MODEL)
    pbip = (SRC / "GoodnightInn-opzet.pbip").read_text(encoding="utf-8").replace(SRC_REPORT, REPORT)
    (DST / "SPIKE2-throwaway.pbip").write_text(pbip, encoding="utf-8")

# ---------------------------------------------------------------- model: spike columns and measures (copy only)
MINUS, WJ = "UNICHAR ( 8722 )", "UNICHAR ( 8288 )"
PID = "InvestmentProjects[ProjectID]"
NAMES = {"GI-01": "Booking app & member rates", "GI-10": "Revenue management", "GI-02": "Kiosks at the 20 busiest hotels",
         "GI-09": "Breakfast upgrade", "GI-05": "Gatwick +40 rooms", "GI-03": "Energy programme", "GI-04": "Toronto +40 rooms",
         "GI-06": "Kingston +40 rooms", "GI-08": "Boston new hotel", "GI-07": "Refresh, 10 oldest hotels"}
FINDING = {"GI-01": "F2", "GI-10": "F1", "GI-02": "F4", "GI-09": "F3", "GI-05": "F4", "GI-03": "F1", "GI-04": "F4", "GI-06": "F4",
           "GI-08": "F4", "GI-07": "F3"}
STATUS = {"GI-01": "A", "GI-10": "A", "GI-02": "A", "GI-05": "2028 gate", "GI-04": "2028 gate", "GI-07": "2028 gate"}


def switch(mapping, default):
    return "SWITCH ( " + PID + ", " + ", ".join(f'"{k}", "{v}"' for k, v in mapping.items()) + f", {default} )"


YIELD_EXP = ("DIVIDE ( SUMX ( FILTER ( InvestmentScenarios, InvestmentScenarios[ProjectID] = {p} && InvestmentScenarios[Scenario] = \"Expected\" ), "
             "InvestmentScenarios[AnnualOperatingProfitImpactUSD] ), {c} )")
columns = [
    ("S2 Move Name", "string", switch(NAMES, "InvestmentProjects[ProjectName]"), "S2 Hero Sort"),
    # rank of the Expected "a year on cost" inside the brand, fixed at refresh (the order never follows the scenario);
    # column-only table expressions and no context transition, so the column depends on source columns only
    ("S2 Hero Sort", "int64",
     'VAR myp = InvestmentProjects[ProjectID] VAR myc = InvestmentProjects[CapexUSD] VAR myb = InvestmentProjects[Brand] '
     'VAR gi = FILTER ( ALL ( InvestmentProjects[ProjectID], InvestmentProjects[CapexUSD], InvestmentProjects[Brand] ), InvestmentProjects[Brand] = "Goodnight Inn" ) '
     'VAR me = ' + YIELD_EXP.format(p="myp", c="myc")
     + ' RETURN IF ( myb = "Goodnight Inn", COUNTROWS ( FILTER ( gi, VAR p = InvestmentProjects[ProjectID] VAR c = InvestmentProjects[CapexUSD] RETURN '
     + YIELD_EXP.format(p="p", c="c") + " > me ) ) + 1, 99 )", None),
    ("S2 Status", "string", switch(STATUS, '"not now"'), None),
]
col_lines = []
for name, dtype, expr, sortby in columns:
    col_lines.append(f"\tcolumn '{name}' = {expr}")
    col_lines.append(f"\t\tdataType: {dtype}")
    if dtype == "int64":
        col_lines.append("\t\tformatString: 0")
    if sortby:
        col_lines.append(f"\t\tsortByColumn: '{sortby}'")
    col_lines.append("\t\tsummarizeBy: none")
    col_lines.append("")

SEL = f"SELECTEDVALUE ( {PID} )"
STAT = "SELECTEDVALUE ( InvestmentProjects[S2 Status] )"
YLD = "DIVIDE ( [2032 Run-rate], SUM ( InvestmentProjects[CapexUSD] ) )"
MARK = f'SWITCH ( {STAT}, "A", "{BLUE}", "2028 gate", "{NIGHT}", "{GREY}" )'
NPV_T = ('VAR v = [NPV @ 8%] / 1000000 VAR r1 = ROUND ( v, 1 ) VAR r2 = ROUND ( v, 2 ) VAR sg = IF ( v < 0, ' + MINUS + ', "+" ) & ' + WJ + ' '
         f'RETURN IF ( ISBLANK ( {SEL} ), BLANK (), SWITCH ( TRUE (), r2 = 0, "$0.0M", r1 = 0, sg & "$" & FORMAT ( ABS ( r2 ), "0.00", "en-US" ) & "M", '
         'sg & "$" & FORMAT ( ABS ( r1 ), "0.0", "en-US" ) & "M" ) )')
BM = "SELECTEDVALUE ( BuildMove[ProjectID] )"
RR_T = (f'VAR p = {BM} VAR v = CALCULATE ( [2032 Run-rate], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) / 1000000 '
        'VAR r1 = ROUND ( v, 1 ) RETURN IF ( ISBLANK ( p ), BLANK (), IF ( r1 = 0, "$0.0M", IF ( r1 < 0, ' + MINUS + ', "+" ) & ' + WJ
        + ' & "$" & FORMAT ( ABS ( r1 ), "0.0", "en-US" ) & "M" ) )')
measures = [
    # (name, expression, data category)
    ("S2 Yield", YLD, None),
    ("S2 Yield (text)", f'VAR y = {YLD} RETURN IF ( ISBLANK ( {SEL} ), BLANK (), IF ( ROUND ( y, 3 ) < 0, {MINUS}, "" ) & '
                        'FORMAT ( ABS ( y ) * 100, "0.0", "en-US" ) & "%" )', None),
    ("S2 NPV (text)", NPV_T, None),
    ("S2 Answers (text)", f'VAR p = {SEL} RETURN IF ( ISBLANK ( p ), BLANK (), ' + switch(FINDING, '""').replace(PID, "p")
     + ' & IF ( SELECTEDVALUE ( InvestmentProjects[GrowthInitiative] ) = "Yes", " · growth", "" ) )', None),
    ("S2 Mark Color", MARK, None),
    ("S2 Status Text Color", f'SWITCH ( {STAT}, "A", "{BLUE_T}", "2028 gate", "{NIGHT}", "{DUSK}" )', None),
    ("S2 NPV Text Color", f'IF ( ROUND ( [NPV @ 8%] / 1000000, 2 ) < 0, "{BAD}", "{NIGHT}" )', None),
    ("S2 Yield Bar SVG", bar_cell(YLD, YDOM, SPEC_COLS[3], YREF, MARK), "ImageUrl"),
    ("S2 NPV Bar SVG", bar_cell("[NPV @ 8%]", NDOM, SPEC_COLS[5], NREF, MARK), "ImageUrl"),
    ("S3 Run-rate (text)", RR_T, None),
    ("S3 NPV Text Color", f'IF ( ROUND ( [Move NPV (num)] / 1000000, 2 ) < 0, "{BAD}", "{NIGHT}" )', None),
    ("S3 Picked (text)", '"Picked: " & [Build Count] & IF ( [Build Count] = 1, " move, ", " moves, " ) & [Build Capex (text)] & " of $60.0M"', None),
]
mea_lines = []
for name, expr, cat in measures:
    mea_lines.append(f"\tmeasure '{name}' = {expr}")
    mea_lines.append("\t\tdisplayFolder: 99 Spike")
    if cat:
        mea_lines.append(f"\t\tdataCategory: {cat}")
    mea_lines.append("")


# the expressions as data too: a measure change does not reach a running Desktop through `powerbi-desktop reload`
# (report only); push it with the modelling MCP (measure_operations Update) or project/tools/sync_measures_to_desktop.ps1
DST.mkdir(parents=True, exist_ok=True)
(DST / "spike_measures.json").write_text(json.dumps({n: e for n, e, _ in measures}, indent=1, ensure_ascii=False), encoding="utf-8")


def insert_before_first(path, marker, block):
    text = path.read_bytes().decode("utf-8")
    i = text.find(marker)
    assert i >= 0, f"marker {marker!r} not found in {path.name}"
    path.write_bytes((text[: i + 2] + block + text[i + 2:]).encode("utf-8"))


if not REPORT_ONLY:
    tables = DST / MODEL / "definition" / "tables"
    insert_before_first(tables / "_Measures.tmdl", "\r\n\tcolumn ", "\r\n".join(mea_lines) + "\r\n")
    insert_before_first(tables / "InvestmentProjects.tmdl", "\r\n\tpartition ", "\r\n".join(col_lines) + "\r\n")


# ---------------------------------------------------------------- report helpers
def lit(v):
    return {"expr": {"Literal": {"Value": v}}}


def col(hex_):
    return {"solid": {"color": lit(f"'{hex_}'")}}


def meas(name):
    return {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": name}}


def colref(entity, column):
    return {"Column": {"Expression": {"SourceRef": {"Entity": entity}}, "Property": column}}


def proj_m(name, display=None):
    p = {"field": meas(name), "queryRef": f"_Measures.{name}", "nativeQueryRef": name}
    if display is not None:
        p["displayName"] = display
    return p


def proj_c(entity, column, display=None):
    p = {"field": colref(entity, column), "queryRef": f"{entity}.{column}", "nativeQueryRef": column}
    if display is not None:
        p["displayName"] = display
    return p


def filter_in(entity, column, values, name):
    return {"name": name, "field": colref(entity, column), "type": "Categorical", "howCreated": "User",
            "filter": {"Version": 2, "From": [{"Name": "f", "Entity": entity, "Type": 0}],
                       "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "f"}}, "Property": column}}],
                                                         "Values": [[{"Literal": {"Value": f"'{v}'"}}] for v in values]}}}]}}


def vco(header=False, alt=None, background=None, border=None):
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
        o["border"] = [{"properties": {"show": lit("true"), "color": col(border), "width": lit("1D")}}]
    if alt:
        o["general"] = [{"properties": {"altText": lit("'" + alt.replace("'", "''") + "'")}}]
    return o


PAGES = DST / REPORT / "definition" / "pages"
SPIKE_PAGES = []
z = [0]


def page(name, title):
    p = PAGES / name
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True)
    (p / "page.json").write_text(json.dumps({
        "$schema": SCHEMA_PAGE, "name": name, "displayName": title, "displayOption": "FitToPage", "height": 1080, "width": 1920,
        "objects": {"background": [{"properties": {"color": col("#FFFFFF"), "transparency": lit("0D")}}]},
    }, indent=2) + "\n", encoding="utf-8")
    SPIKE_PAGES.append(name)
    z[0] = 0
    # fiducials: Night squares at the page corners, so measure.py can map capture pixels to page pixels
    for nm, fx, fy in (("fid_tl", 0, 0), ("fid_br", 1904, 1064)):
        write(p, nm, fx, fy, 16, 16, {"visualType": "textbox", "objects": {}, "visualContainerObjects": vco(background=NIGHT),
                                      "drillFilterOtherVisuals": False})
    return p


def write(pg, name, x, y, w, h, visual, filters=None):
    z[0] += 1000
    d = {"$schema": SCHEMA_VC, "name": name,
         "position": {"x": x, "y": y, "z": z[0], "width": w, "height": h, "tabOrder": z[0]}, "visual": visual}
    if filters:
        d["filterConfig"] = {"filters": filters}
    p = pg / "visuals" / name
    p.mkdir(parents=True, exist_ok=True)
    (p / "visual.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def textbox(text, color=DUSK, size="16px", align="left", background=None):
    return {"visualType": "textbox",
            "objects": {"general": [{"properties": {"paragraphs": [{
                "textRuns": [{"value": text, "textStyle": {"fontFamily": "'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif",
                                                           "fontSize": size, "color": color}}],
                "horizontalTextAlignment": align}]}}]},
            "visualContainerObjects": vco(background=background), "drillFilterOtherVisuals": False}


def card(measure, color=NIGHT, border=None):
    """A plain cardVisual on one text measure (the shape of the report's sentence cards, read from c_f1_note)."""
    src = json.loads((PAGES / "p1-brand-review" / "visuals" / "c_f1_note" / "visual.json").read_text(encoding="utf-8"))["visual"]
    src["query"]["queryState"]["Data"]["projections"] = [proj_m(measure)]
    src["objects"]["value"][0]["properties"]["fontColor"] = col(color)
    src["visualContainerObjects"] = vco(border=border)
    src["visualContainerObjects"]["general"] = [{"properties": {"altText": {"expr": meas(measure)}}}]
    return src


WILD = {"data": [{"dataViewWildcard": {"matchingOption": 1}}]}


def table(projections, widths, header_h_hint=None, row_padding=0, image=None, right=(), font_colors=None, field_colors=None,
          header_rule=True, wrap=False, alt="spike table"):
    """tableEx: fixed column widths, no grid, one hairline under the header.
    widths by queryRef · right: queryRefs right-aligned (header and values) · font_colors: {queryRef: hex} (static)
    · field_colors: {queryRef: measure name} (font colour from a measure) · image: (height, width or None)."""
    grid = {"gridVertical": lit("false"), "gridHorizontal": lit("false"), "rowPadding": lit(f"{row_padding}D"), "outlineStyle": lit("'None'")}
    if DIAG:  # diagnostic render: Tangerine gridlines show the real column and row boundaries
        grid.update({"gridVertical": lit("true"), "gridVerticalColor": col(TANGERINE), "gridVerticalWeight": lit("1D"),
                     "gridHorizontal": lit("true"), "gridHorizontalColor": col(TANGERINE), "gridHorizontalWeight": lit("1D")})
    if image:
        grid["imageHeight"] = lit(f"{image[0]}D")
        if image[1]:
            grid["imageWidth"] = lit(f"{image[1]}D")
    head = {"fontFamily": lit(FONT), "fontSize": lit("12D"), "fontColor": col(DUSK), "backColor": col("#FFFFFF"), "bold": lit("false"),
            "outlineStyle": lit("'BottomOnly'" if header_rule else "'None'"), "outlineColor": col(DUSK), "outlineWeight": lit("1D"),
            "autoSizeColumnWidth": lit("false"), "wordWrap": lit("true" if wrap else "false")}
    values = {"fontFamily": lit(FONT), "fontSize": lit("12D"), "fontColorPrimary": col(NIGHT), "fontColorSecondary": col(NIGHT),
              "backColorPrimary": col("#FFFFFF"), "backColorSecondary": col("#FFFFFF"), "outlineStyle": lit("'None'"),
              "wordWrap": lit("true" if wrap else "false"), "urlIcon": lit("false")}
    vals = [{"properties": values}]
    for q, mname in (field_colors or {}).items():
        vals.append({"properties": {"fontColor": {"solid": {"color": {"expr": meas(mname)}}}}, "selector": {**WILD, "metadata": q}})
    fmt = []
    for q in right:
        fmt.append({"properties": {"alignment": lit("'Right'"), "styleHeader": lit("true"), "styleValues": lit("true")}, "selector": {"metadata": q}})
    for q, hexv in (font_colors or {}).items():
        fmt.append({"properties": {"fontColor": col(hexv), "styleHeader": lit("false"), "styleValues": lit("true")}, "selector": {"metadata": q}})
    objs = {"columnHeaders": [{"properties": head}], "values": vals, "grid": [{"properties": grid}],
            "total": [{"properties": {"totals": lit("false")}}],
            "columnWidth": [{"properties": {"value": lit(f"{w}D")}, "selector": {"metadata": q}} for q, w in widths.items()]}
    if fmt:
        objs["columnFormatting"] = fmt
    return {"visualType": "tableEx", "query": {"queryState": {"Values": {"projections": projections}}}, "objects": objs,
            "visualContainerObjects": vco(alt=alt), "drillFilterOtherVisuals": False}


# ---------------------------------------------------------------- S-2: the hero table, one page per scenario
GI = filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_gi_proj")
HERO_PAD = float(KNOB.get("hero_pad", 0))
HERO_IMG = (float(KNOB.get("hero_img_h", ROW_H)), IMG_W)
hero_q = ["InvestmentProjects.S2 Move Name", "_Measures.S2 Answers (text)", "InvestmentProjects.S2 Status", "_Measures.S2 Yield Bar SVG",
          "_Measures.S2 Yield (text)", "_Measures.S2 NPV Bar SVG", "_Measures.S2 NPV (text)"]


def hero_table():
    proj = [proj_c("InvestmentProjects", "S2 Move Name", "Move"), proj_m("S2 Answers (text)", "Answers"),
            proj_c("InvestmentProjects", "S2 Status", "Status"), proj_m("S2 Yield Bar SVG", "A year on cost"),
            proj_m("S2 Yield (text)", "​"), proj_m("S2 NPV Bar SVG", "NPV through 2032"), proj_m("S2 NPV (text)", "​​")]
    return table(proj, dict(zip(hero_q, HERO_COLS)), row_padding=HERO_PAD, image=HERO_IMG, right=(hero_q[4], hero_q[6]),
                 font_colors={hero_q[1]: DUSK}, field_colors={hero_q[2]: "S2 Status Text Color", hero_q[6]: "S2 NPV Text Color"},
                 alt="Hero table spike: ten moves, a year on cost and NPV through 2032 as bars with their values")


x8, x0 = hero_ref_x()
for scen in ("Expected", "Low", "High"):
    pg = page(f"s2-hero-{scen.lower()}", f"S-2 hero · {scen}")
    scen_f = filter_in("Scenario", "Scenario", [scen], "flt_scen")
    write(pg, "n_s2", 56, 120, 992, 24, textbox(f"S-2 · hero table, {scen} case · 56, 240, {HERO['w']}, {HERO['h']} · columns "
                                                + "/".join(str(c) for c in HERO_COLS) + f" · rows 34, row padding {HERO_PAD:g}"))
    write(pg, "c_scen", 56, 152, 300, 24, card("Selected Scenario"), [scen_f])
    # the two reference labels at the comp's slots (lbl_hero_8 starts at the 8 % line, lbl_hero_0 ends at the 0 line)
    write(pg, "lbl_hero_8", round(x8), 216, 176, 24, textbox("8%: our cost of money"))
    write(pg, "lbl_hero_0", round(x0) - 168, 216, 168, 24, textbox("pays back by 2032 →", align="right"))
    write(pg, "tbl_hero", HERO["x"], HERO["y"], HERO["w"], HERO["h"], hero_table(), [GI, scen_f])
    # a frame of the slot, 8 px outside, so a scrollbar or an overflow shows against it
    write(pg, "n_slot", 56, 620, 992, 24, textbox("slot ends at y 612 (this line starts at 620)"))
    # the page-ruler: where the generator expects the two reference lines
    write(pg, "n_x", 56, 652, 992, 24, textbox(f"expected reference lines at page x {x8:.2f} and {x0:.2f}"))

# ---------------------------------------------------------------- S-3: the native selector
SL = dict(x=792, y=280, w=216, h=320)
TM = dict(x=1008, y=248, w=344, h=352)
MOVES_SPEC = [92, 64, 72, 116]  # the comp's widths
# Desktop needs 74 for "−$27.3M" and 118 for the header "A year by 2032" (cell padding, see the hero), and 2 px of slack
MOVES_COLS = [int(v) for v in KNOB.get("moves_cols", "92/64/74/118").split("/")]
A_MOVES = ["Booking app", "Revenue management", "Kiosks at 20 desks"]
# rows of 32 px: a 12 pt line is 21.28 px, so the padding is (32 - 21.28) / 2; Desktop honours the fraction.
# The header takes the same padding and becomes 43.3 px (32.6 at padding 0), so the table starts at 280 - 43 = 237.
MOVES_PAD = float(KNOB.get("moves_pad", 5.36))
TILE_PAD = int(KNOB.get("tile_pad", 0))
ICON = int(KNOB.get("icon", 16))
KEY_W = float(KNOB.get("key_w", 0))
MOVES_Y = int(KNOB.get("moves_y", 237))


def move_slicer(selected):
    sel = lambda s: {"selector": {"id": s}}  # noqa: E731
    objs = {
        "shapeCustomRectangle": [{"properties": {"tileShape": lit("'rectangle'")}, **sel("default")}],
        "layout": [{"properties": {"rowCount": lit("10L"), "columnCount": lit("1L"), "maxTiles": lit("10L"), "cellPadding": lit(f"{TILE_PAD}L")}}],
        "fillCustom": [{"properties": {"show": lit("true"), "fillColor": col("#FFFFFF"), "transparency": lit("0D")}, **sel("default")},
                       {"properties": {"fillColor": col(HAIR)}, **sel("interaction:hover")},
                       {"properties": {"fillColor": col(HAIR)}, **sel("interaction:press")},
                       {"properties": {"fillColor": col("#FFFFFF")}, **sel("selection:selected")}],
        "outline": [{"properties": {"show": lit("false")}, **sel("default")}],
        "value": [{"properties": {"show": lit("true"), "fontFamily": lit(FONT), "fontSize": lit("12D"), "fontColor": col(NIGHT), "bold": lit("false"),
                                  "horizontalAlignment": lit("'left'"), "verticalAlignment": lit("'middle'")}, **sel("default")},
                  {"properties": {"fontColor": col(NIGHT), "bold": lit("false")}, **sel("selection:selected")}],
        "label": [{"properties": {"show": lit("false")}, **sel("default")}],
        "padding": [{"properties": {"paddingSelection": lit("'Custom'"), "topMargin": lit("0L"), "bottomMargin": lit("0L"),
                                    "leftMargin": lit("8L"), "rightMargin": lit("8L")}, **sel("default")}],
        "selectionIcon": [{"properties": {"show": lit("true"), "position": lit("'Left'"), "size": lit(f"{ICON}L"), "color": col(NIGHT)}, **sel("default")},
                          {"properties": {"color": col(NIGHT)}, **sel("selection:selected")}],
        "selection": [{"properties": {"singleSelect": lit("false"), "strictSingleSelect": lit("false"), "selectAllCheckboxEnabled": lit("false")}}],
        "general": [{"properties": {"filter": {"filter": {
            "Version": 2, "From": [{"Name": "b", "Entity": "BuildMove", "Type": 0}],
            "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "b"}}, "Property": "Short Name"}}],
                                              "Values": [[{"Literal": {"Value": f"'{v}'"}}] for v in selected]}}}]}}}}] if selected else [],
    }
    if not selected:
        del objs["general"]
    return {"visualType": "advancedSlicerVisual", "query": {"queryState": {"Values": {"projections": [proj_c("BuildMove", "Short Name")]}}},
            "objects": objs,
            "visualContainerObjects": vco(alt="Moves: click a move to add or remove it; Tab to a move, Space to pick it"),
            "drillFilterOtherVisuals": False}


# The table needs one BuildMove column to get a row per move. It is the move's own name at width 0: nothing shows
# (the names are on the tiles), and a screen reader still reads the name with the row.
moves_q = ["BuildMove.Short Name", "_Measures.Move Answers (text)", "_Measures.Move Capex (text)", "_Measures.Move NPV (text)", "_Measures.S3 Run-rate (text)"]


def moves_table():
    proj = [proj_c("BuildMove", "Short Name", "Move"), proj_m("Move Answers (text)", "Answers"), proj_m("Move Capex (text)", "Capex"),
            proj_m("Move NPV (text)", "NPV"), proj_m("S3 Run-rate (text)", "A year by 2032")]
    return table(proj, dict(zip(moves_q, [KEY_W] + MOVES_COLS)), row_padding=MOVES_PAD, right=tuple(moves_q[2:]),
                 font_colors={moves_q[1]: DUSK, moves_q[0]: "#FFFFFF"}, field_colors={moves_q[3]: "S3 NPV Text Color"},
                 alt="Moves table spike: answers, capex, NPV and a year by 2032 for the ten moves, in the order of the selector")


pg = page("s3-selector", "S-3 selector")
MOVES_W, MOVES_H = sum(MOVES_COLS) + KEY_W + 2, int(KNOB.get("moves_h", SL["y"] + SL["h"] - MOVES_Y))
write(pg, "n_s3", 792, 120, 1072, 24, textbox(f"S-3 · button slicer 792, 280, 216, 320 beside table 1008, {MOVES_Y}, {MOVES_W:g}, {MOVES_H} · "
                                               f"row padding {MOVES_PAD:g}, tile padding {TILE_PAD}, icon {ICON}"))
write(pg, "sl_moves", SL["x"], SL["y"], SL["w"], SL["h"], move_slicer(A_MOVES))
write(pg, "tbl_moves", TM["x"], MOVES_Y, MOVES_W, MOVES_H, moves_table())
write(pg, "c_sel_footer", 792, 608, 560, 24, card("S3 Picked (text)"))
write(pg, "c_build_title", 1384, 256, 464, 40, card("Build Title (text)"))
write(pg, "n_s3b", 792, 648, 1072, 24, textbox("The two cards read the slicer's selection through the Build measures (ISFILTERED / ALLSELECTED on BuildMove)."))
# the table must keep ten rows when tiles are deselected: the slicer does not filter it (doc 21 section 8)
pj = pg / "page.json"
pd = json.loads(pj.read_text(encoding="utf-8"))
pd["visualInteractions"] = [{"source": "sl_moves", "target": "tbl_moves", "type": "NoFilter"}]
pj.write_text(json.dumps(pd, indent=2) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- page order
pj = PAGES / "pages.json"
pages = json.loads(pj.read_text(encoding="utf-8"))
pages["pageOrder"] = SPIKE_PAGES + [p for p in pages["pageOrder"] if p not in SPIKE_PAGES]
pages["activePageName"] = KNOB.get("active", SPIKE_PAGES[0])  # active=s3-selector puts the selector on screen for s3_keys.ps1
pj.write_text(json.dumps(pages, indent=2) + "\n", encoding="utf-8")
print("copy ready:", DST, "| pages:", ", ".join(SPIKE_PAGES), f"| reference lines at page x {x8:.2f}, {x0:.2f}")
