"""Writes the report set-up (opzet) as a PBIP report on the shared model. v2 of 2026-11-07: the D1 briefing,
stripped (06-d1-briefing-opzet.md): P1 = headline, four benchmarked KPIs, findings F1-F3 with one chart each,
F4 where we are full; P2 = the package scatter with the focus swap and one recommendation (A) plus alternatives.

Run from the repo root, after sketch_model.py and opzet_backgrounds.mjs:
    python project/tools/opzet_report.py            # writes project/pbip/GoodnightInn-opzet.pbip + .Report
    python project/tools/opzet_report.py --out DIR  # dry run elsewhere (validation outside project/pbip)

Source of truth:
  positions  project/design-prototypes/opzet-layout.json (the slot map; the HTML comp uses the same file)
  bindings   this file (one function per visual, measures from project/tools/sketch_model.py)
  decisions  project/project-state/active/01-, 02-, 04- and 05-doorlichting-nieuwe-opzet.md
Canvas 1920x1080; brand kit goodnight-inn-hanger (theme: project/deliverables/theme.json).

Two visible pages, both named after the contest's questions. P2 has two panel states
(shortlist / plan) swapped by display-only bookmarks bm_p2_shortlist / bm_p2_plan; the package
in focus lives in the disconnected PlanSelector slicer and the scenario in the Scenario slicer,
so a bookmark never changes either (fx-focus rules 1-2).

Shapes not yet exercised by the earlier Desktop-rendered sketches are marked VERIFY and listed
in 05-doorlichting-nieuwe-opzet.md as Desktop checks with a fallback each.
"""
import csv
import json
import math
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pbir_lib import (visual, textbox, card, slicer, write_report, vco, axis, legend, labels, series_colors, line_styles,  # noqa: E402
                      table_objects, proj_col, proj_mea, mref, filter_in, filter_measure_gt, filter_topn, sort_by_measure,
                      sort_by_column, b, num, integer, enum, text, color, mea, col, write_json, tag, PAGE_SCHEMA)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "project" / "pbip"
if len(sys.argv) > 2 and sys.argv[1] == "--out":
    OUT = Path(sys.argv[2])
NAME = "GoodnightInn-opzet"
# --plan-state: a throwaway copy (GoodnightInn-opzet-planstate) that opens in the P2 plan state, so a Desktop
# screenshot can check the state a bookmark normally reveals. Never commit it.
PLAN_STATE = "--plan-state" in sys.argv
if PLAN_STATE:
    NAME += "-planstate"
LAYOUT = json.loads((ROOT / "project" / "design-prototypes" / "opzet-layout.json").read_text(encoding="utf-8"))
THEME = json.loads((ROOT / "project" / "deliverables" / "theme.json").read_text(encoding="utf-8"))
THEME_FILE = "goodnight-inn-hanger.json"
THEME["name"] = THEME_FILE  # the registered file name (pbir_lib / pbir_detect convention)
BG = ROOT / "project" / "deliverables" / "backgrounds"

CANVAS, SURFACE, INK, INK2, HAIR = "#F5F3F0", "#FFFFFF", "#24192B", "#5B5163", "#E4DEE3"
ACCENT, GOOD, BAD, SLATE, PLUM = "#B5175F", "#1D5FA8", "#B45309", "#82798A", "#3E2C55"
DISPLAY, BODY = "Trebuchet MS", "Verdana"
FOOTER = "Source: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores weighted by survey responses. 2021 is a depressed base year."
PACKAGES_CSV = ROOT / "project" / "analysis" / "output" / "packages.csv"
# Kit type scale (brand.yaml scale_pt 28 / 20 / 13 / 11 / 10): textboxes in px (28 pt = 37 px, 13 pt = 17 px, 10 pt = 13 px),
# cards and visual objects in pt. Nothing below the 10 pt caption floor.
BRANDS = [("GI", "Goodnight Inn"), ("PS", "P&K Select"), ("MO", "Maison d'Or"), ("PP", "Pebble & Pine")]
WILD = {"data": [{"dataViewWildcard": {"matchingOption": 1}}]}

SLOT = {p["name"]: {v["name"]: v for v in p["visuals"]} for p in LAYOUT["pages"]}


