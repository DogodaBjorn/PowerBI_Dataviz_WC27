"""Writes the report set-up (opzet) as a PBIP report on the shared model. v2 of 2026-11-07: the D1 briefing,
stripped (06-d1-briefing-opzet.md): P1 = headline, four benchmarked KPIs, findings F1-F3 with one chart each,
F4 where we are full; P2 = the package scatter with the focus swap and one recommendation (A) plus alternatives.

Run from the repo root, after sketch_model.py and brand_canvas_v3.py (plan 11):
    python project/tools/opzet_report.py            # writes project/pbip/GoodnightInn-opzet.pbip + .Report
    python project/tools/opzet_report.py --out DIR  # dry run elsewhere (validation outside project/pbip)

Source of truth:
  positions  project/design-prototypes/opzet-layout.json (the slot map; the HTML comp uses the same file)
  bindings   this file (one function per visual, measures from project/tools/sketch_model.py)
  decisions  project/project-state/active/01-, 02-, 04- and 05-doorlichting-nieuwe-opzet.md
Canvas 1920x1080; brand kit goodnight-inn-wakeup 3.1, night header with the night-glow canvas (plans 10 and 11;
theme: project/deliverables/theme.json, canvas: project/tools/brand_canvas_v3.py).

Two visible pages, both named after the contest's questions. P2 has two panel states
(shortlist / plan) swapped by display-only bookmarks bm_p2_shortlist / bm_p2_plan; the package
in focus lives in the disconnected PlanSelector slicer and the scenario in the Scenario slicer,
so a bookmark never changes either (fx-focus rules 1-2).

Shapes not yet exercised by the earlier Desktop-rendered sketches are marked VERIFY and listed
in 05-doorlichting-nieuwe-opzet.md as Desktop checks with a fallback each.
"""
import copy
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
THEME_FILE = "goodnight-inn-wakeup.json"
THEME["name"] = THEME_FILE  # the registered file name (pbir_lib / pbir_detect convention)
BG = ROOT / "project" / "deliverables" / "backgrounds"

# Kit goodnight-inn-wakeup 3.1 (plan 10 D1, plan 11): Goodnight Inn is Coffee Blue, the sister brands Warm Grey,
# Tangerine only marks a signal. ACCENT is the text cut (Deep Coffee, 6.2:1 on white, white on it 6.2:1);
# ACCENT_MARK the series and marks (Coffee Blue, 3.7:1 on white: enough for a mark, not for small text).
CANVAS, SURFACE, INK, INK2, HAIR = "#F3F1EA", "#FFFFFF", "#12233D", "#4B5466", "#E3DFD3"
ACCENT, ACCENT_MARK, GOOD, BAD, SLATE = "#1763A8", "#2589D8", "#1763A8", "#A63F0E", "#8E897D"
SIGNAL_MARK = "#E05A22"  # Tangerine: the Low case, decreases (never a brand or series identity)
TINT = "#EAF2FB"  # Ice, the kit's accent tint (sequential step 1)
# Text on the Night header zone (plan 10 D3): headline, masthead/subtitle, eyebrow. Contrast on the lightest pixel
# of the night-glow zone is checked by project/tools/a11y_check.py from backgrounds/zone-samples.json.
ZONE_TEXT, ZONE_MUTED, ZONE_EYEBROW = "#F7F5EE", "#C9D0DC", "#A9CDF0"
# The font stacks Desktop itself writes for Segoe UI: wf_segoe-ui_* are the Power BI service's web fonts, so a
# browser without Segoe UI (a Mac under Publish-to-Web) still gets it; Arial as the last named fallback (kit 3.1).
DISPLAY = "'Segoe UI Semibold', wf_segoe-ui_semibold, helvetica, arial, sans-serif"
BODY = "'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif"
FOOTER = ("Source: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores weighted by survey responses. 2021 is a depressed base year. "
          # plan 09 R4 (Profit Ability 2; Keiningham et al. 2007, see CREDITS.md): what is left out on purpose
          "Deliberately not shown: impressions, likes, and NPS as a growth measure; effectiveness research does not support them.")
PACKAGES_CSV = ROOT / "project" / "analysis" / "output" / "packages.csv"
KIT = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
# The brand row (plan 11): the 3.1 lockup on the Night zone and an eyebrow in the former pay-off slot. The door
# vignettes and pay-off lines of the hanger kit (08-verbeterplan V5) are gone: kit 3.1 allows no faces or
# illustrations; the faded zone hanger (plan 10 D2b) is the one piece of brand theatre.
EYEBROW = {"p1-brand-review": "01  THE BRAND REVIEW", "p2-investment-strategy": "02  THE INVESTMENT STRATEGY"}
LOCKUP = "gi-lockup-reversed@2x.png"
# Kit type scale (brand.yaml 3.1 scale_pt 30 / 20 / 14 / 12 / 12): textboxes in px, cards and visual objects in pt.
# Floor 12 pt (16 px at 1920) for notes, axes, tables, slicers and tooltips alike (kit typography.floor; plan 11
# replaces the 11 pt of 08-verbeterplan R4). Segoe UI sets narrower than the Verdana it replaces, so 12 pt Segoe
# takes about the width of 11 pt Verdana. S = small text in pt, SPX the same in px.
S = 12
SPX = 16
TITLE_PT = 14  # card titles (kit scale step 3)
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


def bind_alt(v, measure):
    """Alt text from a measure (plan 11): visualContainerObjects.general.altText takes any expression
    (visualConfiguration 2.6.0), so the text a screen reader gets is computed by the model and never drifts."""
    v["visual"].setdefault("visualContainerObjects", {})["general"] = [{"properties": {"altText": mtext(measure)}}]
    return v


def decorative(v, i):
    """Out of the tab order and unannounced: Desktop stores 'hidden from tab order' as a negative tabOrder (seen in
    Desktop-saved PBIR, plan 11 section 4); no alt text, so a screen reader that reaches it anyway reads nothing."""
    v["position"]["tabOrder"] = -1000 - i
    v["visual"].get("visualContainerObjects", {}).pop("general", None)
    return v


def tb(page, name, txt, font=BODY, size=SPX, colour=INK2, bold=False, align="left", alt=None):
    # a static text box reads its own words unless told otherwise (plan 11: eight text boxes had no alt text)
    return textbox(name, *at(page, name), [[(txt, font, size, colour, bold)]], align=align, alt=alt or txt)


