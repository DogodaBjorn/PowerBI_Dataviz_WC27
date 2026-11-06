"""Writes the new report set-up (opzet, 2026-11-06) as a PBIP report on the shared model.

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
import json
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
LAYOUT = json.loads((ROOT / "project" / "design-prototypes" / "opzet-layout.json").read_text(encoding="utf-8"))
THEME = json.loads((ROOT / "project" / "deliverables" / "theme.json").read_text(encoding="utf-8"))
THEME_FILE = "goodnight-inn-hanger.json"
THEME["name"] = THEME_FILE  # the registered file name (pbir_lib / pbir_detect convention)
BG = ROOT / "project" / "deliverables" / "backgrounds"

CANVAS, SURFACE, INK, INK2, HAIR = "#F5F3F0", "#FFFFFF", "#24192B", "#5B5163", "#E4DEE3"
ACCENT, GOOD, BAD, SLATE, PLUM = "#B5175F", "#1D5FA8", "#B45309", "#82798A", "#3E2C55"
DISPLAY, BODY = "Trebuchet MS", "Verdana"
FOOTER = ("Data: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores response-weighted. "
          "Margins before commissions unless marked. 2021 is a depressed base year. Projections: scenario logic from FinanceParameters.")
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
    return SLOT[page][name].get("state")


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


def p1_visuals():
    v = [tb(P1, "z_masthead", "THE BRAND REVIEW  ·  2021 TO 2025  ·  FOR THE BOARD OF PILLOW & KEY GROUP", align="right"),
         tb(P1, "z_headline", "Do not disturb, since 2020.", font=DISPLAY, size=37, colour=INK, bold=True, alt="Page headline: Do not disturb, since 2020."),
         dyn(P1, "c_subtitle", "Subtitle P1 (text)", size=11),
         tb(P1, "c_compare_title", "Goodnight Inn leads on occupancy, and is last of four on what guests and booking channels say", font=DISPLAY, size=17, colour=INK, bold=True),
         tb(P1, "c_compare_sub", "The brand promise is “A good night. A fair price.” The lines test it: booked with us, a good night, a fair price, recommend us. 2025, the four Pillow & Key brands; rates reflect each segment and are not ranked; change is 2023 to 2025.")]

    # hero: the four-brand comparison (table-studio: right-aligned figures, Goodnight Inn column tinted, verdict in words)
    proj = [proj_col("KpiLine", "Finding", display="Finding"), proj_col("KpiLine", "Measure", display="Measure")]
    proj += [proj_mea(f"KPI Text {c}", nm) for c, nm in BRANDS]
    proj += [proj_mea("KPI Rank (text)", "Goodnight Inn rank"), proj_mea("KPI Change since 2023 (text)", "Change since 2023")]
    extra = [{"properties": {"fontColorPrimary": fv("KPI Rank Color")}, "selector": {**WILD, "metadata": mref("KPI Rank (text)")}},
             {"properties": {"fontColorPrimary": fv("KPI Change Color")}, "selector": {**WILD, "metadata": mref("KPI Change since 2023 (text)")}},
             {"properties": {"backColorPrimary": fv("GN Column Tint")}, "selector": {**WILD, "metadata": mref("KPI Text GI")}}]
    colfmt = [{"properties": {"alignment": enum("Right")}, "selector": {"metadata": mref(f"KPI Text {c}")}} for c, _ in BRANDS]
    colfmt += [{"properties": {"alignment": enum("Right")}, "selector": {"metadata": mref(m)}} for m in ("KPI Rank (text)", "KPI Change since 2023 (text)")]
    objs = table_objects(BODY, 11, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=7, header_size=10, extra_values=extra, column_formatting=colfmt)
    v.append(visual("hero_brand_compare", "tableEx", *at(P1, "hero_brand_compare"), query={"Values": {"projections": proj}}, objects=objs,
                    vcos=vco(alt="Table comparing Goodnight Inn with P&K Select, Maison d'Or and Pebble & Pine on thirteen 2025 measures, grouped by findings F1 to F3, with Goodnight Inn's rank and its change since 2023", padding=0),
                    sort=sort_by_column("KpiLine", "Measure")))

    # geography
    v.append(dyn(P1, "c_geo_title", "Geo Title (text)", size=13, colour=INK, font=DISPLAY, bold=True))
    v.append(tb(P1, "c_geo_sub", "Occupancy 2025 by region and location type  ·  number of hotels"))
    q = {"Rows": {"projections": [proj_col("Hotels", "Region")]}, "Columns": {"projections": [proj_col("Hotels", "LocationType")]},
         "Values": {"projections": [proj_mea("Occupancy and Hotels (text)", "Occupancy · hotels")]}}
    objs = {"columnHeaders": [{"properties": {"fontFamily": text(BODY), "fontSize": num(10), "fontColor": color(INK2), "backColor": color(SURFACE), "outlineStyle": enum("None"), "alignment": enum("Right")}}],
            "rowHeaders": [{"properties": {"fontFamily": text(BODY), "fontSize": num(11), "fontColor": color(INK), "backColor": color(SURFACE), "outlineStyle": enum("None")}}],
            "values": [{"properties": {"fontFamily": text(BODY), "fontSize": num(11), "fontColorPrimary": color(INK), "backColorPrimary": color(SURFACE), "backColorSecondary": color(SURFACE), "outlineStyle": enum("None")}},
                       {"properties": {"backColor": fv("Occupancy Heat Color")}, "selector": {**WILD, "metadata": mref("Occupancy and Hotels (text)")}}],
            "grid": [{"properties": {"gridVertical": b(False), "gridHorizontal": b(True), "gridHorizontalColor": color(HAIR), "rowPadding": num(8), "outlineStyle": enum("None")}}]}
    v.append(visual("tbl_geo", "pivotTable", *at(P1, "tbl_geo"), query=q, objects=objs, filters=[gi_filter()],
                    vcos=vco(alt="Matrix of Goodnight Inn occupancy in 2025 by region (rows) and location type (columns), with hotel counts and totals; airport cells are the fullest", padding=0)))
    v.append(tb(P1, "c_full_title", "The seven fullest hotels, 2025 occupancy  ·  airports in raspberry"))
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Occupancy % 2025", "Occupancy 2025")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK), "valueAxis": axis(BODY, 9, INK2, show=False, gridlines=False, start=0, end=1),
            "dataPoint": [{"properties": {"fill": fv("Hotel Bar Color")}, "selector": WILD}], "labels": labels(True, BODY, 10, INK), "legend": legend(False)}
    v.append(chart(P1, "ch_fullest_hotels", "clusteredBarChart", q, objs, "Bar chart of the seven Goodnight Inn hotels with the highest 2025 occupancy; five are airport hotels, led by Toronto Pearson and London Gatwick",
                   filters=[gi_filter(), topn_filter("Hotels", "Hotel Short Name", 7, "Occupancy % 2025", "flt_top7")], sort=sort_by_measure("Occupancy % 2025")))

    # trends: Goodnight Inn in raspberry, the sister brands in plum-slate (one live hue)
    for slot_name, key, title_m, fmt in (("ch_trend_margin", "Margin after", "Trend Title Margin (text)", 0), ("ch_trend_ota", "OTA", "Trend Title OTA (text)", 0), ("ch_trend_nps", "NPS", "Trend Title NPS (text)", 1)):
        ms = [f"Trend {key} {c}" for c, _ in BRANDS]
        q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m, nm) for m, (_, nm) in zip(ms, BRANDS)]}}
        objs = {"categoryAxis": axis(BODY, 10, INK2), "valueAxis": axis(BODY, 10, INK2, gridlines=True, grid_color=HAIR),
                "legend": legend(True, BODY, 10, INK2, "Right"),
                "dataPoint": series_colors({mref(ms[0]): ACCENT, **{mref(m): SLATE for m in ms[1:]}}),
                "lineStyles": line_styles({mref(ms[0]): 3, **{mref(m): 1.5 for m in ms[1:]}})}
        v.append(chart(P1, slot_name, "lineChart", q, objs, f"Line chart 2021 to 2025: Goodnight Inn against the three sister brands, {key.lower()}",
                       title_measure=title_m, filters=[filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")]))
    v.append(tb(P1, "z_footer", FOOTER))
    return v


# ====================================================================== P2 The Investment Strategy
P2 = "p2-investment-strategy"


def nums_card(name, measures, labs, alt):
    return card(name, *at(P2, name), measures, BODY, 16, INK, BODY, 10, INK2, labels=labs, alt=alt)


def button(name, label, bookmark, filled, alt):
    """VERIFY: actionButton text/fill object shapes; the visualLink shape is from the 2.6.0 visual schema."""
    objs = {"icon": [{"properties": {"show": b(False)}, "selector": {"id": "default"}}],
            "text": [{"properties": {"show": b(True), "text": text(label), "fontFamily": text(BODY), "fontSize": num(11), "fontColor": color(SURFACE if filled else INK), "bold": b(True)}, "selector": {"id": "default"}}],
            "fill": [{"properties": {"show": b(True), "fillColor": color(ACCENT if filled else SURFACE), "transparency": num(0)}, "selector": {"id": "default"}}],
            "outline": [{"properties": {"show": b(not filled), "lineColor": color(INK2), "weight": num(1), "roundEdge": num(20)}, "selector": {"id": "default"}}]}
    vcos = vco(alt=alt, padding=0)
    vcos["visualLink"] = [{"properties": {"show": b(True), "type": enum("Bookmark"), "bookmark": text(bookmark)}}]
    return visual(name, "actionButton", *at(P2, name), objects=objs, vcos=vcos)


def tile(name, card_id):
    c = next(c for c in LAYOUT["pages"][1]["cards"] if c["id"] == card_id)
    v = textbox(name, c["x"], c["y"], c["w"], c["h"], 1100, 9500, [[("", BODY, 10, INK2, False)]])
    v["visual"]["visualContainerObjects"]["background"] = [{"properties": {"show": b(True), "color": color(CANVAS), "transparency": num(0)}}]
    v["visual"]["visualContainerObjects"]["border"] = [{"properties": {"show": b(True), "color": color(HAIR), "radius": num(12), "width": num(1)}}]
    return v


def p2_visuals():
    v = [tb(P2, "z_masthead2", "THE INVESTMENT STRATEGY  ·  2027 TO 2032  ·  GOODNIGHT INN BUDGET $60.0M", align="right"),
         tb(P2, "z_headline2", "Please make up the room.", font=DISPLAY, size=37, colour=INK, bold=True, alt="Page headline: Please make up the room."),
         dyn(P2, "c_subtitle2", "Subtitle P2 (text)", size=11),
         dyn(P2, "c_scatter_title", "Scatter Title (text)", size=13, colour=INK, font=DISPLAY, bold=True),
         tb(P2, "c_scatter_sub", "One dot per package the rules allow: three or more initiatives, at least one growth initiative, within $60M, kiosks only with the app. Raspberry: the package in focus  ·  plum: without the room refresh  ·  grey: with it.")]
    q = {"Category": {"projections": [proj_col("Package", "PackageID")]}, "X": {"projections": [proj_mea("Package Capex", "Capex")]},
         "Y": {"projections": [proj_mea("Package NPV (sel)", "NPV through 2032")]}, "Size": {"projections": [proj_mea("Package Point Size", "In focus")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2, title=True, start=0, end=60000000, extra={"titleText": text("Capex of the package, $M"), "titleFontFamily": text(BODY), "titleFontSize": num(10), "titleColor": color(INK2)}),
            "valueAxis": axis(BODY, 10, INK2, title=True, gridlines=True, grid_color=HAIR, extra={"titleText": text("NPV through 2032, $M (2025 dollars, 8%)"), "titleFontFamily": text(BODY), "titleFontSize": num(10), "titleColor": color(INK2)}),
            "dataPoint": [{"properties": {"fill": fv("Package Point Color")}, "selector": WILD}],
            "bubbles": [{"properties": {"bubbleSize": integer(-25)}}], "legend": legend(False), "categoryLabels": [{"properties": {"show": b(False)}}],
            # VERIFY: constant line shape (analytics pane); fallback: gridline at zero plus the subtitle sentence
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "style": enum("solid"), "position": enum("front"),
                                                    "displayName": text("worth its cost by 2032 above this line"), "dataLabelShow": b(True), "dataLabelText": enum("Name"), "dataLabelColor": color(INK2)}, "selector": {"id": "1"}}]}
    v.append(visual("hero_packages", "scatterChart", *at(P2, "hero_packages"), query=q, objects=objs,
                    vcos=vco(alt="Scatter of the 456 valid investment packages: capex on the horizontal axis, NPV through 2032 in the selected scenario on the vertical axis; the package in focus is the large raspberry dot", padding=0)))
    v.append(slicer("sl_scenario", *at(P2, "sl_scenario"), "Scenario", "Scenario", "Scenario", BODY, INK, INK2, SURFACE, ACCENT, single=True, horizontal=True, selected=["Expected"],
                    alt="Scenario: Low, Expected or High; every number on this page follows it", size=10))
    v.append(slicer("sl_package", *at(P2, "sl_package"), "PlanSelector", "Label", "Package in focus", BODY, INK, INK2, SURFACE, ACCENT, mode="Dropdown", single=True,
                    selected=["A · Highest NPV through 2032"], alt="Package in focus: one of the three shortlist rules, or any valid package", size=10))

    # state: shortlist
    v.append(dyn(P2, "c_short_title", "Shortlist Title (text)", size=13, colour=INK, font=DISPLAY, bold=True))
    heads = {"a": "A · Highest NPV through 2032", "b": "B · Most hotels with a guest-score effect, NPV at least zero", "c": "C · Highest NPV that includes the refresh of the ten oldest hotels"}
    for k in "abc":
        v.append(tile(f"z_tile_preset_{k}", f"tile_preset_{k}"))
        v.append(tb(P2, f"c_preset_{k}_head", heads[k], size=15, colour=INK, bold=True))
        v.append(dyn(P2, f"c_preset_{k}_mix", f"Preset {k.upper()} Mix (text)", size=11, colour=INK))
        K = k.upper()
        v.append(nums_card(f"c_preset_{k}_nums", [f"Preset {K} Capex", f"Preset {K} NPV (sel)", f"Preset {K} Range (text)", f"Preset {K} Run-rate (sel)"],
                           ["capex", "NPV, selected case", "NPV, Low to High, $M", "a year by 2032"], f"Preset {K}: capex, NPV, NPV range and 2032 run-rate"))
    v.append(dyn(P2, "c_uncertainty", "Uncertainty (text)", size=10))
    v.append(button("btn_open_plan", "Open the plan for the package in focus  →", "bm_p2_plan", True, "Button: open the plan for the package in focus"))

    # state: plan (hidden by default)
    v.append(dyn(P2, "c_plan_title", "Plan Title (text)", size=13, colour=INK, font=DISPLAY, bold=True))
    q = {"Category": {"projections": [proj_col("InvestmentProjects", "Short Name")]}, "Y": {"projections": [proj_mea("Focus Project NPV (sel)", "NPV through 2032")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2, gridlines=None), "valueAxis": axis(BODY, 10, INK2, gridlines=False),
            "sentimentColors": [{"properties": {"increaseFill": color(GOOD), "decreaseFill": color(BAD), "totalFill": color(INK), "otherFill": color(SLATE)}}],
            "labels": labels(True, BODY, 10, INK), "legend": legend(False)}
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
    # VERIFY: image size of the chip column (grid image height); fallback: Format > Image size 24 px in Desktop
    v.append(visual("tbl_plan_initiatives", "tableEx", *at(P2, "tbl_plan_initiatives"), query={"Values": {"projections": proj}}, objects=objs,
                    sort=sort_by_measure("Initiative Status (text)", desc=False),
                    vcos=vco(alt="Table of all ten Goodnight Inn initiatives, funded ones first: status in the package in focus, the page-1 finding each answers, capex, go-live month, 2032 run-rate, NPV and the dataset guest-score effect", padding=0)))
    ms = ["Focus Cumulative Net (Low)", "Focus Cumulative Net (Expected)", "Focus Cumulative Net (High)"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(ms[0], "Low"), proj_mea(ms[1], "Expected"), proj_mea(ms[2], "High")]}}
    objs = {"categoryAxis": axis(BODY, 10, INK2), "valueAxis": axis(BODY, 10, INK2, gridlines=True, grid_color=HAIR), "legend": legend(False),
            "dataPoint": series_colors({mref(m): ACCENT for m in ms}), "lineStyles": line_styles({mref(ms[0]): 1, mref(ms[1]): 2, mref(ms[2]): 1})}
    v.append(chart(P2, "ch_plan_cumulative", "lineChart", q, objs, "Line chart of the cumulative net impact of the package in focus 2027 to 2032 in the Low, Expected and High scenarios",
                   title="Cumulative net impact, $M  ·  Low to High", filters=[filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon2")]))
    v.append(card("c_plan_ops", *at(P2, "c_plan_ops"), ["Focus Rooms Added", "Focus Rooms Refreshed", "Focus Hotels Rated"], BODY, 16, INK, BODY, 10, INK2,
                  labels=["rooms added", "rooms refreshed", "hotels, guest effect"], alt="Operational impact of the package in focus: rooms added, rooms refreshed, hotels with a dataset guest-score effect"))
    v.append(dyn(P2, "c_plan_risk", "Plan Risk (text)", size=10))
    v.append(button("btn_back", "←  Back to the three packages", "bm_p2_shortlist", False, "Button: back to the three shortlist packages"))
    v.append(tb(P2, "z_footer2", FOOTER))
    return v


# ====================================================================== pages, bookmarks, resources
def page(name, display, visuals, bg_image, filters=None):
    p = {"$schema": PAGE_SCHEMA, "name": name, "displayName": display, "displayOption": "FitToPage", "height": LAYOUT["canvas"]["h"], "width": LAYOUT["canvas"]["w"],
         "objects": {"background": [{"properties": {
             "color": color(CANVAS), "transparency": num(0),
             # VERIFY: page background image shape; fallback: Format page > Canvas background > image, project/deliverables/backgrounds/<page>.png, Fit, 0 %
             "image": {"image": {"name": text(bg_image), "url": {"expr": {"ResourcePackageItem": {"PackageName": "RegisteredResources", "PackageType": 1, "ItemName": bg_image}}}, "scaling": text("Fit")}}}}]}}
    if filters:
        p["filterConfig"] = {"filters": filters}
    for vis in visuals:
        if state_of(name, vis["name"]) == "plan":
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
    v1, v2 = p1_visuals(), p2_visuals()
    for vis in v2:  # tiles belong to the shortlist state
        if vis["name"].startswith("z_tile_"):
            SLOT[P2][vis["name"]] = {"state": "shortlist"}
    pages = [page(P1, "The Brand Review", v1, "bg-p1-brand-review.png"),
             page(P2, "The Investment Strategy", v2, "bg-p2-investment-strategy.png",
                  filters=[filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_page_projects"), filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_page_brand")])]
    rep = write_report(OUT, NAME, "Goodnight Inn · opzet", pages, THEME, THEME_FILE)
    res = rep / "StaticResources" / "RegisteredResources"
    for pg in ("p1-brand-review", "p2-investment-strategy"):
        shutil.copyfile(BG / f"{pg}.png", res / f"bg-{pg}.png")
    rj = rep / "definition" / "report.json"
    report = json.loads(rj.read_text(encoding="utf-8"))
    for pk in report["resourcePackages"]:
        if pk["name"] == "RegisteredResources":
            pk["items"] += [{"name": f"bg-{pg}.png", "path": f"bg-{pg}.png", "type": "Image"} for pg in ("p1-brand-review", "p2-investment-strategy")]
    write_json(rj, report)
    bm = rep / "definition" / "bookmarks"
    write_json(bm / "bm_p2_shortlist.bookmark.json", bookmark("bm_p2_shortlist", "P2 Shortlist", "shortlist", v2))
    write_json(bm / "bm_p2_plan.bookmark.json", bookmark("bm_p2_plan", "P2 Plan", "plan", v2))
    write_json(bm / "bookmarks.json", {"$schema": BOOKMARKS_SCHEMA, "items": [{"name": "bm_p2_shortlist"}, {"name": "bm_p2_plan"}]})
    n1, n2 = len(v1), len(v2)
    core = sum(1 for v in v1 + v2 if v["visual"]["visualType"] in ("tableEx", "pivotTable", "clusteredBarChart", "lineChart", "scatterChart", "waterfallChart"))
    print(f"report written: {rep}  P1 {n1} visuals, P2 {n2} visuals ({sum(1 for v in v2 if v.get('isHidden'))} hidden in the plan state), {core} core chart/table visuals")


if __name__ == "__main__":
    main()