def topn_filter(table, column, n, measure, name):
    """TopN as an In-condition over a subquery (the shape the semanticQuery schema allows; pbir_lib.filter_topn's
    'Top' condition does not validate against it)."""
    sel = {"Column": {"Expression": {"SourceRef": {"Source": "t"}}, "Property": column}}
    # Every SourceRef inside the subquery must name an alias declared in its own From; an Entity ref here crashes
    # Desktop's SemanticQueryRewriter.rewriteOrderBy ("Cannot read properties of undefined (reading 'accept')").
    sub = {"Version": 2, "From": [{"Name": "t", "Entity": table, "Type": 0}, {"Name": "m", "Entity": "_Measures", "Type": 0}],
           "Select": [{**sel, "Name": "field"}],
           "OrderBy": [{"Direction": 2, "Expression": {"Measure": {"Expression": {"SourceRef": {"Source": "m"}}, "Property": measure}}}], "Top": n}
    return {"name": name, "field": col(table, column), "type": "TopN",
            "filter": {"Version": 2, "From": [{"Name": "subquery", "Expression": {"Subquery": {"Query": sub}}, "Type": 2}, {"Name": "t", "Entity": table, "Type": 0}],
                       "Where": [{"Condition": {"In": {"Expressions": [sel], "Table": {"SourceRef": {"Source": "subquery"}}}}}]},
            "howCreated": "User"}


def fv(measure):
    """Field-value color: a measure that returns a hex string."""
    return {"solid": {"color": {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}}}}}


def mtext(measure):
    """Field-value text (VERIFY: title text bound to a measure)."""
    return {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}}}


def at(page, name):
    s = SLOT[page][name]
    return s["x"], s["y"], s["w"], s["h"], s["z"], s["tab"]


def state_of(page, name):
    """Slot state; visuals derived from a slot (the KPI cell's label and context, e.g. kpi_occ_label) share it."""
    base = name if name in SLOT[page] else name.rsplit("_", 1)[0]
    return SLOT[page].get(base, {}).get("state")  # card frames (z_card_*) are not slots: always visible


def tb(page, name, txt, font=BODY, size=13, colour=INK2, bold=False, align="left", alt=None):
    return textbox(name, *at(page, name), [[(txt, font, size, colour, bold)]], align=align, alt=alt)