def dyn(page, name, measure, size=S, colour=INK2, font=BODY, bold=False, align="left", alt_measure=None):
    """A cardVisual that shows one text measure as copy (dynamic title or subtitle). Its alt text is the same measure
    (or alt_measure), so a screen reader hears the sentence on the canvas, not the measure's name (plan 11)."""
    v = card(name, *at(page, name), [measure], font, size, colour, align=align)
    if bold:
        v["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    return bind_alt(v, alt_measure or measure)


def chart(page, name, vtype, query, objects, alt, title=None, title_measure=None, filters=None, sort=None, alt_measure=None):
    vcos = vco(title=title or ("x" if title_measure else None), title_font=DISPLAY, title_size=TITLE_PT, title_color=INK, alt=alt, padding=0)
    if title_measure:
        vcos["title"][0]["properties"]["text"] = mtext(title_measure)
        vcos["title"][0]["properties"]["bold"] = b(True)
    v = visual(name, vtype, *at(page, name), query=query, objects=objects, vcos=vcos, filters=filters, sort=sort)
    return bind_alt(v, alt_measure) if alt_measure else v


# ====================================================================== P1 The Brand Review
P1 = "p1-brand-review"


def gi_filter():
    return filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_gi")


def kpi_cell(slot, label, value_measure, context_measure, alt_measure):
    """One KPI of the band: a label, the value and one comparison (DC-051), stacked inside the slot (24 + 40 + 24 px).
    One tab stop per KPI (plan 11): the value reads label, value and comparison aloud (Alt KPI ... (text)); the label
    and the context line are the same words on the canvas, so they leave the tab order."""
    x, y, w, h, z, tab = at(P1, slot)
    lab = textbox(f"{slot}_label", x, y, w, 24, z, tab, [[(label, BODY, SPX, INK2, False)]])
    val = card(slot, x, y + 24, w, 48, z, tab + 1, [value_measure], DISPLAY, 28, INK)
    val["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    ctx = card(f"{slot}_ctx", x, y + 72, w, 24, z, tab + 2, [context_measure], BODY, S, INK2)
    return [decorative(lab, 100 + tab), bind_alt(val, alt_measure), decorative(ctx, 200 + tab)]


_KICK = [0]


def kicker(page, name, txt):
    # the kit's eyebrow on a white card: Deep Coffee capitals (6.2:1), at the 12 pt floor (was 13 px). Out of the tab
    # order: the title after it reads the kicker's words first (Alt F# Title (text); pass-3 review: 27 stops on P1)
    _KICK[0] += 1
    return decorative(tb(page, name, txt, font=DISPLAY, size=SPX, colour=ACCENT), 600 + _KICK[0])


def title(page, name, measure, alt_measure=None):
    return dyn(page, name, measure, size=TITLE_PT, colour=INK, font=DISPLAY, alt_measure=alt_measure)


def p1_visuals():
    # headline and subtitle as cards, like P2's, so the two headers sit on one grid (REVIEW p2: P2's sat 2-7 px lower)
    # on the night zone (plan 10 D3): masthead and subtitle in ZONE_MUTED (10.2:1 on Night), the headline in ZONE_TEXT
    v = [tb(P1, "z_masthead", "2021 TO 2025  ·  FOR THE BOARD OF PILLOW & KEY GROUP", size=SPX, colour=ZONE_MUTED, align="right",
            alt="2021 to 2025, for the Board of Pillow & Key Group"),
         dyn(P1, "z_headline", "Headline P1 (text)", size=28, colour=ZONE_TEXT, font=DISPLAY),
         dyn(P1, "c_subtitle", "Subtitle P1 Briefing (text)", size=S, colour=ZONE_MUTED)]

    # the KPI band: four cells in one card; values are text measures, one formatter with the context line (REVIEW M7)
    v += kpi_cell("kpi_occ", "Occupancy", "KPI Occupancy GI (text)", "KPI Occupancy Context (text)", "Alt KPI Occupancy (text)")
    v += kpi_cell("kpi_margin", "Operating margin after commissions", "KPI Margin after GI (text)", "KPI Margin after Context (text)", "Alt KPI Margin after (text)")
    v += kpi_cell("kpi_ota", "Room revenue booked through online agencies", "KPI OTA GI (text)", "KPI OTA Context (text)", "Alt KPI OTA (text)")
    # plan 09 R2: NPS as a guest-quality signal, not the brand's one number (Keiningham et al. 2007; CREDITS.md)
    v += kpi_cell("kpi_nps", "Guest quality: net promoter score", "KPI NPS GI (text)", "KPI NPS Context (text)", "Alt KPI NPS (text)")

    years = filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")

    # F1 the margin: before vs after commissions, Goodnight Inn only; the gap between the lines is the channels' take
    v += [kicker(P1, "c_f1_kicker", "F1  ·  THE MARGIN"), title(P1, "c_f1_title", "F1 Title (text)", "Alt F1 Title (text)")]
    ms = ["Trend Margin before GI", "Trend Margin after GI"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(ms[0], "Before commissions"), proj_mea(ms[1], "After commissions")]}}
    # 30 % to 50 %: from 25 % an empty band sat between the lowest gridline and the years (REVIEW p4)
    objs = {"categoryAxis": axis(BODY, S, INK2), "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, start=0.3, end=0.5, extra={"labelPrecision": integer(0)}),
            # the lines named at their ends in Dusk, as on F2 (pass-3 review: a legend of a grey and a blue dot was colour
            # only, 1.07:1 between them)
            "legend": legend(False),
            "seriesLabels": [{"properties": {"show": b(True), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2), "textSize": num(S), "seriesFontFamily": text(BODY)}}],
            "dataPoint": series_colors({mref(ms[0]): SLATE, mref(ms[1]): ACCENT_MARK}), "lineStyles": line_styles({mref(ms[0]): 2, mref(ms[1]): 3})}
    v.append(chart(P1, "ch_f1_margin", "lineChart", q, objs, None, filters=[years], alt_measure="Alt F1 Chart (text)"))
    v.append(dyn(P1, "c_f1_note", "F1 Note (text)"))

    # F2 the middleman: OTA share for the four brands, and the folio (one 2025 room night by channel)
    v += [kicker(P1, "c_f2_kicker", "F2  ·  THE MIDDLEMAN"), title(P1, "c_f2_title", "F2 Title (text)", "Alt F2 Title (text)")]
    ms = [f"Trend OTA {c}" for c, _ in BRANDS]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m, nm) for m, (_, nm) in zip(ms, BRANDS)]}}
    # the line ends carry the names, as in the comp: a legend of three identical grey dots could not be decoded (REVIEW m3).
    # The names in Dusk, not in the line's colour: Warm Grey (3.5:1) and Coffee Blue (3.7:1) fail 4.5:1 for 12 pt text
    # (plan 11); the line next to each name still ties them.
    objs = {"categoryAxis": axis(BODY, S, INK2), "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, extra={"labelPrecision": integer(0)}),
            "legend": legend(False),
            "seriesLabels": [{"properties": {"show": b(True), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2), "textSize": num(S), "seriesFontFamily": text(BODY)}}],
            "dataPoint": series_colors({mref(ms[0]): ACCENT_MARK, **{mref(m): SLATE for m in ms[1:]}}),
            "lineStyles": line_styles({mref(ms[0]): 3, **{mref(m): 1.5 for m in ms[1:]}})}
    v.append(chart(P1, "ch_f2_ota", "lineChart", q, objs, None, filters=[filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")],
                   alt_measure="Alt F2 Chart (text)"))
    # text measures: one formatter, and 'keeps' is the difference of the two shown amounts (REVIEW M7, M8)
    fol = ("Folio OTA Guest (text)", "Folio Direct Guest (text)")
    proj = [proj_col("FolioLine", "Line", display="One room night, 2025"), proj_mea(fol[0], "Via an online agency"), proj_mea(fol[1], "Direct, web and app")]
    colfmt = [{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": mref(m)}} for m in fol]
    # row padding 0: at 12 pt three rows and the header must fit 96 px without a scrollbar (renders 9 Nov: padding 4 scrolled at 120, padding 1 at 96)
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=0, header_size=S, column_formatting=colfmt)
    # no explicit sort: FolioLine[Line] is sorted by its Sort column in the model, and an explicit sort drew an arrow
    # under 'One room night, 2025' (REVIEW m5)
    v.append(visual("tbl_f2_folio", "tableEx", *at(P1, "tbl_f2_folio"), query={"Values": {"projections": proj}}, objects=objs, filters=[gi_filter()],
                    vcos=vco(padding=0)))
    bind_alt(v[-1], "Alt F2 Folio (text)")
    v.append(dyn(P1, "c_f2_note", "F2 Note (text)"))

    # F3 the fading welcome: NPS 2025 by years since the last renovation (dated hotels only)
    v += [kicker(P1, "c_f3_kicker", "F3  ·  THE FADING WELCOME"), title(P1, "c_f3_title", "F3 Title (text)", "Alt F3 Title (text)")]
    q = {"Category": {"projections": [proj_col("Hotels", "Renovation Age Label", display="Years since the last renovation")]}, "Y": {"projections": [proj_mea("NPS 2025 (signed)", "NPS 2025")]}}
    objs = {"categoryAxis": axis(BODY, S, INK), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False),
            "dataPoint": [{"properties": {"fill": fv("Age Band Color")}, "selector": WILD}], "labels": labels(True, BODY, 12, INK), "legend": legend(False),
            # the zero line the bars hang from (REVIEW m4); same object shape as the scatter's, which Desktop rendered
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "style": enum("solid"), "position": enum("front"),
                                                    "dataLabelShow": b(False)}, "selector": {"id": "1"}}]}
    v.append(chart(P1, "ch_f3_age", "clusteredColumnChart", q, objs, None,
                   filters=[gi_filter(), filter_in("Hotels", "Renovation Age Sort", [1, 2, 3], "flt_dated")], sort=sort_by_column("Hotels", "Renovation Age Label"),
                   alt_measure="Alt F3 Chart (text)"))
    v.append(dyn(P1, "c_f3_note", "F3 Note (text)"))

    # F4 where we are full
    v += [kicker(P1, "c_f4_kicker", "F4  ·  WHERE WE ARE FULL"), title(P1, "c_f4_title", "F4 Title (text)", "Alt F4 Title (text)")]
    v.append(card("c_f4_types", *at(P1, "c_f4_types"), ["Occupancy Airport GI (text)", "Occupancy City GI (text)", "Occupancy Highway GI (text)"], DISPLAY, 21, INK, BODY, S, INK2,
                  labels=["Airport hotels", "City hotels", "Highway hotels"]))
    bind_alt(v[-1], "Alt F4 Types (text)")
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Occupancy % 2025", "Occupancy 2025")]}}
    # axis from zero (never truncate a bar axis, CP-066); end 1.3 leaves room for the labels above the 90 % bars (pass 3)
    objs = {"categoryAxis": axis(BODY, S, INK), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, start=0, end=1.3),
            "dataPoint": [{"properties": {"fill": fv("Hotel Bar Color")}, "selector": WILD}], "labels": labels(True, BODY, S, INK, position="OutsideEnd"), "legend": legend(False)}
    # the airport hotels are Coffee Blue and every one of their names ends in "Airport", so colour is not the only carrier
    v.append(chart(P1, "ch_f4_fullest", "clusteredColumnChart", q, objs, None,
                   filters=[gi_filter(), topn_filter("Hotels", "Hotel Short Name", 7, "Occupancy % 2025", "flt_top7")], sort=sort_by_measure("Occupancy % 2025"),
                   alt_measure="Alt F4 Chart (text)"))
    v.append(tb(P1, "z_footer", FOOTER, alt="Source: Pillow & Key Group dataset. Guest scores weighted by survey responses; 2021 is a depressed base year. "
                                           "Not shown on purpose: impressions, likes, and NPS as a growth measure."))
    return v