def dyn(page, name, measure, size=10, colour=INK2, font=BODY, bold=False, alt=None):
    """A cardVisual that shows one text measure as copy (dynamic title or subtitle)."""
    v = card(name, *at(page, name), [measure], font, size, colour, alt=alt or measure.replace(" (text)", ""))
    if bold:
        v["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    return v


def chart(page, name, vtype, query, objects, alt, title=None, title_measure=None, filters=None, sort=None):
    vcos = vco(title=title or ("x" if title_measure else None), title_font=DISPLAY, title_size=13, title_color=INK, alt=alt, padding=0)
    if title_measure:
        vcos["title"][0]["properties"]["text"] = mtext(title_measure)
        vcos["title"][0]["properties"]["bold"] = b(True)
    return visual(name, vtype, *at(page, name), query=query, objects=objects, vcos=vcos, filters=filters, sort=sort)


# ====================================================================== P1 The Brand Review
P1 = "p1-brand-review"


def gi_filter():
    return filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_gi")


def kpi_cell(slot, label, value_measure, context_measure, alt):
    """One KPI of the band: a label, the value and one comparison (DC-051), stacked inside the slot (24 + 40 + 24 px)."""
    x, y, w, h, z, tab = at(P1, slot)
    lab = textbox(f"{slot}_label", x, y, w, 24, z, tab, [[(label, BODY, 13, INK2, False)]], alt=label)
    val = card(slot, x, y + 24, w, 40, z, tab + 1, [value_measure], DISPLAY, 28, INK, alt=alt)
    val["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    ctx = card(f"{slot}_ctx", x, y + 64, w, 24, z, tab + 2, [context_measure], BODY, 10, INK2, alt=context_measure.replace(" (text)", ""))
    return [lab, val, ctx]


def kicker(page, name, txt):
    return tb(page, name, txt, size=13, colour=ACCENT, bold=True, alt=txt)


def title(page, name, measure):
    return dyn(page, name, measure, size=13, colour=INK, font=DISPLAY, bold=True)


def p1_visuals():
    v = [tb(P1, "z_masthead", "THE BRAND REVIEW  ·  2021 TO 2025  ·  FOR THE BOARD OF PILLOW & KEY GROUP", align="right"),
         tb(P1, "z_headline", "Full rooms, a slipping margin: Goodnight Inn pays the middleman and is losing its guests.", font=DISPLAY, size=37, colour=INK, bold=True,
            alt="Page headline: Full rooms, a slipping margin: Goodnight Inn pays the middleman and is losing its guests."),
         tb(P1, "c_subtitle", "Goodnight Inn in 2025, against the three other Pillow & Key Group brands.", size=15)]

    # the KPI band: four cells in one card (the hairline rules are in the page background)
    v += kpi_cell("kpi_occ", "Occupancy", "KPI Occupancy GI", "KPI Occupancy Context (text)", "Goodnight Inn occupancy 2025")
    v += kpi_cell("kpi_margin", "Operating margin after commissions", "KPI Margin after GI", "KPI Margin after Context (text)", "Goodnight Inn operating margin after commissions 2025")
    v += kpi_cell("kpi_ota", "Room revenue booked through online agencies", "KPI OTA GI", "KPI OTA Context (text)", "Share of Goodnight Inn room revenue booked through online agencies 2025")
    v += kpi_cell("kpi_nps", "Net promoter score", "KPI NPS GI", "KPI NPS Context (text)", "Goodnight Inn net promoter score 2025")

    years = filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")

    # F1 the margin: before vs after commissions, Goodnight Inn only; the gap between the lines is the channels' take
    v += [kicker(P1, "c_f1_kicker", "F1  ·  THE MARGIN"), title(P1, "c_f1_title", "F1 Title (text)")]
    ms = ["Trend Margin before GI", "Trend Margin after GI"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(ms[0], "Before commissions"), proj_mea(ms[1], "After commissions")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2), "valueAxis": axis(BODY, 10, INK2, gridlines=True, grid_color=HAIR, start=0.25, end=0.5, extra={"labelPrecision": integer(0)}),
            "legend": legend(True, BODY, 10, INK2, "Top"),
            "dataPoint": series_colors({mref(ms[0]): SLATE, mref(ms[1]): ACCENT}), "lineStyles": line_styles({mref(ms[0]): 2, mref(ms[1]): 3})}
    v.append(chart(P1, "ch_f1_margin", "lineChart", q, objs, "Line chart 2021 to 2025 of Goodnight Inn's operating margin before and after commissions; the gap between the two lines widens every year",
                   filters=[years]))
    v.append(dyn(P1, "c_f1_note", "F1 Note (text)", size=10))

    # F2 the middleman: OTA share for the four brands, and the folio (one 2025 room night by channel)
    v += [kicker(P1, "c_f2_kicker", "F2  ·  THE MIDDLEMAN"), title(P1, "c_f2_title", "F2 Title (text)")]
    ms = [f"Trend OTA {c}" for c, _ in BRANDS]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m, nm) for m, (_, nm) in zip(ms, BRANDS)]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2), "valueAxis": axis(BODY, 10, INK2, gridlines=True, grid_color=HAIR, extra={"labelPrecision": integer(0)}),
            "legend": legend(True, BODY, 10, INK2, "Right"),
            "dataPoint": series_colors({mref(ms[0]): ACCENT, **{mref(m): SLATE for m in ms[1:]}}),
            "lineStyles": line_styles({mref(ms[0]): 3, **{mref(m): 1.5 for m in ms[1:]}})}
    v.append(chart(P1, "ch_f2_ota", "lineChart", q, objs, "Line chart 2021 to 2025 of the share of room revenue booked through online travel agencies: Goodnight Inn against the three sister brands",
                   filters=[filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")]))
    proj = [proj_col("FolioLine", "Line", display="One room night, 2025"), proj_mea("Folio OTA Guest", "Via an online agency"), proj_mea("Folio Direct Guest", "Direct, web and app")]
    colfmt = [{"properties": {"alignment": enum("Right")}, "selector": {"metadata": mref(m)}} for m in ("Folio OTA Guest", "Folio Direct Guest")]
    objs = table_objects(BODY, 10, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=4, header_size=10, column_formatting=colfmt)
    v.append(visual("tbl_f2_folio", "tableEx", *at(P1, "tbl_f2_folio"), query={"Values": {"projections": proj}}, objects=objs, filters=[gi_filter()],
                    sort=sort_by_column("FolioLine", "Line"),
                    vcos=vco(alt="The folio: one Goodnight Inn room night in 2025. Via an online agency the guest pays $109.31, commission and fees take $19.68 and the inn keeps $89.64; booked direct the guest pays $111.56 and the inn keeps $107.09", padding=0)))
    v.append(dyn(P1, "c_f2_note", "F2 Note (text)", size=10))

    # F3 the fading welcome: NPS 2025 by years since the last renovation (dated hotels only)
    v += [kicker(P1, "c_f3_kicker", "F3  ·  THE FADING WELCOME"), title(P1, "c_f3_title", "F3 Title (text)")]
    q = {"Category": {"projections": [proj_col("Hotels", "Renovation Age Label", display="Years since the last renovation")]}, "Y": {"projections": [proj_mea("NPS 2025 (signed)", "NPS 2025")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK), "valueAxis": axis(BODY, 9, INK2, show=False, gridlines=False),
            "dataPoint": [{"properties": {"fill": fv("Age Band Color")}, "selector": WILD}], "labels": labels(True, BODY, 12, INK), "legend": legend(False)}
    v.append(chart(P1, "ch_f3_age", "clusteredColumnChart", q, objs, "Column chart of Goodnight Inn's 2025 net promoter score by years since the last renovation: 5 years or less, 6 to 9 years, 10 years or more; only the oldest group is negative",
                   filters=[gi_filter(), filter_in("Hotels", "Renovation Age Sort", [1, 2, 3], "flt_dated")], sort=sort_by_column("Hotels", "Renovation Age Label")))
    v.append(dyn(P1, "c_f3_note", "F3 Note (text)", size=10))

    # F4 where we are full
    v += [kicker(P1, "c_f4_kicker", "F4  ·  WHERE WE ARE FULL"), title(P1, "c_f4_title", "F4 Title (text)")]
    v.append(card("c_f4_types", *at(P1, "c_f4_types"), ["Occupancy Airport GI", "Occupancy City GI", "Occupancy Highway GI"], DISPLAY, 21, INK, BODY, 10, INK2,
                  labels=["Airport hotels", "City hotels", "Highway hotels"], alt="Goodnight Inn occupancy 2025 by location type: airport, city and highway hotels"))
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Occupancy % 2025", "Occupancy 2025")]}}
    # axis from zero (never truncate a bar axis, CP-066); end 1.1 leaves room for the labels above the 90 % bars
    objs = {"categoryAxis": axis(BODY, 10, INK), "valueAxis": axis(BODY, 9, INK2, show=False, gridlines=False, start=0, end=1.1),
            "dataPoint": [{"properties": {"fill": fv("Hotel Bar Color")}, "selector": WILD}], "labels": labels(True, BODY, 10, INK, position="OutsideEnd"), "legend": legend(False)}
    v.append(chart(P1, "ch_f4_fullest", "clusteredColumnChart", q, objs, "Column chart of the seven Goodnight Inn hotels with the highest 2025 occupancy; five are airport hotels, in raspberry",
                   filters=[gi_filter(), topn_filter("Hotels", "Hotel Short Name", 7, "Occupancy % 2025", "flt_top7")], sort=sort_by_measure("Occupancy % 2025")))
    v.append(tb(P1, "z_footer", FOOTER))
    return v


# ====================================================================== P2 The Investment Strategy
P2 = "p2-investment-strategy"


def nums_card(name, measures, labs, alt):
    return card(name, *at(P2, name), measures, BODY, 16, INK, BODY, 10, INK2, labels=labs, alt=alt)


def button(name, label, bookmark, filled, alt):
    """VERIFY: actionButton text/fill object shapes; the visualLink shape is from the 2.6.0 visual schema."""
    # Shape copied from a Desktop-rendered button (hp-world-champs btn_nav_1): 'show' sits WITHOUT a selector, the
    # state formatting under {"id": "default"}; with 'show' inside the selector the text did not render (7 Nov).
    objs = {"icon": [{"properties": {"shapeType": text("blank")}, "selector": {"id": "default"}}],
            "text": [{"properties": {"show": b(True)}},
                     {"properties": {"text": text(label), "fontFamily": text(BODY), "fontSize": num(11), "fontColor": color(SURFACE if filled else INK), "bold": b(True)}, "selector": {"id": "default"}}],
            "fill": [{"properties": {"show": b(True)}},
                     {"properties": {"fillColor": color(ACCENT if filled else SURFACE), "transparency": num(0)}, "selector": {"id": "default"}}],
            # no roundEdge: not in the actionButton catalog, and Desktop drops it on save (seen 7 Nov)
            "outline": [{"properties": {"show": b(not filled)}},
                        {"properties": {"lineColor": color(INK2), "weight": num(1)}, "selector": {"id": "default"}}]}
    vcos = vco(alt=alt, padding=0)
    vcos["visualLink"] = [{"properties": {"show": b(True), "type": enum("Bookmark"), "bookmark": text(bookmark)}}]
    return visual(name, "actionButton", *at(P2, name), objects=objs, vcos=vcos)


def npv_axis_range():
    """One fixed NPV axis for all three scenarios (DC-034): the packages' extremes across Low, Expected and High,
    rounded out to whole $10M, so the scenario switch never rescales the picture. Same rule as the comp."""
    with PACKAGES_CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    vals = [float(r[k]) for r in rows for k in ("NPV_Low", "NPV_Expected", "NPV_High")]
    return math.floor(min(vals) / 1e7) * 1e7, math.ceil(max(vals) / 1e7) * 1e7


def p2_visuals():
    y0, y1 = npv_axis_range()
    v = [tb(P2, "z_masthead2", "THE INVESTMENT STRATEGY  ·  2027 TO 2032  ·  GOODNIGHT INN BUDGET $60.0M", align="right"),
         dyn(P2, "z_headline2", "Headline P2 (text)", size=28, colour=INK, font=DISPLAY, bold=True, alt="Page headline: the recommendation"),
         dyn(P2, "c_subtitle2", "Subtitle P2 (text)", size=11),
         title(P2, "c_scatter_title", "Scatter Title (text)"),
         tb(P2, "c_scatter_sub", "Each dot is a package the rules allow; above the line it pays back by 2032. Raspberry: our recommendation A. Plum-black: B and C.")]
    q = {"Category": {"projections": [proj_col("Package", "PackageID")]}, "X": {"projections": [proj_mea("Package Capex", "Capex")]},
         "Y": {"projections": [proj_mea("Package NPV (sel)", "NPV through 2032")]}, "Size": {"projections": [proj_mea("Package Point Size", "Marker size")]}}
    # units=1 (none): the measures' formats already print $M; auto units scaled a second time ("$0MM", 7 Nov)
    objs = {"categoryAxis": axis(BODY, 10, INK2, title=True, start=0, end=60000000, units=1, extra={"titleText": text("Capex of the package, $M"), "titleFontFamily": text(BODY), "titleFontSize": num(10), "titleColor": color(INK2)}),
            "valueAxis": axis(BODY, 10, INK2, title=True, gridlines=True, grid_color=HAIR, start=y0, end=y1, units=1,
                              extra={"titleText": text("NPV through 2032, $M"), "titleFontFamily": text(BODY), "titleFontSize": num(10), "titleColor": color(INK2)}),
            "dataPoint": [{"properties": {"fill": fv("Package Point Color")}, "selector": WILD}],
            # smaller markers: at -25 the 456 plum-slate dots read as one heavy mass in Desktop (7 Nov)
            "bubbles": [{"properties": {"bubbleSize": integer(-40)}}], "legend": legend(False), "categoryLabels": [{"properties": {"show": b(False)}}],
            # the zero line (rendered in Desktop 7 Nov); its meaning sits in the subtitle, because the line's own label sat
            # under the dots of the best packages
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "style": enum("solid"), "position": enum("front"),
                                                    "displayName": text("Pays back by 2032 above this line"), "dataLabelShow": b(False)}, "selector": {"id": "1"}}]}
    v.append(visual("hero_packages", "scatterChart", *at(P2, "hero_packages"), query=q, objects=objs,
                    vcos=vco(alt="Scatter of the 456 valid investment packages: capex on the horizontal axis, NPV through 2032 in the selected scenario on the vertical axis; the recommendation, package A, is the large raspberry dot, the alternatives B and C are plum-black", padding=0)))
    v.append(slicer("sl_scenario", *at(P2, "sl_scenario"), "Scenario", "Scenario", "Scenario", BODY, INK, INK2, SURFACE, ACCENT, single=True, horizontal=True, selected=["Expected"],
                    alt="Scenario: Low, Expected or High; every number on this page follows it", size=10))
    v.append(slicer("sl_package", *at(P2, "sl_package"), "PlanSelector", "Label", "Package in focus", BODY, INK, INK2, SURFACE, ACCENT, mode="Dropdown", single=True,
                    selected=["A · Our recommendation"], alt="Package in focus: the recommendation A, the alternatives B and C, or any valid package", size=10))

    # state: shortlist = the recommendation and its alternatives (no tiles: whitespace groups, nothing sits on top of content)
    v.append(tb(P2, "c_rec_title", "Our recommendation: package A", font=DISPLAY, size=17, colour=INK, bold=True))
    v.append(dyn(P2, "c_rec_mix", "Rec Mix (text)", size=11, colour=INK))
    v.append(card("c_rec_nums", *at(P2, "c_rec_nums"), ["Rec Capex", "Rec NPV (sel)", "Rec Range (text)", "Rec Run-rate (sel)"], DISPLAY, 21, INK, BODY, 10, INK2,
                  labels=["capex", "NPV through 2032", "NPV, Low to High, $M", "profit a year by 2032"],
                  alt="Package A in numbers: capex, NPV through 2032 in the selected scenario, the NPV range from Low to High, and the 2032 run-rate"))
    v.append(dyn(P2, "c_rec_answers", "Rec Answers (text)", size=10))
    v.append(tb(P2, "c_alt_title", "Considered, not recommended", font=DISPLAY, size=17, colour=INK, bold=True))
    v.append(dyn(P2, "c_alt_b", "Alt B (text)", size=10, colour=INK))
    v.append(dyn(P2, "c_alt_c", "Alt C (text)", size=10, colour=INK))
    v.append(dyn(P2, "c_not_funded", "Not Funded (text)", size=10, colour=INK))
    v.append(dyn(P2, "c_uncertainty", "Uncertainty (text)", size=10))
    v.append(button("btn_open_plan", "Open the plan for the package in focus  →", "bm_p2_plan", True, "Button: open the plan for the package in focus"))

    # state: plan (hidden by default)
    v.append(dyn(P2, "c_plan_title", "Plan Title (text)", size=13, colour=INK, font=DISPLAY, bold=True))
    q = {"Category": {"projections": [proj_col("InvestmentProjects", "Short Name")]}, "Y": {"projections": [proj_mea("Focus Project NPV (sel)", "NPV through 2032")]}}
    # units=1 on axis and labels: the measure format already prints $M ("$0MM" in Desktop with auto units, 7 Nov)
    objs = {"categoryAxis": axis(BODY, 10, INK2, gridlines=None), "valueAxis": axis(BODY, 10, INK2, gridlines=False, units=1),
            "sentimentColors": [{"properties": {"increaseFill": color(GOOD), "decreaseFill": color(BAD), "totalFill": color(INK), "otherFill": color(SLATE)}}],
            "labels": labels(True, BODY, 10, INK, units=1), "legend": legend(False)}
    v.append(chart(P2, "ch_plan_waterfall", "waterfallChart", q, objs, "Waterfall of each initiative's NPV contribution through 2032 to the package in focus, ending in the package total",
                   title="Where the NPV comes from, $M through 2032", filters=[filter_measure_gt("Focus Project Flag", 0, "flt_focus_wf")]))
    # all ten initiatives, funded ones first, each with the kit's state chip (brand-guide section 6): the chip is the
    # decorative carrier (shape + color), the Status word the accessible one
    proj = [proj_mea("Initiative Chip", " "), proj_mea("Initiative Status (text)", "Status"), proj_col("InvestmentProjects", "Short Name", display="Initiative"),
            proj_col("InvestmentProjects", "Answers Finding", display="Answers"), proj_mea("Initiative Capex", "Capex"), proj_mea("Live (text)", "Live"),
            proj_mea("Initiative Run-rate (sel)", "Run-rate"), proj_mea("Initiative NPV (sel)", "NPV"), proj_mea("Initiative Guest Effect (text)", "Guest pts")]
    colfmt = [{"properties": {"alignment": enum("Right")}, "selector": {"metadata": mref(m)}} for m in ("Initiative Capex", "Live (text)", "Initiative Run-rate (sel)", "Initiative NPV (sel)", "Initiative Guest Effect (text)")]
    extra = [{"properties": {"fontColorPrimary": fv("Initiative Status Color")}, "selector": {**WILD, "metadata": mref("Initiative Status (text)")}}]
    objs = table_objects(BODY, 10, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=4, header_size=10, extra_values=extra, column_formatting=colfmt)
    # chip size: grid.imageHeight / imageWidth (powerbi-report-author catalog); the default made rows so tall that only
    # four of ten initiatives showed (7 Nov). 28 x 20 keeps the chip's 40:28 shape.
    objs["grid"][0]["properties"]["imageHeight"] = num(20)
    objs["grid"][0]["properties"]["imageWidth"] = num(28)
    v.append(visual("tbl_plan_initiatives", "tableEx", *at(P2, "tbl_plan_initiatives"), query={"Values": {"projections": proj}}, objects=objs,
                    sort=sort_by_measure("Initiative Status (text)", desc=False),
                    vcos=vco(alt="Table of all ten Goodnight Inn initiatives, funded ones first: status in the package in focus, the page-1 finding each answers, capex, go-live month, 2032 run-rate, NPV and the dataset guest-score effect", padding=0)))
    ms = ["Focus Cumulative Net (Low)", "Focus Cumulative Net (Expected)", "Focus Cumulative Net (High)"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(ms[0], "Low"), proj_mea(ms[1], "Expected"), proj_mea(ms[2], "High")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2), "valueAxis": axis(BODY, 10, INK2, gridlines=True, grid_color=HAIR, units=1), "legend": legend(False),
            "dataPoint": series_colors({mref(m): ACCENT for m in ms}), "lineStyles": line_styles({mref(ms[0]): 1, mref(ms[1]): 2, mref(ms[2]): 1})}
    v.append(chart(P2, "ch_plan_cumulative", "lineChart", q, objs, "Line chart of the cumulative net impact of the package in focus 2027 to 2032 in the Low, Expected and High scenarios",
                   title="Cumulative net impact, $M  ·  Low to High", filters=[filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon2")]))
    v.append(card("c_plan_ops", *at(P2, "c_plan_ops"), ["Focus Rooms Added", "Focus Rooms Refreshed", "Focus Hotels Rated"], BODY, 14, INK, BODY, 10, INK2,
                  labels=["rooms added", "rooms refreshed", "hotels, score up"], alt="Operational impact of the package in focus: rooms added, rooms refreshed, hotels with a dataset guest-score effect"))
    v.append(dyn(P2, "c_plan_risk", "Plan Risk (text)", size=10))
    v.append(button("btn_back", "←  Back to the recommendation", "bm_p2_shortlist", False, "Button: back to the recommendation and its alternatives"))
    v.append(dyn(P2, "z_footer2", "Footer P2 (text)", size=10))
    return v


# ====================================================================== pages, bookmarks, resources
def card_frames(page_name):
    """The layout's cards as empty textboxes with a Sheet fill and a Seam hairline (radius 12), drawn UNDER the content
    (z 100+) and last in tab order. Being visuals, they scale with the content: a page-background PNG did not when
    Desktop scaled the canvas non-uniformly (7 Nov). The fill and border shapes are the earlier tile()'s, which
    Desktop rendered; only the z-order changed."""
    pg = next(p for p in LAYOUT["pages"] if p["name"] == page_name)
    out = []
    for i, c in enumerate(pg["cards"]):
        v = textbox(f"z_card_{c['id']}", c["x"], c["y"], c["w"], c["h"], 100 + i, 9500 + i, [[("", BODY, 10, INK2, False)]], alt="Decorative card background")
        v["visual"]["visualContainerObjects"]["background"] = [{"properties": {"show": b(True), "color": color(SURFACE), "transparency": num(0)}}]
        v["visual"]["visualContainerObjects"]["border"] = [{"properties": {"show": b(True), "color": color(HAIR), "radius": num(12), "width": num(1)}}]
        out.append(v)
    return out


def logo(page_name):
    """The lockup as an image visual (asleep on P1, awake on P2; PNGs from opzet_backgrounds.mjs). Object shape from
    the powerbi-report-author catalog (image.sourceFile name/url/scaling, imageScaling.imageScalingType)."""
    pg = next(p for p in LAYOUT["pages"] if p["name"] == page_name)
    f = f"lockup-{page_name}.png"
    objs = {"image": [{"properties": {"sourceType": text("image"), "sourceFile": {"image": {
                "name": text(f), "url": {"expr": {"ResourcePackageItem": {"PackageName": "RegisteredResources", "PackageType": 1, "ItemName": f}}}, "scaling": text("Fit")}}}}],
            "imageScaling": [{"properties": {"imageScalingType": text("Fit")}}]}
    L = pg["logo"]
    return visual("z_logo", "image", L["x"], L["y"], L["w"], L["h"], 1003, 9050, objects=objs, vcos=vco(alt="Goodnight Inn logo", padding=0))


def no_card_fill(visuals):
    """cardVisual draws a white fill of its own (fillCustom, id 'default'); it showed as white boxes on the canvas in
    Desktop (7 Nov). Off everywhere: the cards' surfaces come from the card frames."""
    # Both layers closed, each with show=false AND 100 % transparency: with show=false alone the cards on the canvas
    # (P2 headline, subtitle, footer) still drew white in Desktop, under a theme that turns every background on.
    for v in visuals:
        if v["visual"]["visualType"] == "cardVisual":
            v["visual"]["objects"]["fillCustom"] = [{"properties": {"show": b(False), "transparency": num(100)}, "selector": {"id": "default"}}]
            v["visual"]["visualContainerObjects"]["background"] = [{"properties": {"show": b(False), "transparency": num(100)}}]
    return visuals


def page(name, display, visuals, filters=None):
    # colour only: furniture (cards, logo) is drawn by visuals so it scales with the content on any viewport
    p = {"$schema": PAGE_SCHEMA, "name": name, "displayName": display, "displayOption": "FitToPage", "height": LAYOUT["canvas"]["h"], "width": LAYOUT["canvas"]["w"],
         "objects": {"background": [{"properties": {"color": color(CANVAS), "transparency": num(0)}}]}}
    if filters:
        p["filterConfig"] = {"filters": filters}
    for vis in visuals:
        if state_of(name, vis["name"]) == ("shortlist" if PLAN_STATE else "plan"):
            vis["isHidden"] = True
    return p, visuals


BOOKMARK_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/2.1.0/schema.json"
BOOKMARKS_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmarksMetadata/1.0.0/schema.json"


def bookmark(name, display, show_state, visuals):
    targets = [v for v in visuals if state_of(P2, v["name"]) in ("shortlist", "plan") or v["name"].startswith("z_tile_")]
    containers = {}
    for v in targets:
        st = "shortlist" if v["name"].startswith("z_tile_") else state_of(P2, v["name"])
        sv = {"visualType": v["visual"]["visualType"]}
        if st != show_state:
            sv["display"] = {"mode": "hidden"}
        containers[v["name"]] = {"singleVisual": sv}
    return {"$schema": BOOKMARK_SCHEMA, "displayName": display, "name": name,
            "options": {"applyOnlyToTargetVisuals": True, "targetVisualNames": [v["name"] for v in targets], "suppressActiveSection": True, "suppressData": True},
            "explorationState": {"version": "1.3", "activeSection": P2, "sections": {P2: {"visualContainers": containers}}}}


def main():
    v1 = no_card_fill(card_frames(P1) + [logo(P1)] + p1_visuals())
    v2 = no_card_fill(card_frames(P2) + [logo(P2)] + p2_visuals())
    pages = [page(P1, "The Brand Review", v1),
             page(P2, "The Investment Strategy", v2,
                  filters=[filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_page_projects"), filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_page_brand")])]
    rep = write_report(OUT, NAME, "Goodnight Inn · opzet", pages, THEME, THEME_FILE)
    res = rep / "StaticResources" / "RegisteredResources"
    for pg in ("p1-brand-review", "p2-investment-strategy"):
        shutil.copyfile(BG / f"lockup-{pg}.png", res / f"lockup-{pg}.png")
    rj = rep / "definition" / "report.json"
    report = json.loads(rj.read_text(encoding="utf-8"))
    for pk in report["resourcePackages"]:
        if pk["name"] == "RegisteredResources":
            pk["items"] += [{"name": f"lockup-{pg}.png", "path": f"lockup-{pg}.png", "type": "Image"} for pg in ("p1-brand-review", "p2-investment-strategy")]
    write_json(rj, report)
    bm = rep / "definition" / "bookmarks"
    write_json(bm / "bm_p2_shortlist.bookmark.json", bookmark("bm_p2_shortlist", "P2 Shortlist", "shortlist", v2))
    write_json(bm / "bm_p2_plan.bookmark.json", bookmark("bm_p2_plan", "P2 Plan", "plan", v2))
    write_json(bm / "bookmarks.json", {"$schema": BOOKMARKS_SCHEMA, "items": [{"name": "bm_p2_shortlist"}, {"name": "bm_p2_plan"}]})
    n1, n2 = len(v1), len(v2)
    core = sum(1 for v in v1 + v2 if v["visual"]["visualType"] in ("tableEx", "pivotTable", "clusteredBarChart", "clusteredColumnChart", "lineChart", "scatterChart", "waterfallChart"))
    print(f"report written: {rep}  P1 {n1} visuals, P2 {n2} visuals ({sum(1 for v in v2 if v.get('isHidden'))} hidden in the plan state), {core} core chart/table visuals")


if __name__ == "__main__":
    main()