# ====================================================================== P2 The Investment Strategy
P2 = "p2-investment-strategy"


HOVER_ACCENT, HOVER_SHEET = INK, HAIR  # theme colours only (pbir_detect theme-color-drift): white on Night, Night on Seam


def button(name, label, bookmark, filled, alt, label_measure=None):
    """VERIFY: actionButton text/fill object shapes; the visualLink shape is from the 2.6.0 visual schema."""
    # Shape copied from a Desktop-rendered button (hp-world-champs btn_nav_1): 'show' sits WITHOUT a selector, the
    # state formatting under {"id": "default"}; with 'show' inside the selector the text did not render (7 Nov).
    # Hover and selected (pressed) states set explicitly (catalog selectors default / hover / selected): the Back
    # button's hover fill went dark under dark text, 1.4:1 (REVIEW M1). Filled: white on Deep Coffee (6.2:1), white on
    # Night when hovered (15.8:1); outline: Night text on the Seam grey (13.9:1).
    ink, fill = (SURFACE, ACCENT) if filled else (INK, SURFACE)
    hover_fill = HOVER_ACCENT if filled else HOVER_SHEET
    lab = mtext(label_measure) if label_measure else text(label)
    objs = {"icon": [{"properties": {"shapeType": text("blank")}, "selector": {"id": "default"}}],
            "text": [{"properties": {"show": b(True)}},
                     {"properties": {"text": lab, "fontFamily": text(DISPLAY), "fontSize": num(S), "fontColor": color(ink), "bold": b(False)}, "selector": {"id": "default"}},
                     *[{"properties": {"text": lab, "fontColor": color(ink)}, "selector": {"id": st}} for st in ("hover", "selected")]],
            "fill": [{"properties": {"show": b(True)}},
                     {"properties": {"fillColor": color(fill), "transparency": num(0)}, "selector": {"id": "default"}},
                     *[{"properties": {"fillColor": color(hover_fill), "transparency": num(0)}, "selector": {"id": st}} for st in ("hover", "selected")]],
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


def button_slicer(name, table, column, selected, alt, cols, size=S):
    """The house-style toggle (08-verbeterplan V5/S1, brand-guide section 6 'scenario toggle'): a button slicer whose
    tiles are thin rounded outlines on white, the selected one Night with white text. State ids as the built-in
    themes write them (interaction:hover, selection:selected). VERIFY in Desktop: value text per state."""
    x, y, w, h, z, tab = at(P2, name)
    st = lambda i: {"id": i}
    objs = {
        "shapeCustomRectangle": [{"properties": {"tileShape": enum("rectangleRoundedByPixel"), "rectangleRoundedCurve": integer(h // 2)}, "selector": st("default")}],
        "layout": [{"properties": {"rowCount": integer(1), "columnCount": integer(cols), "maxTiles": integer(cols), "cellPadding": integer(8)}}],
        "fillCustom": [{"properties": {"show": b(True), "fillColor": color(SURFACE), "transparency": num(0)}, "selector": st("default")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:hover")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:press")},
                       {"properties": {"fillColor": color(INK)}, "selector": st("selection:selected")}],
        "outline": [{"properties": {"show": b(True), "lineColor": color(INK2), "weight": num(1), "transparency": num(0)}, "selector": st("default")},
                    {"properties": {"lineColor": color(INK)}, "selector": st("selection:selected")}],
        "value": [{"properties": {"show": b(True), "fontFamily": text(BODY), "fontSize": num(size), "fontColor": color(INK), "bold": b(False),
                                  "horizontalAlignment": text("center"), "verticalAlignment": text("middle")}, "selector": st("default")},
                  {"properties": {"fontColor": color(SURFACE), "bold": b(True)}, "selector": st("selection:selected")}],
        "label": [{"properties": {"show": b(False)}, "selector": st("default")}],
        # tile text padding: the theme's default (6 top, 8 bottom) clipped the descenders at 40 px (render 7 Nov)
        "padding": [{"properties": {"paddingSelection": text("Custom"), "topMargin": integer(2), "bottomMargin": integer(2), "leftMargin": integer(8), "rightMargin": integer(8)}, "selector": st("default")}],
        "selectionIcon": [{"properties": {"show": b(False)}, "selector": st("default")}],
        "selection": [{"properties": {"singleSelect": b(True), "strictSingleSelect": b(True), "selectAllCheckboxEnabled": b(False)}}],
        "general": [{"properties": {"filter": {"filter": {
            "Version": 2, "From": [{"Name": "s", "Entity": table, "Type": 0}],
            "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "s"}}, "Property": column}}],
                                            "Values": [[{"Literal": {"Value": f"'{selected}'"}}]]}}}]}}}}],
    }
    vcos = vco(alt=alt, padding=0)
    return visual(name, "advancedSlicerVisual", x, y, w, h, z, tab, query={"Values": {"projections": [proj_col(table, column)]}}, objects=objs, vcos=vcos)


def image_file(name, x, y, w, h, z, tab, f, alt):
    """An image visual showing a registered resource (logo, vignette). Shape from the powerbi-report-author catalog."""
    objs = {"image": [{"properties": {"sourceType": text("image"), "sourceFile": {"image": {
                "name": text(f), "url": {"expr": {"ResourcePackageItem": {"PackageName": "RegisteredResources", "PackageType": 1, "ItemName": f}}}, "scaling": text("Fit")}}}}],
            "imageScaling": [{"properties": {"imageScalingType": text("Fit")}}]}
    return visual(name, "image", x, y, w, h, z, tab, objects=objs, vcos=vco(alt=alt, padding=0))


def image_measure(page, name, measure, alt):
    """An image visual whose URL is a measure (an SVG data URI): the brand's state chip. VERIFY: image.sourceUrl bound
    to a measure (catalog: sourceType imageUrl + sourceUrl)."""
    x, y, w, h, z, tab = at(page, name)
    objs = {"image": [{"properties": {"sourceType": text("imageUrl"), "sourceUrl": mtext(measure), "fit": text("Fit")}}]}
    return visual(name, "image", x, y, w, h, z, tab, objects=objs, vcos=vco(alt=alt, padding=0))


def brand_row(page_name, sfx):
    """The 3.1 lockup on the night zone and the eyebrow beside it (plan 11): first in the reading order, so a screen
    reader starts with whose report this is and which page. The vignettes and pay-offs of kit 2.x are gone."""
    pg = next(p for p in LAYOUT["pages"] if p["name"] == page_name)
    L = pg["logo"]
    out = [image_file("z_logo", L["x"], L["y"], L["w"], L["h"], 1003, L["tab"], LOCKUP, "Goodnight Inn"),
           # ZONE_EYEBROW on Night 9.5:1; at the 12 pt floor instead of the kit's 11 pt eyebrow
           tb(page_name, f"z_eyebrow{sfx}", EYEBROW[page_name], font=DISPLAY, size=SPX, colour=ZONE_EYEBROW,
              alt=("Page 1 of 2: the brand review" if sfx == "" else "Page 2 of 2: the investment strategy"))]
    return out


def scatter_axes(objs):
    """The scatter's axis ends from measures, shared by all three layers so their plot areas match exactly."""
    objs["categoryAxis"][0]["properties"]["start"] = mtext("Scatter X Start")
    objs["categoryAxis"][0]["properties"]["end"] = mtext("Scatter X End")
    objs["valueAxis"][0]["properties"]["start"] = mtext("Scatter Y Start")
    objs["valueAxis"][0]["properties"]["end"] = mtext("Scatter Y End")
    return objs


def p2_visuals():
    # the budget comes from the model (Masthead P2 (text)); it was typed in here
    v = [dyn(P2, "z_masthead2", "Masthead P2 (text)", size=S, colour=ZONE_MUTED, align="right", alt_measure="Alt Masthead P2 (text)"),
         dyn(P2, "z_headline2", "Headline P2 (text)", size=28, colour=ZONE_TEXT, font=DISPLAY),
         dyn(P2, "c_subtitle2", "Subtitle P2 (text)", size=S, colour=ZONE_MUTED),
         title(P2, "c_scatter_title", "Scatter Title (text)"),
         # C named by its role (08-verbeterplan V1): the answer to "why not renovate?", not a third candidate
         tb(P2, "c_scatter_sub", "Above the line a package pays back by 2032. A: our recommendation  ·  B: the alternative  ·  C: why not renovate?")]
    q = {"Category": {"projections": [proj_col("Package", "PackageID")]},
         "X": {"projections": [proj_mea("Package Capex", "Capex")]},
         "Y": {"projections": [proj_mea("Package NPV (sel)", "NPV through 2032")]}, "Size": {"projections": [proj_mea("Package Point Size", "Marker size")]}}
    # units=1 (none): the measures' formats already print $M; auto units scaled a second time ("$0MM", 7 Nov).
    objs = {"categoryAxis": axis(BODY, S, INK2, title=True, units=1, extra={"titleText": text("Capex of the package, $M"), "titleFontFamily": text(BODY), "titleFontSize": num(S), "titleColor": color(INK2)}),
            "valueAxis": axis(BODY, S, INK2, title=True, gridlines=True, grid_color=HAIR, units=1,
                              extra={"titleText": text("NPV through 2032, $M"), "titleFontFamily": text(BODY), "titleFontSize": num(S), "titleColor": color(INK2)}),
            "dataPoint": [{"properties": {"fill": fv("Package Point Color")}, "selector": WILD}],
            "bubbles": [{"properties": {"bubbleSize": integer(-40), "markerRangeType": enum("magnitude"), "preventOverflow": b(False)}}], "legend": legend(False),
            "categoryLabels": [{"properties": {"show": b(False)}}],
            # The verdict line, quieter (08-verbeterplan V3): 1 px in Warm Grey, not at full weight. The band
            # above it, where a package pays back by 2032, is shaded in Coffee Blue at 90 % transparency and says so at its
            # right end, where no package sits (its label at the left had sat under the best packages, 7 Nov).
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(SLATE), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("back"), "displayName": text("Pays back by 2032"),
                                                    "dataLabelShow": b(True), "dataLabelText": text("Name"), "dataLabelColor": color(INK2),
                                                    "dataLabelHorizontalPosition": enum("right"), "dataLabelVerticalPosition": enum("above"),
                                                    "shadeShow": b(True), "shadeRegion": enum("after"), "shadeColor": color(ACCENT_MARK), "shadeTransparency": num(90)},
                                     "selector": {"id": "1"}}]}
    scatter_axes(objs)
    # Three layers on one plot area (same axis measures, preventOverflow off on all, so the plot areas match).
    # 1 the cloud: every package but A, B and C, Warm Grey. 2 A, B and C on top with their letters: Power BI draws
    # larger markers first, so a cloud in the same visual painted over B and C (REVIEW M2, 7 Nov). 3 a hover layer on
    # top of both: all 456 packages, fully transparent markers, wired to the tooltip page, so every dot shows its own
    # card (08-verbeterplan V2; in batch 2 the A/B/C layer blocked the cloud's tooltips, N3).
    x, y, w, h, z, tab = at(P2, "hero_packages")
    q_cloud = {k: val for k, val in q.items() if k != "Size"}
    o_cloud = copy.deepcopy(objs)
    o_cloud["bubbles"][0]["properties"]["bubbleSize"] = integer(0)
    # The cloud is a tab stop after the A/B/C layer (pass-3 review: the package card is hover-only). Its header gives
    # 'Show as table', and the card's facts ride in its Tooltips well, so a keyboard user reads every package's
    # payback, range and initiatives there. The hover layer stays out of the tab order (mouse only).
    q_cloud_kb = {**q_cloud, "Tooltips": {"projections": [proj_mea("TT Payback (text)", "Payback"), proj_mea("TT Range (text)", "NPV in Low, Expected, High"),
                                                          proj_mea("TT Mix (text)", "Initiatives")]}}
    v.append(bind_alt(visual("hero_packages", "scatterChart", x, y, w, h, z, tab + 1, query=q_cloud_kb, objects=o_cloud, filters=[filter_in("Package", "Preset", [""], "flt_cloud")],
                             vcos=vco(padding=0)), "Alt Scatter Cloud (text)"))
    quiet = lambda o: (o["valueAxis"][0]["properties"].__setitem__("gridlineShow", b(False)), o.pop("y1AxisReferenceLine", None), o)[-1]
    q2 = {**q, "Category": {"projections": [proj_col("Package", "Preset", display="Package")]}}
    o2 = quiet(copy.deepcopy(objs))
    o2["categoryLabels"] = [{"properties": {"show": b(True), "fontFamily": text(DISPLAY), "fontSize": num(S), "color": color(SURFACE), "bold": b(True)}}]
    o2["dataPoint"] = [{"properties": {"fill": fv("Named Point Color")}, "selector": WILD}]
    v.append(bind_alt(visual("hero_named", "scatterChart", x, y, w, h, z + 2, tab, query=q2, objects=o2, filters=[filter_in("Package", "Preset", ["A", "B", "C"], "flt_named")],
                             vcos=vco(padding=0)), "Alt Scatter (text)"))
    o3 = quiet(copy.deepcopy(o_cloud))
    o3["markers"] = [{"properties": {"transparency": num(100), "borderShow": b(False)}}]
    hv = vco(padding=0)
    hv["visualTooltip"] = [{"properties": {"show": b(True), "type": enum("Canvas"), "section": text(TT)}}]
    v.append(decorative(visual("hero_hover", "scatterChart", x, y, w, h, z + 4, 0, query=q_cloud, objects=o3, vcos=hv), 2))
    v.append(button_slicer("sl_view", "ScatterView", "View", "All packages", "Scatter view: all packages, or a zoom on the region where A, B and C sit", 2, size=S))
    # the labels above the two slicers are in the slicers' alt text, so they leave the tab order (plan 11)
    v.append(decorative(tb(P2, "lbl_scenario", "Scenario", size=SPX, colour=INK2), 3))
    v.append(button_slicer("sl_scenario", "Scenario", "Scenario", "Expected", "Scenario: Low, Expected or High; every number on this page follows it", 3))
    v.append(decorative(tb(P2, "lbl_package", "Package in focus", size=SPX, colour=INK2), 4))
    v.append(slicer("sl_package", *at(P2, "sl_package"), "PlanSelector", "Label", "Package in focus", BODY, INK, INK2, SURFACE, ACCENT, mode="Dropdown", single=True,
                    selected=["A · Our recommendation"], alt="Package in focus: the recommendation A, the alternative B, or C, the answer to why not renovate", size=S))
    v[-1]["visual"]["objects"]["header"][0]["properties"]["show"] = b(False)
    v[-1]["visual"]["visualContainerObjects"]["border"] = [{"properties": {"show": b(True), "color": color(INK2), "radius": num(20), "width": num(1)}}]

    # state: shortlist = the recommendation and what was weighed against it
    v.append(dyn(P2, "c_focus_line", "Focus Line (text)"))
    v.append(decorative(image_measure(P2, "img_rec_chip", "Chip Funded", None), 5))
    v.append(tb(P2, "c_rec_title", "Our recommendation: package A", font=DISPLAY, size=20, colour=INK))
    v.append(dyn(P2, "c_rec_mix", "Rec Mix (text)", size=S, colour=INK))
    v.append(card("c_rec_nums", *at(P2, "c_rec_nums"), ["Rec Capex (text)", "Rec NPV (text)", "Rec Range (text)", "Rec Run-rate (text)"], DISPLAY, 21, INK, BODY, S, INK2,
                  labels=["capex", "NPV through 2032", "NPV, Low to High, $M", "profit a year by 2032"]))
    bind_alt(v[-1], "Alt Rec Nums (text)")
    v.append(dyn(P2, "c_rec_answers", "Rec Answers (text)", colour=INK))
    v.append(dyn(P2, "c_rec_held", "Rec Held (text)", colour=INK, alt_measure="Alt Rec Held (text)"))
    v.append(dyn(P2, "c_rec_rules", "Rec Rules (text)"))
    v.append(tb(P2, "c_alt_title", "Considered, not recommended", font=DISPLAY, size=20, colour=INK))
    v.append(dyn(P2, "c_alt_b", "Alt B (text)", colour=INK))
    v.append(dyn(P2, "c_alt_c", "Alt C (text)", colour=INK))
    v.append(dyn(P2, "c_not_funded", "Not Funded (text)", colour=INK))
    v.append(dyn(P2, "c_uncertainty", "Uncertainty (text)"))
    v.append(bind_alt(button("btn_open_plan", "Open the plan for the package in focus  →", "bm_p2_plan", True, None,
                             label_measure="Open Plan Label (text)"), "Alt Open Plan (text)"))

    # state: plan (hidden by default)
    v.append(dyn(P2, "c_plan_title", "Plan Title (text)", size=TITLE_PT, colour=INK, font=DISPLAY))
    v.append(dyn(P2, "c_plan_ops", "Plan Ops (text)"))
    q = {"Category": {"projections": [proj_col("InvestmentProjects", "Short Name")]}, "Y": {"projections": [proj_mea("Focus Project NPV (shown)", "NPV through 2032")]}}
    # no value axis: every bar carries its own signed label, and at 12 pt with 'responsive' off (plan 11) the axis
    # labels piled up in the 120 px plot (render 9 Nov)
    objs = {"categoryAxis": axis(BODY, S, INK2, gridlines=None), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, units=1),
    # the ends from the model, so the bar labels always have room (Waterfall Y Start / End)
            # plan 10 D6: an increase in Coffee Blue, a decrease in Tangerine (a signal), the total in Night; the labels
            # carry the sign (+ / true minus) too
            "sentimentColors": [{"properties": {"increaseFill": color(ACCENT_MARK), "decreaseFill": color(SIGNAL_MARK), "totalFill": color(INK), "otherFill": color(SLATE)}}],
            "labels": labels(True, BODY, S, INK, units=1, position="OutsideEnd"), "legend": legend(False)}
    objs["valueAxis"][0]["properties"]["start"] = mtext("Waterfall Y Start")
    objs["valueAxis"][0]["properties"]["end"] = mtext("Waterfall Y End")
    v.append(chart(P2, "ch_plan_waterfall", "waterfallChart", q, objs, None,
                   title_measure="Waterfall Title (text)", filters=[filter_measure_gt("Focus Project Flag", 0, "flt_focus_wf")], alt_measure="Alt Waterfall (text)"))
    # All ten initiatives, the package first, each group by NPV. At 11 pt the finding and the growth flag share one
    # column ("F2 · growth"): nine columns no longer fit 752 px (08-verbeterplan R4).
    # the chip column has a header word (plan 11: a blank header is read as an empty column name)
    proj = [proj_mea("Initiative Chip", "In plan"), proj_mea("Initiative Status (text)", "Status"), proj_col("InvestmentProjects", "Short Name", display="Initiative"),
            proj_mea("Initiative Answers (text)", "Answers"), proj_mea("Initiative Capex (text)", "Capex"),
            proj_mea("Initiative Run-rate (text)", "Profit/yr"), proj_mea("Initiative NPV (text)", "NPV"), proj_mea("Initiative Guest Effect (text)", "Guest pts")]
    right = ("Initiative Capex (text)", "Initiative Run-rate (text)", "Initiative NPV (text)", "Initiative Guest Effect (text)")
    colfmt = [{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": mref(m)}} for m in right]
    extra = [{"properties": {"fontColorPrimary": fv("Initiative Status Color")}, "selector": {**WILD, "metadata": mref("Initiative Status (text)")}}]
    # row padding 0: ten rows and the header in 264 px at 12 pt (renders 9 Nov: padding 2 scrolled at 280, padding 0 at 248)
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=0, header_size=S, extra_values=extra, column_formatting=colfmt)
    objs["grid"][0]["properties"]["imageHeight"] = num(18)
    objs["grid"][0]["properties"]["imageWidth"] = num(26)
    v.append(visual("tbl_plan_initiatives", "tableEx", *at(P2, "tbl_plan_initiatives"), query={"Values": {"projections": proj}}, objects=objs,
                    sort=sort_by_measure("Initiative Chip", desc=False),
                    vcos=vco(padding=0)))
    bind_alt(v[-1], "Alt Plan Table (text)")
    ms = ["Cumulative Line (Low)", "Cumulative Line (Expected)", "Cumulative Line (High)", "Focus Cumulative Net (sel)"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]},
         "Y": {"projections": [proj_mea(ms[0], "Low"), proj_mea(ms[1], "Expected"), proj_mea(ms[2], "High"), proj_mea(ms[3], "This case")]}}
    # no year axis in 104 px (what 'responsive' used to hide; plan 11 turned it off so text never shrinks): the payback
    # year is in the risk sentence under the chart and in the alt text
    # A legend that draws each line (lineOnly), not end labels: in 96 px the three end points sit closer than a label
    # is tall and Power BI dropped the labels of the line in view (pass-3 review). Each line differs by pattern too:
    # Low dashed, Expected dotted, High solid, the case in view thick.
    lg = legend(True, BODY, S, INK2, "Top")
    lg[0]["properties"]["legendMarkerRendering"] = enum("lineOnly")
    # no axes in 96 px: the payback year is in the title, the end values in the alt text, and the zero line is labelled
    objs = {"categoryAxis": axis(BODY, S, INK2, show=False), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, units=1), "legend": lg,
            # plan 10 D6: the Low case is a signal (Tangerine, and dashed, so not by colour alone), Expected and High in
            # Warm Grey, the case in view emphasised in Coffee Blue; the end labels in Dusk (series colours fail 4.5:1)
            "dataPoint": series_colors({mref(ms[0]): SIGNAL_MARK, mref(ms[1]): SLATE, mref(ms[2]): SLATE, mref(ms[3]): ACCENT_MARK}),
            "lineStyles": line_styles({**{mref(m): 1.5 for m in ms[:3]}, mref(ms[3]): 3}, dashed=(mref(ms[0]),)),
            "seriesLabels": [{"properties": {"show": b(False)}}],
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(SLATE), "transparency": num(0), "width": num(1), "style": enum("solid"), "position": enum("back"),
                                                    "displayName": text("Break-even"), "dataLabelShow": b(True), "dataLabelText": text("Name"), "dataLabelColor": color(INK2),
                                                    "dataLabelHorizontalPosition": enum("left"), "dataLabelVerticalPosition": enum("above")}, "selector": {"id": "1"}}]}
    next(e for e in objs["lineStyles"] if e.get("selector", {}).get("metadata") == mref(ms[1]))["properties"]["lineStyle"] = enum("dotted")
    v.append(chart(P2, "ch_plan_cumulative", "lineChart", q, objs, None,
                   title_measure="Cumulative Title (text)", filters=[filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon2")],
                   alt_measure="Alt Cumulative (text)"))
    v.append(dyn(P2, "c_plan_risk", "Plan Risk (text)"))
    v.append(button("btn_back", "←  Back to the recommendation", "bm_p2_shortlist", False, "Back to the recommendation and its alternatives"))
    v.append(dyn(P2, "z_footer2", "Footer P2 (text)"))
    return v


# ====================================================================== the package tooltip (08-verbeterplan V2)
TT = "tt-package"


def tt_visuals():
    """A native report-page tooltip, 432 x 296: the brand's state chip and the package's name, NPV large (Deep Coffee
    when it pays back by 2032, Burnt Tangerine when not; the sign carries it too), capex, the three cases, payback and
    the moves.
    Grain: one Package[PackageID] from the hover layer."""
    def c(name, measure, size, colour, font=BODY, bold=False, label=None):
        x, y, w, h, z, tab = at(TT, name)
        vv = card(name, x, y, w, h, z, tab, [measure], font, size, colour, BODY, S, INK2, labels=[label] if label else None)
        if bold:
            vv["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
        return bind_alt(vv, measure)
    v = [decorative(image_measure(TT, "tt_chip", "TT Chip", None), 1),
         c("tt_title", "TT Title (text)", TITLE_PT, INK, DISPLAY),
         c("tt_npv", "TT NPV (text)", 28, INK, DISPLAY, True, label="NPV through 2032"),
         c("tt_capex", "TT Capex (text)", 21, INK, DISPLAY, False, label="capex"),
         c("tt_range", "TT Range (text)", S, INK2),
         c("tt_payback", "TT Payback (text)", S, INK, bold=True),
         c("tt_mix", "TT Mix (text)", S, INK2)]
    v[2]["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("TT NPV Color")
    return v


# ====================================================================== pages, bookmarks, resources
# Night-glow depth (plan 10 D7 with Bjorn's waiver, plan 11): one soft shadow for every card, a heavier one under each
# page's hero card, and a Coffee Blue glow under the recommendation. Values from the comps (comps_v3.GLOW):
# box-shadow 0 14px 36px rgba(8,18,34,.16) / 0 24px 56px rgba(8,18,34,.28) / 0 14px 34px rgba(37,137,216,.30).
# The shadow colour is Night, the kit's card_shadow token (the comps used a near-black #081222 that is not in the theme).
SHADOW = {"card": (INK, 14, 36, 84), "hero": (INK, 24, 56, 72), "glow": (ACCENT_MARK, 14, 34, 70)}
HERO_CARDS = {"kpi", "scatter"}


def frame(name, x, y, w, h, z, i, shadow, border=SURFACE):
    """An empty textbox as card furniture: white fill, radius 12, one outer shadow (visualContainer dropShadow:
    preset Custom, position Outer, angle 90 = straight down), out of the tab order. The border is drawn in the
    fill colour, so the radius shows without a hairline (plan 10 D4: no hairline round the cards)."""
    col, dist, blur, transp = SHADOW[shadow]
    v = textbox(name, x, y, w, h, z, 0, [[("", BODY, SPX, INK2, False)]])
    vc = v["visual"]["visualContainerObjects"]
    vc["background"] = [{"properties": {"show": b(True), "color": color(SURFACE), "transparency": num(0)}}]
    vc["border"] = [{"properties": {"show": b(True), "color": color(border), "radius": num(12), "width": num(1)}}]
    vc["dropShadow"] = [{"properties": {"show": b(True), "preset": enum("Custom"), "position": enum("Outer"), "color": color(col),
                                        "transparency": num(transp), "shadowSpread": num(0), "shadowBlur": num(blur), "angle": num(90),
                                        "shadowDistance": num(dist)}}]
    return decorative(v, 500 + i)


def card_frames(page_name):
    """The layout's cards as visuals UNDER the content (z 100+): being visuals, they scale with the content (a
    page-background PNG did not when Desktop scaled the canvas non-uniformly, 7 Nov). Then the recommendation's tile
    (z_tile_rec, P2 shortlist state only: the bookmarks hide every z_tile_* in the plan state)."""
    pg = next(p for p in LAYOUT["pages"] if p["name"] == page_name)
    out = [frame(f"z_card_{c['id']}", c["x"], c["y"], c["w"], c["h"], 100 + i, i, "hero" if c["id"] in HERO_CARDS else "card")
           for i, c in enumerate(pg["cards"])]
    for j, t in enumerate(pg.get("tiles", [])):
        out.append(frame(f"z_tile_{t['id']}", t["x"], t["y"], t["w"], t["h"], 150 + j, 50 + j, "glow", border=ACCENT_MARK))
    return out


CANVAS_FILE = "canvas-night.jpg"


def night_canvas():
    """The night-glow canvas (brand_canvas_v3.py) as a decorative image visual under everything (z 0)."""
    return decorative(image_file("z_canvas", 0, 0, LAYOUT["canvas"]["w"], LAYOUT["canvas"]["h"], 0, 0, CANVAS_FILE, None), 0)


DATA_VISUALS = {"lineChart", "clusteredColumnChart", "scatterChart", "tableEx", "waterfallChart"}


def finish(visuals):
    """Plan 11, the same for every visual: (1) Segoe UI Semibold is the bold cut, so no synthetic bold on top of it;
    (2) data visuals keep their header (focus mode, 'show as a table': the accessibility features the theme keeps for
    them, compile_theme.py), except layers that are out of the tab order; (3) charts are not responsive."""
    def walk(o):
        if isinstance(o, dict):
            if o.get("fontFamily") == text(DISPLAY) and "bold" in o:
                o["bold"] = b(False)
            if o.get("fontFamily") == DISPLAY and "fontWeight" in o:
                o.pop("fontWeight")
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    for v in visuals:
        walk(v)
        # (3) charts never shrink their text to fit: 'responsive' scaled F2's 12 pt axis labels down in its 184 px chart
        # (render 9 Nov), under the floor (catalog: objects.general.responsive)
        if v["visual"]["visualType"] in DATA_VISUALS - {"tableEx"}:
            gen = v["visual"].setdefault("objects", {}).setdefault("general", [{"properties": {}}])
            gen[0]["properties"]["responsive"] = b(False)
        if v["visual"]["visualType"] in DATA_VISUALS and v["position"]["tabOrder"] >= 0:
            v["visual"]["visualContainerObjects"]["visualHeader"] = [{"properties": {"show": b(True)}}]
    return visuals


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


def page(name, display, visuals, filters=None, tooltip=False, interactions=None):
    # colour only: furniture (cards, logo) is drawn by visuals so it scales with the content on any viewport
    cv = next(pg for pg in LAYOUT["pages"] if pg["name"] == name).get("canvas", LAYOUT["canvas"])
    p = {"$schema": PAGE_SCHEMA, "name": name, "displayName": display, "displayOption": "FitToPage", "height": cv["h"], "width": cv["w"],
         "objects": {"background": [{"properties": {"color": color(SURFACE if tooltip else CANVAS), "transparency": num(0)}}]}}
    if tooltip:
        # a report-page tooltip: hidden in view mode, bound as a tooltip (page schema 2.1.0: type + pageBinding)
        p.update({"displayOption": "ActualSize", "type": "Tooltip", "visibility": "HiddenInViewMode",
                  "pageBinding": {"name": tag("binding." + name)[:20].replace("-", ""), "type": "Tooltip", "parameters": []}})
    if interactions:
        p["visualInteractions"] = interactions
    if filters:
        p["filterConfig"] = {"filters": filters}
    for vis in visuals:
        # inner tiles (z_tile_*) belong to the shortlist state, as in bookmark()
        st = "shortlist" if vis["name"].startswith("z_tile_") else state_of(name, vis["name"])
        if st == ("shortlist" if PLAN_STATE else "plan"):
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
    v1 = finish(no_card_fill([night_canvas()] + card_frames(P1) + brand_row(P1, "") + p1_visuals()))
    v2 = finish(no_card_fill([night_canvas()] + card_frames(P2) + brand_row(P2, "2") + p2_visuals()))
    vt = finish(no_card_fill(tt_visuals()))
    # the hover layer only shows tooltips: a click on a transparent dot must not filter or dim anything else
    quiet = [{"source": "hero_hover", "target": o["name"], "type": "NoFilter"} for o in v2 if o["name"] != "hero_hover"]
    # visual header icons: already off on every visual through pbir_lib.vco (visualHeader show=false); the icons in
    # the review screenshots (REVIEW p10) are Desktop's edit-mode chrome, which the Publish-to-Web check confirms
    pages = [page(P1, "The Brand Review", v1),
             page(P2, "The Investment Strategy", v2,
                  filters=[filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_page_projects"), filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_page_brand")],
                  interactions=quiet),
             page(TT, TT, vt, tooltip=True)]
    rep = write_report(OUT, NAME, "Goodnight Inn · opzet", pages, THEME, THEME_FILE)
    res = rep / "StaticResources" / "RegisteredResources"
    # embedded, never a link (Publish to Web): the kit's reversed lockup and the one night-glow canvas both pages share
    shutil.copyfile(KIT / LOCKUP, res / LOCKUP)
    shutil.copyfile(BG / CANVAS_FILE, res / CANVAS_FILE)
    files = [LOCKUP, CANVAS_FILE]
    rj = rep / "definition" / "report.json"
    report = json.loads(rj.read_text(encoding="utf-8"))
    for pk in report["resourcePackages"]:
        if pk["name"] == "RegisteredResources":
            pk["items"] += [{"name": f, "path": f, "type": "Image"} for f in files]
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
