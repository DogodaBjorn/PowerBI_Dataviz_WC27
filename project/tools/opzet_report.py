"""Writes the report set-up (opzet) as a PBIP report on the shared model. v4 of 2026-11-10: feedback round 4
(12-feedbackronde-4.md) on the D1 briefing (06-d1-briefing-opzet.md): P1 = headline, four benchmarked KPIs, findings
F1-F3 with one chart each, F4 where we are full; P2 = the package scatter and a right panel in three states.

Run from the repo root, after sketch_model.py and brand_canvas_v3.py (plan 11):
    python project/tools/opzet_report.py                   # writes project/pbip/GoodnightInn-opzet.pbip + .Report
    python project/tools/opzet_report.py --out DIR         # dry run elsewhere (validation outside project/pbip)
    python project/tools/opzet_report.py --state=alts      # a throwaway copy (…-alts) that OPENS in the alts state
    python project/tools/opzet_report.py --selector=native # the move selector as a native button slicer (fallback)

Source of truth:
  positions  project/design-prototypes/opzet-layout.json (the slot map, with the state of every slot, tile and card)
  bindings   this file (one function per visual, measures from project/tools/sketch_model.py)
  selector   project/deliverables/deneb-specs/dn_build_selector.json (written by project/tools/build_selector_spec.py)
  decisions  project/project-state/active/06-, 08-, 11- and 12-feedbackronde-4.md
Canvas 1920x1080; brand kit goodnight-inn-wakeup 3.1, night header with the night-glow canvas (plans 10 and 11;
theme: project/deliverables/theme.json, canvas: project/tools/brand_canvas_v3.py).

Two visible pages, both named after the contest's questions. P2 has three panel states swapped by display-only
bookmarks (bm_p2_rec / bm_p2_alts / bm_p2_build), reached through a tab bar:
  rec    the recommendation A: tile, where the NPV comes from, the cumulative chart (default)
  alts   B and C, considered and not recommended: two cards and a comparer against A across the bottom
  build  build your own plan: the Deneb move selector, your plan's numbers and waterfall, a comparer against A
In alts and build the scatter card shrinks: a bookmark cannot resize a visual, so a second, smaller scatter stack
(hero_s_packages*) is shown instead of the full one. The scenario lives in the Scenario slicer, so a bookmark never
changes it (fx-focus rules 1-2). Shapes not yet exercised in Desktop are marked VERIFY.
"""
import copy
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pbir_lib import (visual, textbox, card, write_report, vco, axis, legend, labels, series_colors, line_styles,  # noqa: E402
                      table_objects, proj_col, proj_mea, mref, filter_in, filter_measure_gt, sort_by_measure,
                      sort_by_column, b, num, integer, enum, text, color, mea, col, write_json, tag, PAGE_SCHEMA)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "project" / "pbip"
if len(sys.argv) > 2 and sys.argv[1] == "--out":
    OUT = Path(sys.argv[2])
NAME = "GoodnightInn-opzet"
STATES = ("rec", "alts", "build")
# --state=X: a throwaway copy (GoodnightInn-opzet-X) that opens in that P2 state, so a Desktop screenshot can check
# what a bookmark normally reveals. Never commit it. The CDP shots click the tabs instead (project/tools/desktop_shots).
OPEN_STATE = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--state=")), "rec")
assert OPEN_STATE in STATES, OPEN_STATE
if OPEN_STATE != "rec":
    NAME += f"-{OPEN_STATE}"
# the move selector: Deneb (Björn 10 Nov) or, if the Desktop spike fails, a native button slicer in the same slot
SELECTOR = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--selector=")), "deneb")
assert SELECTOR in ("deneb", "native"), SELECTOR
LAYOUT = json.loads((ROOT / "project" / "design-prototypes" / "opzet-layout.json").read_text(encoding="utf-8"))
THEME = json.loads((ROOT / "project" / "deliverables" / "theme.json").read_text(encoding="utf-8"))
THEME_FILE = "goodnight-inn-wakeup.json"
THEME["name"] = THEME_FILE  # the registered file name (pbir_lib / pbir_detect convention)
BG = ROOT / "project" / "deliverables" / "backgrounds"
DENEB_SPEC = ROOT / "project" / "deliverables" / "deneb-specs" / "dn_build_selector.json"
DENEB_GUID = "deneb7E15AEF80B9E4D4F8E12924291ECE89A"  # Deneb, AppSource edition (deneb.guide PBIR guide)

# Kit goodnight-inn-wakeup 3.1 (plan 10 D1, plan 11): Goodnight Inn is Coffee Blue, the sister brands Warm Grey,
# Tangerine only marks a signal. ACCENT is the text cut (Deep Coffee, 6.2:1 on white, white on it 6.2:1);
# ACCENT_MARK the series and marks (Coffee Blue, 3.7:1 on white: enough for a mark, not for small text).
CANVAS, SURFACE, INK, INK2, HAIR = "#F3F1EA", "#FFFFFF", "#12233D", "#4B5466", "#E3DFD3"
ACCENT, ACCENT_MARK, GOOD, BAD, SLATE = "#1763A8", "#2589D8", "#1763A8", "#A63F0E", "#8E897D"
SIGNAL_MARK = "#E05A22"  # Tangerine: the Low case, decreases, C and the plan being built in the comparers (never a brand identity)
TINT = "#EAF2FB"  # Ice, the kit's accent tint (sequential step 1)
# Text on the Night header zone (plan 10 D3): headline, masthead/subtitle, eyebrow. Contrast on the lightest pixel
# of the night-glow zone is checked by project/tools/a11y_check.py from backgrounds/zone-samples.json.
ZONE_TEXT, ZONE_MUTED, ZONE_EYEBROW = "#F7F5EE", "#C9D0DC", "#A9CDF0"
# Round 9 (Björn, 11 Nov): the tooltip banners are orange (brand_canvas_v3.tooltip, kit waiver of 11 Nov), so a tooltip reads
# as another surface than the page. Round 9b: the FLASHY Tangerine, Björn's choice; white text on it is 3.4:1, under the
# floor, so the kicker and the title are Night on it (4.7:1 on the band's darkest pixel; a11y_check reads the pixels).
TT_KICKER = INK
TT_TITLE = INK
# The font stacks Desktop itself writes for Segoe UI: wf_segoe-ui_* are the Power BI service's web fonts, so a
# browser without Segoe UI (a Mac under Publish-to-Web) still gets it; Arial as the last named fallback (kit 3.1).
DISPLAY = "'Segoe UI Semibold', wf_segoe-ui_semibold, helvetica, arial, sans-serif"
BODY = "'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif"
# feedback round 4: one line (plan 09 R4 kept in its short form; Keiningham et al. 2007, CREDITS.md)
# round 6 (Björn, 10 Nov): the source and the two real caveats; the R4 scoping line ("not shown: impressions, likes, NPS as a
# growth measure") left the canvas for the submission notes
FOOTER = "Source: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores weighted by survey responses; 2021 is a depressed base year."
KIT = ROOT / "design" / "brand-kits" / "goodnight-inn-wakeup" / "assets"
# The brand row (plan 11): the 3.1 lockup on the Night zone and an eyebrow in the former pay-off slot.
# Round 9 (Björn, 11 Nov): no section numbers (a listed AI tell, design-taste-frontend 9.F); a hotel pun says what the page
# is and the page name follows as its tagline, the line's one middle dot between them (pun, name).
EYEBROW = {"p1-brand-review": ("THE WAKE-UP CALL", "THE BRAND REVIEW"), "p2-investment-strategy": ("ROOM TO INVEST", "THE INVESTMENT STRATEGY")}
LOCKUP = "gi-lockup-reversed@2x.png"
# Kit type scale (brand.yaml 3.1 scale_pt 30 / 20 / 14 / 12 / 12): textboxes in px, cards and visual objects in pt.
# Floor 12 pt (16 px at 1920) for notes, axes, tables, slicers and tooltips alike (plan 11). S = small text in pt,
# SPX the same in px.
S = 12
SPX = 16
TITLE_PT = 14  # card titles (kit scale step 3)
BRANDS = [("GI", "Goodnight Inn"), ("PS", "P&K Select"), ("MO", "Maison d'Or"), ("PP", "Pebble & Pine")]
WILD = {"data": [{"dataViewWildcard": {"matchingOption": 1}}]}

SLOT = {p["name"]: {v["name"]: v for v in p["visuals"]} for p in LAYOUT["pages"]}
# FinalV2 phase 0 (plan 15 S6): Björn's layering pass in Desktop (11 Nov, saved 12 Nov as commit 1361f71) renumbered the
# z-order and tab order of every visual on P1 and P2; that file carries them, the generator applies them last, so a
# rebuild reproduces his save. A visual missing there keeps the generator's values.
LAYERING = json.loads((ROOT / "project" / "design-prototypes" / "opzet-layering.json").read_text(encoding="utf-8"))


def layered(page_name, visuals):
    for v in visuals:
        o = LAYERING.get(page_name, {}).get(v["name"])
        if o:
            v["position"]["z"], v["position"]["tabOrder"] = o["z"], o["tabOrder"]
    return visuals
PAGES = {p["name"]: p for p in LAYOUT["pages"]}


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
    """Field-value text (title text, axis ends, image URLs bound to a measure; rendered 7 and 9 Nov)."""
    return {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}}}


def at(page, name):
    s = SLOT[page][name]
    return s["x"], s["y"], s["w"], s["h"], s["z"], s["tab"]


def states_of(page, name):
    """The states a visual is shown in (a list), or None when it is always visible. Visuals derived from a slot
    (kpi_occ_label from kpi_occ, hero_packages_hover from hero_packages) share the slot's state; card frames
    (z_card_<id>) and tiles (z_tile_<id>) read the layout's cards and tiles."""
    pg = PAGES[page]
    if name.startswith("z_card_"):
        entry = next((c for c in pg.get("cards", []) if c["id"] == name[len("z_card_"):]), {})
    elif name.startswith("z_tile_"):
        entry = next((t for t in pg.get("tiles", []) if t["id"] == name[len("z_tile_"):]), {})
    else:
        base = name if name in SLOT[page] else name.rsplit("_", 1)[0]
        entry = SLOT[page].get(base, {})
    st = entry.get("state")
    if st is None:
        return None
    return [st] if isinstance(st, str) else list(st)


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


def tb(page, name, txt, font=BODY, size=SPX, colour=INK2, bold=False, align="left", alt=None, runs=None):
    """A static text box; it reads its own words unless told otherwise (plan 11). runs: coloured runs instead of txt."""
    return textbox(name, *at(page, name), [runs or [(txt, font, size, colour, bold)]], align=align, alt=alt or txt)


def dyn(page, name, measure, size=S, colour=INK2, font=BODY, bold=False, align="left", alt_measure=None, colour_measure=None, fill_measure=None):
    """A cardVisual that shows one text measure as copy (dynamic title or subtitle). Its alt text is the same measure
    (or alt_measure), so a screen reader hears the sentence on the canvas, not the measure's name (plan 11).
    fill_measure (round 5): the visual's own background from a measure, paired branch for branch with colour_measure
    (the budget alarm band: Tangerine with white text while over the budget, white with Night text otherwise)."""
    v = card(name, *at(page, name), [measure], font, size, colour, align=align)
    if bold:
        v["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    if colour_measure:
        v["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv(colour_measure)
    if fill_measure:
        vc = v["visual"]["visualContainerObjects"]
        vc["background"] = [{"properties": {"show": b(True), "color": fv(fill_measure), "transparency": num(0)}}]
        vc["padding"] = [{"properties": {"top": num(0), "bottom": num(0), "left": num(12), "right": num(12)}}]
    return bind_alt(v, alt_measure or measure)


def page_tooltip(section):
    """A report-page tooltip binding (visualContainerObjects.visualTooltip), the shape the scatter's hover layer uses."""
    return [{"properties": {"show": b(True), "type": enum("Canvas"), "section": text(section)}}]


def chart(page, name, vtype, query, objects, alt, title=None, title_measure=None, filters=None, sort=None, alt_measure=None, tooltip_page=None, muted=False):
    # muted (FinalV2, plan 15 S2): a quiet 12 pt Dusk line instead of the bold title, for the build waterfall's waiting note
    vcos = vco(title=title or ("x" if title_measure else None), title_font=BODY if muted else DISPLAY, title_size=S if muted else TITLE_PT, title_color=INK2 if muted else INK, alt=alt, padding=0)
    if title_measure:
        vcos["title"][0]["properties"]["text"] = mtext(title_measure)
        vcos["title"][0]["properties"]["bold"] = b(not muted)
    if tooltip_page:  # round 6: the F3 and F4 charts open a detail page on hover
        vcos["visualTooltip"] = page_tooltip(tooltip_page)
    v = visual(name, vtype, *at(page, name), query=query, objects=objects, vcos=vcos, filters=filters, sort=sort)
    return bind_alt(v, alt_measure) if alt_measure else v


# ====================================================================== P1 The Brand Review
P1 = "p1-brand-review"


def gi_filter():
    return filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_gi")


def kpi_cell(slot, label, value_measure, context_measure, alt_measure, colour_measure):
    """One KPI of the band: a label, the value and one comparison (DC-051), stacked inside the slot (24 + 40 + 24 px).
    One tab stop per KPI (plan 11): the value reads label, value and comparison aloud (Alt KPI ... (text)); the label
    and the context line are the same words on the canvas, so they leave the tab order. Round 4: the context line's
    colour comes from a measure (Burnt Tangerine where the news is bad, Deep Coffee where it is best of four)."""
    x, y, w, h, z, tab = at(P1, slot)
    lab = textbox(f"{slot}_label", x, y, w, 24, z, tab, [[(label, BODY, SPX, INK2, False)]])
    val = card(slot, x, y + 24, w, 48, z, tab + 1, [value_measure], DISPLAY, 28, INK)
    val["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    ctx = card(f"{slot}_ctx", x, y + 72, w, 24, z, tab + 2, [context_measure], BODY, S, INK2)
    ctx["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv(colour_measure)
    return [decorative(lab, 100 + tab), bind_alt(val, alt_measure), decorative(ctx, 200 + tab)]


_KICK = [0]


def kicker(page, name, txt):
    """The kit's eyebrow on a white card at the 12 pt floor, out of the tab order: the title after it reads the
    kicker's words first (Alt F# Title (text)). Round 4, a little more orange: the finding's code (F1) in Burnt
    Tangerine (6.2:1 on white), the words in Deep Coffee."""
    _KICK[0] += 1
    code, _, rest = txt.partition("  ·  ")
    runs = [(code, DISPLAY, SPX, BAD, False), ("  ·  " + rest, DISPLAY, SPX, ACCENT, False)] if rest else [(txt, DISPLAY, SPX, ACCENT, False)]
    return decorative(tb(page, name, txt, runs=runs), 600 + _KICK[0])


def night_kicker(page, name, txt):
    """Round 7: the kicker on a tooltip's banner, the page's own eyebrow idea, out of the tab order; the title after it
    carries the words. Round 9: on the orange banner, in TT_KICKER."""
    _KICK[0] += 1
    return decorative(tb(page, name, txt, font=DISPLAY, size=SPX, colour=TT_KICKER), 600 + _KICK[0])


def title(page, name, measure, alt_measure=None):
    return dyn(page, name, measure, size=TITLE_PT, colour=INK, font=DISPLAY, alt_measure=alt_measure)


def p1_visuals():
    # headline and subtitle as cards, like P2's, so the two headers sit on one grid (REVIEW p2)
    # on the night zone (plan 10 D3): masthead and subtitle in ZONE_MUTED (10.2:1 on Night), the headline in ZONE_TEXT
    # 12 Nov evening (Björn): the masthead line said nothing; its slot holds the header line (header_line)
    v = [dyn(P1, "z_headline", "Headline P1 (text)", size=28, colour=ZONE_TEXT, font=DISPLAY),
         dyn(P1, "c_subtitle", "Subtitle P1 Briefing (text)", size=S, colour=ZONE_MUTED)]

    # the KPI band: four cells in one card; values are text measures, one formatter with the context line (REVIEW M7)
    v += kpi_cell("kpi_occ", "Occupancy", "KPI Occupancy GI (text)", "KPI Occupancy Context (text)", "Alt KPI Occupancy (text)", "KPI Occupancy Context Color")
    v += kpi_cell("kpi_margin", "Operating margin after commissions", "KPI Margin after GI (text)", "KPI Margin after Context (text)", "Alt KPI Margin after (text)", "KPI Margin after Context Color")
    v += kpi_cell("kpi_ota", "Room revenue booked through online agencies", "KPI OTA GI (text)", "KPI OTA Context (text)", "Alt KPI OTA (text)", "KPI OTA Context Color")
    # plan 09 R2: NPS as a guest-quality signal, not the brand's one number (Keiningham et al. 2007; CREDITS.md).
    # Round 4 (Björn 10 Nov): the context line says it is still positive but falling every year.
    v += kpi_cell("kpi_nps", "Guest quality: net promoter score", "KPI NPS GI (text)", "KPI NPS Context (text)", "Alt KPI NPS (text)", "KPI NPS Context Color")

    # F1 the margin: before vs after commissions, Goodnight Inn only; the gap between the lines is the channels' take
    v += [kicker(P1, "c_f1_kicker", "F1  ·  THE MARGIN"), title(P1, "c_f1_title", "F1 Title (text)", "Alt F1 Title (text)")]
    v.append(f1_chart(P1, "ch_f1_margin"))
    v.append(dyn(P1, "c_f1_note", "F1 Note (text)"))

    # F2 the middleman: OTA share for the four brands, and the folio (one 2025 room night by channel)
    v += [kicker(P1, "c_f2_kicker", "F2  ·  THE MIDDLEMAN"), title(P1, "c_f2_title", "F2 Title (text)", "Alt F2 Title (text)")]
    v.append(f2_chart(P1, "ch_f2_ota"))
    v.append(f2_folio(P1, "tbl_f2_folio"))
    v.append(dyn(P1, "c_f2_note", "F2 Note (text)"))

    # F3 the fading welcome: NPS 2025 by years since the last renovation (dated hotels only); a bar opens the band's detail
    v += [kicker(P1, "c_f3_kicker", "F3  ·  THE FADING WELCOME"), title(P1, "c_f3_title", "F3 Title (text)", "Alt F3 Title (text)")]
    v.append(f3_chart(P1, "ch_f3_age", tooltip_page=TT_F3))
    v.append(dyn(P1, "c_f3_note", "F3 Note (text)"))

    # F4 where we are full; a bar opens the hotel's detail
    v += [kicker(P1, "c_f4_kicker", "F4  ·  WHERE WE ARE FULL"), title(P1, "c_f4_title", "F4 Title (text)", "Alt F4 Title (text)")]
    v.append(f4_types(P1, "c_f4_types"))
    v.append(f4_chart(P1, "ch_f4_fullest", tooltip_page=TT_F4))
    v.append(tb(P1, "z_footer", FOOTER, alt="Source: Pillow & Key Group dataset. Guest scores weighted by survey responses; 2021 is a depressed base year."))
    # 12 Nov evening: the hover signifier on the two cards with hover detail, the hint and the Definitions chip in the footer row
    v += [badge(P1, "bdg_f3", 3), badge(P1, "bdg_f4", 4)] + header_line(P1, "", 1)
    return v


YEARS = lambda: filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")  # noqa: E731
SERIES_LABELS_RIGHT = [{"properties": {"show": b(True), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2), "textSize": num(S), "seriesFontFamily": text(BODY)}}]


def small_axis_type(small):
    """Round 9: in a 496 px tooltip chart a numeric year axis skipped 2021, 2023 and 2025; a categorical axis labels every year."""
    return {"axisType": enum("Categorical")} if small else None


def f1_chart(page, slot, small=False):
    ms = ["Trend Margin before GI", "Trend Margin after GI"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(ms[0], "Before commissions"), proj_mea(ms[1], "After commissions")]}}
    # 30 % to 50 %: from 25 % an empty band sat between the lowest gridline and the years (REVIEW p4)
    objs = {"categoryAxis": axis(BODY, S, INK2, extra=small_axis_type(small)), "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, start=0.3, end=0.5, extra={"labelPrecision": integer(0)}),
            # the lines named at their ends in Dusk, as on F2 (pass-3 review: a legend of a grey and a blue dot was colour
            # only, 1.07:1 between them)
            # round 10: in the 416 px tooltip chart the line-end names pushed the years into a slant; there the legend sits on top
            "legend": legend(True, BODY, S, INK2, "Top") if small else legend(False),
            "seriesLabels": [{"properties": {"show": b(not small), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2), "textSize": num(S), "seriesFontFamily": text(BODY)}}],
            "dataPoint": series_colors({mref(ms[0]): SLATE, mref(ms[1]): ACCENT_MARK}), "lineStyles": line_styles({mref(ms[0]): 2, mref(ms[1]): 3})}
    return chart(page, slot, "lineChart", q, objs, None, filters=[YEARS()], alt_measure="Alt F1 Chart (text)")


def f2_chart(page, slot, small=False):
    ms = [f"Trend OTA {c}" for c, _ in BRANDS]
    names = [nm for _, nm in BRANDS]
    # round 10: in the chip tooltip the three sister brands are one line (four names fit neither a legend nor the line ends at
    # 416 px). FinalV2 (plan 15 S1, the decided fallback): on P1 as well. With the legend on top the four names fit, but the
    # three sisters share one Warm Grey (kit D6), so three identical grey dots could not tell the lines apart (REVIEW m3, the
    # reason the line ends once carried the names); one line "The other three brands" is the same chart as the tooltip's.
    ms, names = [ms[0], "Trend OTA Sisters"], [names[0], "The other three brands"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m, nm) for m, nm in zip(ms, names)]}}
    # the line ends carry the names, as in the comp: a legend of three identical grey dots could not be decoded (REVIEW m3).
    # The names in Dusk, not in the line's colour: Warm Grey (3.5:1) and Coffee Blue (3.7:1) fail 4.5:1 for 12 pt text
    # (plan 11); the line next to each name still ties them.
    objs = {"categoryAxis": axis(BODY, S, INK2, extra=small_axis_type(small)), "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, extra={"labelPrecision": integer(0)}),
            # FinalV2 (plan 15 S1): on P1 too the legend sits on top and the line ends carry no names: at the line ends Maison d'Or
            # collided with P&K Select and one line went nameless (review 12 Nov); the tooltip chart had the same cure in round 10
            "legend": legend(True, BODY, S, INK2, "Top"),
            "seriesLabels": [{"properties": {"show": b(False)}}],
            "dataPoint": series_colors({mref(ms[0]): ACCENT_MARK, **{mref(m): SLATE for m in ms[1:]}}),
            "lineStyles": line_styles({mref(ms[0]): 3, **{mref(m): 1.5 for m in ms[1:]}})}
    return chart(page, slot, "lineChart", q, objs, None, filters=[YEARS()], alt_measure="Alt F2 Chart (text)")


def f2_folio(page, slot):
    # text measures: one formatter, and 'keeps' is the difference of the two shown amounts (REVIEW M7, M8)
    fol = ("Folio OTA Guest (text)", "Folio Direct Guest (text)")
    proj = [proj_col("FolioLine", "Line", display="One room night, 2025"), proj_mea(fol[0], "Via an online agency"), proj_mea(fol[1], "Direct, web and app")]
    colfmt = [{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": mref(m)}} for m in fol]
    # row padding 0: at 12 pt three rows and the header must fit 96 px without a scrollbar (renders 9 Nov)
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=0, header_size=S, column_formatting=colfmt)
    # no explicit sort: FolioLine[Line] is sorted by its Sort column in the model, and an explicit sort drew an arrow
    # under 'One room night, 2025' (REVIEW m5)
    t = visual(slot, "tableEx", *at(page, slot), query={"Values": {"projections": proj}}, objects=objs, filters=[gi_filter()], vcos=vco(padding=0))
    return bind_alt(t, "Alt F2 Folio (text)")


def f3_chart(page, slot, tooltip_page=None):
    q = {"Category": {"projections": [proj_col("Hotels", "Renovation Age Label", display="Years since the last renovation")]}, "Y": {"projections": [proj_mea("NPS 2025 (signed)", "NPS 2025")]}}
    objs = {"categoryAxis": axis(BODY, S, INK), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False),
            "dataPoint": [{"properties": {"fill": fv("Age Band Color")}, "selector": WILD}], "labels": labels(True, BODY, 12, INK), "legend": legend(False),
            # the zero line the bars hang from (REVIEW m4); same object shape as the scatter's, which Desktop rendered
            # FinalV2 (plan 15 N4): 2 px, a line and not a bar (Björn, 7 Nov: thin, in Dusk); the width key as on the scatter's line
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "width": num(2), "style": enum("solid"), "position": enum("front"),
                                                    "dataLabelShow": b(False)}, "selector": {"id": "1"}}]}
    return chart(page, slot, "clusteredColumnChart", q, objs, None,
                 filters=[gi_filter(), filter_in("Hotels", "Renovation Age Sort", [1, 2, 3], "flt_dated")], sort=sort_by_column("Hotels", "Renovation Age Label"),
                 alt_measure="Alt F3 Chart (text)", tooltip_page=tooltip_page)


def f4_types(page, slot, size=21):
    c = card(slot, *at(page, slot), ["Occupancy Airport GI (text)", "Occupancy City GI (text)", "Occupancy Highway GI (text)"], DISPLAY, size, INK, BODY, S, INK2,
             labels=["Airport hotels", "City hotels", "Highway hotels"])
    return bind_alt(c, "Alt F4 Types (text)")


def f4_chart(page, slot, tooltip_page=None, horizontal=False):
    """horizontal (round 9): in the 496 px chip tooltip the seven names truncated under columns; as bars they read in full."""
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Occupancy % 2025", "Occupancy 2025")]}}
    # axis from zero (never truncate a bar axis, CP-066); end 1.3 leaves room for the labels above the 90 % bars (pass 3)
    objs = {"categoryAxis": axis(BODY, S, INK), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, start=0, end=1.3),
            "dataPoint": [{"properties": {"fill": fv("Hotel Bar Color")}, "selector": WILD}], "labels": labels(True, BODY, S, INK, position="OutsideEnd"), "legend": legend(False)}
    # the airport hotels are Coffee Blue and every one of their names ends in "Airport", so colour is not the only carrier
    return chart(page, slot, "clusteredBarChart" if horizontal else "clusteredColumnChart", q, objs, None,
                 filters=[gi_filter(), topn_filter("Hotels", "Hotel Short Name", 7, "Occupancy % 2025", "flt_top7")], sort=sort_by_measure("Occupancy % 2025"),
                 alt_measure="Alt F4 Chart (text)", tooltip_page=tooltip_page)


# ====================================================================== round 6: the findings on P2 and the hover detail pages
TT_F3, TT_F4 = "tt-f3-band", "tt-f4-hotel"
TT_YEAR = "tt-year"  # round 9: the one designed tooltip the three cumulative charts share
TT_GLOSS = "tt-glossary"  # 12 Nov evening (Björn): the definitions page behind the Definitions chip in the footer row of both pages
FINDINGS = (("1", "The margin"), ("2", "The middleman"), ("3", "The fading welcome"), ("4", "Where we are full"))


def finding_page_visuals(k, nm):
    """One finding's tooltip page: on the banner the kicker (code and name) and the headline; in the card the chart
    P1 draws (the same builder) and the note (F4: the three occupancy figures instead)."""
    pg = f"tt-f{k}"
    v = [night_kicker(pg, "ttf_kicker", f"F{k}  ·  {nm.upper()}"),
         dyn(pg, "ttf_title", f"F{k} Title (text)", size=TITLE_PT, colour=TT_TITLE, font=DISPLAY, alt_measure=f"Alt F{k} Title (text)")]
    if k == "1":
        v.append(f1_chart(pg, "ttf_chart", small=True))
    elif k == "2":
        v.append(f2_chart(pg, "ttf_chart", small=True))
    elif k == "3":
        v.append(f3_chart(pg, "ttf_chart"))
    else:
        v.append(f4_types(pg, "ttf_types", size=18))
        v.append(f4_chart(pg, "ttf_chart", horizontal=True))
    if k != "4":
        v.append(dyn(pg, "ttf_note", f"F{k} Note (text)", colour=INK))
    return v


def line_pair(page, slot, cat_table, cat_col, own, brand, own_label, brand_label, filters, sort=None, alt_measure=None, start=None, end=None, categorical=True):
    """A two-line chart: the hovered band or hotel in Night (the focus), the brand in Coffee Blue (FinalV2, plan 15 S3: the
    one colour Goodnight Inn has everywhere, kit D6), the names in a legend on top."""
    q = {"Category": {"projections": [proj_col(cat_table, cat_col, active=True)]}, "Y": {"projections": [proj_mea(own, own_label), proj_mea(brand, brand_label)]}}
    objs = {"categoryAxis": axis(BODY, S, INK2, extra={"axisType": enum("Categorical")} if categorical else None),  # round 10: every year labelled at 416 px
            # FinalV2: the value axis is back (in round 10 it had slipped into the comment above and the chart fell to defaults)
            "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, start=start, end=end, extra={"labelPrecision": integer(0)}),
            # round 10: the legend on top (the line-end names left a 12-month axis with a scrollbar at 416 px)
            "legend": legend(True, BODY, S, INK2, "Top"), "seriesLabels": [{"properties": {"show": b(False)}}],
            "dataPoint": series_colors({mref(own): INK, mref(brand): ACCENT_MARK}), "lineStyles": line_styles({mref(own): 2.5, mref(brand): 1.5})}
    return chart(page, slot, "lineChart", q, objs, None, filters=filters, sort=sort, alt_measure=alt_measure)


def detail_page_visuals(which):
    """The F3 band page and the F4 hotel page: the kicker and the band or hotel on the banner; a card with three
    figures and the brand's under them; a card with a titled two-line chart against the brand and one closing line
    (weakest guest scores / who fills the hotel)."""
    if which == TT_F3:
        head, nums, labels_, alt_nums, vs, foot = ("Band Header (text)", ["NPS 2025 (signed)", "Occupancy % 2025", "RevPAR 2025"], ["NPS 2025", "occupancy 2025", "RevPAR 2025"],
                                                  "Alt Band Nums (text)", "Band vs Brand (text)", "Weakest Scores (text)")
        ch_title = "NPS by year, this band against the brand"
        ch = line_pair(which, "ttd_chart", "Date", "Year", "NPS Band (line)", "NPS Brand (line)", "This band", "Goodnight Inn", [YEARS()], alt_measure="Alt NPS Band Line (text)")
    else:
        head, nums, labels_, alt_nums, vs, foot = ("Hotel Header (text)", ["Occupancy % 2025", "ADR 2025", "RevPAR 2025"], ["occupancy 2025", "ADR 2025", "RevPAR 2025"],
                                                  "Alt Hotel Nums (text)", "Hotel vs Brand (text)", None)  # FinalV2 N6: no room-nights line (answers no decision)
        ch_title = "Occupancy by month 2025, this hotel against the brand"
        # round 7: month letters on the axis (a 496 px chart rotated the three-letter names)
        ch = line_pair(which, "ttd_chart", "Date", "Month Letter", "Occupancy Hotel (line)", "Occupancy Brand (line)", "This hotel", "Goodnight Inn",
                       [filter_in("Date", "Year", [2025], "flt_2025")], sort=sort_by_column("Date", "Month Letter"), alt_measure="Alt Occupancy Hotel Line (text)", start=0.5, end=1.0, categorical=False)
    v = [night_kicker(which, "ttd_kicker", "F3  ·  THE FADING WELCOME" if which == TT_F3 else "F4  ·  WHERE WE ARE FULL"),
         dyn(which, "ttd_head", head, size=TITLE_PT, colour=TT_TITLE, font=DISPLAY)]
    n = card("ttd_nums", *at(which, "ttd_nums"), nums, DISPLAY, 18, INK, BODY, S, INK2, labels=labels_)
    v.append(bind_alt(n, alt_nums))
    v.append(dyn(which, "ttd_vs", vs))
    v.append(tb(which, "ttd_chart_title", ch_title, font=DISPLAY, size=SPX, colour=INK, alt=ch_title))
    v.append(ch)
    if foot:
        v.append(dyn(which, "ttd_foot", foot, colour=INK))
    return v


def extra_tooltip_pages():
    """The six round-6 tooltip pages in the round-7 skin (their own night scene, the kicker and title on the banner,
    the content in cards), Goodnight Inn as a page filter on the two detail pages (the hovered bar brings the band or
    the hotel, not the brand)."""
    out = []
    for k, nm in FINDINGS:
        pg = f"tt-f{k}"
        out.append(page(pg, pg, finish(no_card_fill(scene_visual(pg) + card_frames(pg) + finding_page_visuals(k, nm))), tooltip=True))
    for pg in (TT_F3, TT_F4):
        out.append(page(pg, pg, finish(no_card_fill(scene_visual(pg) + card_frames(pg) + detail_page_visuals(pg))), tooltip=True,
                        filters=[filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_tt_brand")]))
    out.append(page(TT_YEAR, TT_YEAR, finish(no_card_fill(scene_visual(TT_YEAR) + card_frames(TT_YEAR) + year_page_visuals())), tooltip=True))
    out.append(page(TT_GLOSS, TT_GLOSS, finish(no_card_fill(scene_visual(TT_GLOSS) + card_frames(TT_GLOSS) + glossary_page_visuals())), tooltip=True))
    return out


# 12 Nov evening (Björn): the definitions behind the Definitions chip. The short words of both pages, one line each, in the
# report's own words (the subtitle of P2 already defines NPV in situ; this is the place to look them all up). Years only, no
# typed figures: the rate and the budget live in the model and on the pages.
GLOSSARY = (("NPV", "net present value: benefits minus capex and disruption through 2032, in 2025 dollars at the organisers' rate."),
            ("Capex", "the one-off investment a move takes; the brand's budget caps what a plan may spend."),
            ("Run-rate", "the operating profit a move adds in a full year once it is live, measured in 2032."),
            ("Pays back, break-even", "the first year the cumulative net impact, undiscounted, is above zero."),
            ("Low, Expected, High", "the organisers' three cases for every move; every number on page 2 follows the case in view."),
            ("NPS", "net promoter score: promoters minus detractors among surveyed guests, weighted by responses."),
            ("ADR", "average daily rate: room revenue per room night sold."),
            ("RevPAR", "revenue per available room: room revenue per room night available, sold or not."),
            ("OTA, online agencies", "booking sites that take a commission on every room night they bring."))


def glossary_page_visuals():
    pg = TT_GLOSS
    x, y, w, h, z, tab = at(pg, "ttg_list")
    paras = [[(term, DISPLAY, SPX, INK, False), ("  " + what, BODY, SPX, INK2, False)] for term, what in GLOSSARY]
    lst = textbox("ttg_list", x, y, w, h, z, tab, paras, alt="The definitions of the short words on these pages, one line each")
    return [night_kicker(pg, "ttg_kicker", "DEFINITIONS"),
            tb(pg, "ttg_title", "The terms on these pages", font=DISPLAY, size=19, colour=INK),
            lst]


def year_page_visuals():
    """Round 9: the one designed tooltip for the three cumulative charts (Björn: the default tooltip is off brand; a new
    page only where it adds something, and a year's values are reachable by hover alone). On the banner the kicker and
    the year; a card with A in the three cases; a card with A, B, C and the plan being built in the case in view."""
    pg = TT_YEAR
    a = card("tty_a_nums", *at(pg, "tty_a_nums"), ["TT Year A Low (text)", "TT Year A Expected (text)", "TT Year A High (text)"], DISPLAY, 18, INK, BODY, S, INK2,
             labels=["Low case", "Expected case", "High case"])
    al = card("tty_all_nums", *at(pg, "tty_all_nums"), ["TT Year A (text)", "TT Year B (text)", "TT Year C (text)", "TT Year Plan (text)"], DISPLAY, 18, INK, BODY, S, INK2,
              labels=["A", "B", "C", "Your plan"])
    return [night_kicker(pg, "tty_kicker", "CUMULATIVE NET IMPACT, $M"),
            dyn(pg, "tty_title", "TT Year Title (text)", size=TITLE_PT, colour=TT_TITLE, font=DISPLAY),
            tb(pg, "tty_a_title", "A in the three cases", font=DISPLAY, size=SPX, colour=INK),
            bind_alt(a, "Alt TT Year A (text)"),
            dyn(pg, "tty_all_title", "TT Year All Title (text)", size=S, colour=INK, font=DISPLAY),
            bind_alt(al, "Alt TT Year All (text)")]


# ====================================================================== P2 The Investment Strategy
P2 = "p2-investment-strategy"


HOVER_ACCENT, HOVER_SHEET = INK, HAIR  # theme colours only (pbir_detect theme-color-drift): white on Night, Night on Seam


def button(name, label, bookmark, filled, alt, label_measure=None):
    """actionButton: shape copied from a Desktop-rendered button (hp-world-champs btn_nav_1): 'show' sits WITHOUT a
    selector, the state formatting under {"id": "default"}; with 'show' inside the selector the text did not render
    (7 Nov). Hover and selected (pressed) states set explicitly (catalog selectors default / hover / selected): the Back
    button's hover fill went dark under dark text, 1.4:1 (REVIEW M1). Filled: white on Deep Coffee (6.2:1), white on
    Night when hovered (15.8:1); outline: Night text on the Seam grey (13.9:1)."""
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


# The tab bar (round 4): three tabs over the panel, each drawn twice (its active and its inactive look) and shown by
# the bookmarks, so the current state is always visible. Labels without the kit's middle dot: the a11y check needs the
# visible label inside the spoken name letter for letter.
TABS = [("rec", "Recommended: A", "the recommendation, package A"),
        ("alts", "Considered: B and C", "the two packages considered and not recommended, B and C"),
        ("build", "Build your own", "build your own plan from the ten moves")]


def tab_bar():
    out = []
    for key, label, what in TABS:
        spoken = re.sub(r"[^A-Za-z ]", "", label)  # the visible label inside the spoken name (WCAG 2.5.3, a11y_check)
        out.append(button(f"tab_{key}_on", label, f"bm_p2_{key}", True, f"{spoken}, the current view: {what}"))
        out.append(button(f"tab_{key}_off", label, f"bm_p2_{key}", False, f"{spoken}: show {what}"))
    return out


def button_slicer(name, table, column, selected, alt, cols, size=S, rows=1, multi=False):
    """The house-style toggle (08-verbeterplan V5/S1, brand-guide section 6 'scenario toggle'): a button slicer whose
    tiles are thin rounded outlines on white, the selected one Night with white text. State ids as the built-in
    themes write them (interaction:hover, selection:selected). Rendered 7 and 9 Nov."""
    x, y, w, h, z, tab = at(P2, name)
    st = lambda i: {"id": i}  # noqa: E731
    radius = (h // rows) // 2 if rows > 1 else h // 2
    objs = {
        "shapeCustomRectangle": [{"properties": {"tileShape": enum("rectangleRoundedByPixel"), "rectangleRoundedCurve": integer(radius)}, "selector": st("default")}],
        "layout": [{"properties": {"rowCount": integer(rows), "columnCount": integer(cols), "maxTiles": integer(rows * cols), "cellPadding": integer(8)}}],
        "fillCustom": [{"properties": {"show": b(True), "fillColor": color(SURFACE), "transparency": num(0)}, "selector": st("default")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:hover")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:press")},
                       {"properties": {"fillColor": color(INK)}, "selector": st("selection:selected")}],
        "outline": [{"properties": {"show": b(True), "lineColor": color(INK2), "weight": num(1), "transparency": num(0)}, "selector": st("default")},
                    {"properties": {"lineColor": color(INK)}, "selector": st("selection:selected")}],
        "value": [{"properties": {"show": b(True), "fontFamily": text(BODY), "fontSize": num(size), "fontColor": color(INK), "bold": b(False),
                                  "horizontalAlignment": text("center" if rows == 1 else "left"), "verticalAlignment": text("middle")}, "selector": st("default")},
                  {"properties": {"fontColor": color(SURFACE), "bold": b(True)}, "selector": st("selection:selected")}],
        "label": [{"properties": {"show": b(False)}, "selector": st("default")}],
        # tile text padding: the theme's default (6 top, 8 bottom) clipped the descenders at 40 px (render 7 Nov)
        "padding": [{"properties": {"paddingSelection": text("Custom"), "topMargin": integer(2), "bottomMargin": integer(2), "leftMargin": integer(8), "rightMargin": integer(8)}, "selector": st("default")}],
        "selectionIcon": [{"properties": {"show": b(False)}, "selector": st("default")}],
        "selection": [{"properties": {"singleSelect": b(not multi), "strictSingleSelect": b(not multi), "selectAllCheckboxEnabled": b(False)}}],
    }
    if selected is not None:
        objs["general"] = [{"properties": {"filter": {"filter": {
            "Version": 2, "From": [{"Name": "s", "Entity": table, "Type": 0}],
            "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "s"}}, "Property": column}}],
                                            "Values": [[{"Literal": {"Value": f"'{selected}'"}}]]}}}]}}}}]
    vcos = vco(alt=alt, padding=0)
    return visual(name, "advancedSlicerVisual", x, y, w, h, z, tab, query={"Values": {"projections": [proj_col(table, column)]}}, objects=objs, vcos=vcos)


def image_file(name, x, y, w, h, z, tab, f, alt):
    """An image visual showing a registered resource (logo, vignette). Shape from the powerbi-report-author catalog."""
    objs = {"image": [{"properties": {"sourceType": text("image"), "sourceFile": {"image": {
                "name": text(f), "url": {"expr": {"ResourcePackageItem": {"PackageName": "RegisteredResources", "PackageType": 1, "ItemName": f}}}, "scaling": text("Fit")}}}}],
            "imageScaling": [{"properties": {"imageScalingType": text("Fit")}}]}
    return visual(name, "image", x, y, w, h, z, tab, objects=objs, vcos=vco(alt=alt, padding=0))


def image_measure(page, name, measure, alt):
    """An image visual whose URL is a measure (an SVG data URI): the brand's state chip (rendered 7 Nov)."""
    x, y, w, h, z, tab = at(page, name)
    objs = {"image": [{"properties": {"sourceType": text("imageUrl"), "sourceUrl": mtext(measure), "fit": text("Fit")}}]}
    return visual(name, "image", x, y, w, h, z, tab, objects=objs, vcos=vco(alt=alt, padding=0))


def badge(page, name, i):
    """The hover signifier (12 Nov evening, Björn; a signifier in Don Norman's sense, CREDITS.md): Power BI never changes the
    cursor over a visual that opens a report-page tooltip, so a 16 px Tangerine ring-i (Info Badge SVG) sits at the top right
    of every such visual, and nowhere else, so the mark keeps its meaning; the footer-row hint (Info Hint SVG) names it once.
    Decorative. Under a chip it sits BELOW the chip (its card is transparent), so the chip, not the badge, takes the hover."""
    return decorative(image_measure(page, name, "Info Badge SVG", None), 700 + i)


def hover_word(page, name, measure, tooltip_page, alt_measure, align="center"):
    """A word on the Night banner that opens a report-page tooltip (12 Nov evening, Björn: the footer chips cluttered the
    page while the masthead said nothing): a cardVisual in the eyebrow's light blue, no pill, the tooltip bound to it."""
    v = card(name, *at(page, name), [measure], DISPLAY, S, ZONE_EYEBROW, align=align)
    v["visual"]["visualContainerObjects"]["padding"] = [{"properties": {"top": num(0), "bottom": num(0), "left": num(0), "right": num(0)}}]
    v["visual"]["visualContainerObjects"]["visualTooltip"] = page_tooltip(tooltip_page)
    return bind_alt(v, alt_measure)


def header_line(page, sfx, i):
    """The header line in the masthead's slot, right-aligned on the Night banner: the hint (the badge and 'hover for more'),
    on P2 'Revisit the facts' with the hover words F1 to F4 (the finding tooltips), and the hover word Definitions (the
    glossary page). The words and the dots are out of the tab order; the hover words carry the findings' and the glossary's
    alt text, so a keyboard user hears what a hover would show."""
    dot = lambda name, j: decorative(tb(page, name, "·", font=DISPLAY, colour=ZONE_MUTED, align="center"), 680 + j)  # noqa: E731
    out = [decorative(image_measure(page, f"z_hint{sfx}", "Info Hint SVG", None), 690 + i)]
    if page == P2:
        out += [dot("z_dot2a", 1), decorative(tb(page, "z_facts", "Revisit the facts", colour=ZONE_MUTED, align="right"), 685)]
        out += [hover_word(page, f"hdr_f{k}", f"Finding Chip F{k} (text)", f"tt-f{k}", f"Alt F{k} Title (text)") for k, _ in FINDINGS]
    out += [dot(f"z_dot{sfx}" + ("b" if sfx else ""), 2 + i), hover_word(page, f"hdr_def{sfx}", "Definitions Chip (text)", TT_GLOSS, "Alt Definitions (text)", align="right")]
    return out


def brand_row(page_name, sfx):
    """The 3.1 lockup on the night zone and the eyebrow beside it (plan 11): first in the reading order, so a screen
    reader starts with whose report this is and which page."""
    pg = PAGES[page_name]
    L = pg["logo"]
    out = [image_file("z_logo", L["x"], L["y"], L["w"], L["h"], 1003, L["tab"], LOCKUP, "Goodnight Inn"),
           # ZONE_EYEBROW on Night 9.5:1; at the 12 pt floor instead of the kit's 11 pt eyebrow
           tb(page_name, f"z_eyebrow{sfx}", "  ·  ".join(EYEBROW[page_name]),
              runs=[(EYEBROW[page_name][0], DISPLAY, SPX, ZONE_EYEBROW, False), ("  ·  " + EYEBROW[page_name][1], DISPLAY, SPX, ZONE_MUTED, False)],
              alt=("Page 1 of 2, the wake-up call: the brand review" if sfx == "" else "Page 2 of 2, room to invest: the investment strategy"))]
    return out


def scatter_axes(objs):
    """The scatter's axis ends from measures, shared by all layers so their plot areas match exactly."""
    objs["categoryAxis"][0]["properties"]["start"] = mtext("Scatter X Start")
    objs["categoryAxis"][0]["properties"]["end"] = mtext("Scatter X End")
    objs["valueAxis"][0]["properties"]["start"] = mtext("Scatter Y Start")
    objs["valueAxis"][0]["properties"]["end"] = mtext("Scatter Y End")
    return objs


NAMED_BUBBLE = {"full": -40, "small": -22}  # size multiplier of the A/B/C layer per stack; the dot sizes come from the Named Point Size measures.
# Round 5, measured in Desktop: the full stack centres the letters inside its 22 px dots; the small stack puts them UNDER the dots whatever
# their size (16, 23, 29 px) and caps the dots at 10 px when the multiplier drops to -40. So the small layer labels its dots with a tag:
# the letter in white on a Night box under the dot (categoryLabels background).


def scatter_stack(slot, deco_base, build_layer=False):
    """The package scatter as layers on one plot area (same axis measures, preventOverflow off on all, so the plot
    areas match). 1 the cloud: every package but A, B and C, Warm Grey. 2 A, B and C on top with their letters: Power
    BI draws larger markers first, so a cloud in the same visual painted over B and C (REVIEW M2). 3 a hover layer on
    top: all 456 packages, fully transparent markers, wired to the tooltip page, so every dot shows its own card
    (08-verbeterplan V2). Round 4: the same stack twice, full size (hero_packages, rec state) and small
    (hero_s_packages, alts and build), because a bookmark cannot resize a visual; the small one carries a fourth
    layer, the plan being built, as one Tangerine dot (build state)."""
    v = []
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
            # The verdict line, quieter (08-verbeterplan V3): 1 px in Warm Grey. The band above it, where a package pays
            # back by 2032, is shaded in Coffee Blue at 90 % transparency and says so at its right end.
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(SLATE), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("back"), "displayName": text("Pays back by 2032"),
                                                    "dataLabelShow": b(True), "dataLabelText": text("Name"), "dataLabelColor": color(INK2),
                                                    "dataLabelHorizontalPosition": enum("right"), "dataLabelVerticalPosition": enum("above"),
                                                    "shadeShow": b(True), "shadeRegion": enum("after"), "shadeColor": color(ACCENT_MARK), "shadeTransparency": num(90)},
                                     "selector": {"id": "1"}}]}
    scatter_axes(objs)
    x, y, w, h, z, tab = at(P2, slot)
    q_cloud = {k: val for k, val in q.items() if k != "Size"}
    o_cloud = copy.deepcopy(objs)
    o_cloud["bubbles"][0]["properties"]["bubbleSize"] = integer(0)
    # The cloud is a tab stop after the A/B/C layer (pass-3 review: the package card is hover-only). Its header gives
    # 'Show as table', and the card's facts ride in its Tooltips well, so a keyboard user reads every package's
    # payback, range and initiatives there. The hover layer stays out of the tab order (mouse only).
    q_cloud_kb = {**q_cloud, "Tooltips": {"projections": [proj_mea("TT Payback (text)", "Payback"), proj_mea("TT Range (text)", "NPV in Low, Expected, High"),
                                                          proj_mea("TT Moves (text)", "Moves and their NPV"), proj_mea("TT Not Included (text)", "Not in it")]}}
    v.append(bind_alt(visual(slot, "scatterChart", x, y, w, h, z, tab + 1, query=q_cloud_kb, objects=o_cloud, filters=[filter_in("Package", "Preset", [""], "flt_cloud")],
                             vcos=vco(padding=0)), "Alt Scatter Cloud (text)"))
    quiet = lambda o: (o["valueAxis"][0]["properties"].__setitem__("gridlineShow", b(False)), o.pop("y1AxisReferenceLine", None), o)[-1]  # noqa: E731
    # Round 5: the three named dots get their own, near-equal size (Named Point Size) and a multiplier per stack, so
    # each dot is wide enough for Power BI to centre the letter inside it (at the cloud's sizes B and C were too small
    # and their letters fell beside the dots; render 10 Nov, Björn's second look).
    q2 = {**q, "Category": {"projections": [proj_col("Package", "Preset", display="Package")]},
          "Size": {"projections": [proj_mea("Named Point Size (small)" if build_layer else "Named Point Size", "Marker size")]}}
    o2 = quiet(copy.deepcopy(objs))
    o2["categoryLabels"] = [{"properties": {"show": b(True), "fontFamily": text(DISPLAY), "fontSize": num(S), "color": color(SURFACE), "bold": b(True)}}]
    o2["dataPoint"] = [{"properties": {"fill": fv("Named Point Color")}, "selector": WILD}]
    o2["bubbles"][0]["properties"]["bubbleSize"] = integer(NAMED_BUBBLE["small" if build_layer else "full"])
    if build_layer:  # the tag under the dot (see NAMED_BUBBLE)
        # Night for all three (a measure-driven box colour was not applied per point, render 10 Nov); white letter 15.8:1
        o2["categoryLabels"][0]["properties"].update({"enableBackground": b(True), "backgroundColor": color(INK), "backgroundTransparency": num(0)})
    v.append(bind_alt(visual(f"{slot}_named", "scatterChart", x, y, w, h, z + 2, tab, query=q2, objects=o2, filters=[filter_in("Package", "Preset", ["A", "B", "C"], "flt_named")],
                             vcos=vco(padding=0)), "Alt Scatter (text)"))
    if build_layer:
        # the plan being built: one dot from the one-row BuildPoint table at (Build Capex, Build NPV), Tangerine, no
        # letter (white on Tangerine fails 4.5:1); the comparer's legend names it. Blank size = no dot while empty.
        q4 = {"Category": {"projections": [proj_col("BuildPoint", "Label", display="Your plan")]},
              "X": {"projections": [proj_mea("Build Capex", "Capex")]}, "Y": {"projections": [proj_mea("Build NPV (sel)", "NPV through 2032")]},
              "Size": {"projections": [proj_mea("Build Point Size", "Marker size")]}}
        o4 = quiet(copy.deepcopy(objs))
        o4["dataPoint"] = [{"properties": {"fill": color(SIGNAL_MARK)}, "selector": WILD}]
        o4["bubbles"][0]["properties"]["bubbleSize"] = integer(-20)
        v.append(decorative(visual(f"{slot}_build", "scatterChart", x, y, w, h, z + 3, 0, query=q4, objects=o4, vcos=vco(padding=0)), deco_base + 1))
    o3 = quiet(copy.deepcopy(o_cloud))
    o3["markers"] = [{"properties": {"transparency": num(100), "borderShow": b(False)}}]
    hv = vco(padding=0)
    hv["visualTooltip"] = [{"properties": {"show": b(True), "type": enum("Canvas"), "section": text(TT)}}]
    v.append(decorative(visual(f"{slot}_hover", "scatterChart", x, y, w, h, z + 4, 0, query=q_cloud, objects=o3, vcos=hv), deco_base))
    return v


def waterfall(name, table, column, y_measure, flag_measure, y_start, y_end, alt_measure, title_measure=None, muted=False):
    """Where the NPV comes from: one bar per initiative, the total last. No value axis: every bar carries its own
    signed label (plan 11); the ends come from the model so the labels always have room. Plan 10 D6: an increase in
    Coffee Blue, a decrease in Tangerine (a signal), the total in Night."""
    q = {"Category": {"projections": [proj_col(table, column)]}, "Y": {"projections": [proj_mea(y_measure, "NPV through 2032")]}}
    # verification 17 follow-up (12 Nov): with 8 to 10 bars Desktop rotates the labels and clips them at about 75 px;
    # categoryAxis.maxMarginFactor (reportThemeSchema 2.143) made it worse at 40 (measured), so the axis stays at its
    # default and the Waterfall Label column keeps every name within that width (widest: "Kingston +40")
    objs = {"categoryAxis": axis(BODY, S, INK2, gridlines=None), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, units=1),
            "sentimentColors": [{"properties": {"increaseFill": color(ACCENT_MARK), "decreaseFill": color(SIGNAL_MARK), "totalFill": color(INK), "otherFill": color(SLATE)}}],
            "labels": labels(True, BODY, S, INK, units=1, position="OutsideEnd"), "legend": legend(False)}
    objs["valueAxis"][0]["properties"]["start"] = mtext(y_start)
    objs["valueAxis"][0]["properties"]["end"] = mtext(y_end)
    # round 9: a filter cannot blank the build waterfall before a move is picked: Power BI draws the total bar ($0) whatever
    # the row filter says (render 11 Nov), so the empty state keeps its one bar and the card's title carries the state
    return chart(P2, name, "waterfallChart", q, objs, None, title_measure=title_measure, muted=muted,
                 filters=[filter_measure_gt(flag_measure, 0, f"flt_{name}")], alt_measure=alt_measure)


HORIZON = lambda: filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon")  # noqa: E731


def cumulative_chart(name, series, colours, widths, dashed, title_measure, alt_measure, dotted=()):
    """Cumulative net impact by year: a legend that draws each line (lineOnly), a labelled break-even line, the year
    axis shown (round 4: the chart is tall enough). series: [(measure, display)]."""
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m, d) for m, d in series]}}
    lg = legend(True, BODY, S, INK2, "Top")
    lg[0]["properties"]["legendMarkerRendering"] = enum("lineOnly")
    ms = [mref(m) for m, _ in series]
    objs = {"categoryAxis": axis(BODY, S, INK2, extra={"labelPrecision": integer(0)}), "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, units=1), "legend": lg,
            "dataPoint": series_colors(dict(zip(ms, colours))),
            "lineStyles": line_styles(dict(zip(ms, widths)), dashed=tuple(mref(m) for m in dashed)),
            "seriesLabels": [{"properties": {"show": b(False)}}],
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(SLATE), "transparency": num(0), "width": num(1), "style": enum("solid"), "position": enum("back"),
                                                    "displayName": text("Break-even"), "dataLabelShow": b(True), "dataLabelText": text("Name"), "dataLabelColor": color(INK2),
                                                    "dataLabelHorizontalPosition": enum("left"), "dataLabelVerticalPosition": enum("above")}, "selector": {"id": "1"}}]}
    for m in dotted:
        next(e for e in objs["lineStyles"] if e.get("selector", {}).get("metadata") == mref(m))["properties"]["lineStyle"] = enum("dotted")
    return chart(P2, name, "lineChart", q, objs, None, title_measure=title_measure, filters=[HORIZON()], alt_measure=alt_measure, tooltip_page=TT_YEAR)


def nums_card(name, measures, labels_, alt_measure, size=21):
    v = card(name, *at(P2, name), measures, DISPLAY, size, INK, BODY, S, INK2, labels=labels_)
    return bind_alt(v, alt_measure)


SELECTOR_FIELDS = [proj_col("BuildMove", "ProjectID"), proj_col("BuildMove", "Short Name", display="Move"), proj_col("BuildMove", "Sort"),
                   proj_mea("Move Answers (text)", "Answers"), proj_mea("Move Capex (text)", "Capex"), proj_mea("Move NPV (text)", "NPV"),
                   proj_mea("Move NPV (num)", "NPVnum"), proj_mea("Move Case (text)", "Case"),
                   proj_mea("Move Capex (num)", "CapexNum"), proj_mea("Move Budget (num)", "Budget")]  # the footer's running total (round 5)
SELECTOR_ALT = "Build your own plan: the ten Goodnight Inn moves with what each costs and returns. Tap a move to add it to the plan or take it out"


def deneb_selector():
    """VERIFY (Desktop spike, 12-feedbackronde-4 step 4): the move selector as a Deneb visual in advanced cross-filter
    mode. Shape after the deneb.guide PBIR guide: the spec as a single-quoted text literal in objects.vega.jsonSpec,
    provider 'vega', enableSelection true, selectionMode 'advanced'; the data role is 'dataset'. The GUID also goes
    into report.json publicCustomVisuals (main). Deneb by Daniel Marsh-Patrick, AppSource-certified (CREDITS.md)."""
    spec = json.loads(DENEB_SPEC.read_text(encoding="utf-8"))
    props = {"jsonSpec": text(json.dumps(spec, separators=(",", ":"), ensure_ascii=False)), "jsonConfig": text("{}"),
             "provider": text("vega"), "renderMode": text("svg"), "enableSelection": b(True), "selectionMode": text("advanced"),
             "selectionMaxDataPoints": num(50), "enableTooltips": b(False), "enableContextMenu": b(False), "enableHighlight": b(False)}
    objs = {"vega": [{"properties": props}]}
    x, y, w, h, z, tab = at(P2, "dn_build_selector")
    return visual("dn_build_selector", DENEB_GUID, x, y, w, h, z, tab, query={"dataset": {"projections": SELECTOR_FIELDS}}, objects=objs,
                  vcos=vco(alt=SELECTOR_ALT, padding=0))


def native_selector():
    """The fallback: a native button slicer in list layout (ten rows, multi-select without Ctrl) on BuildMove."""
    v = button_slicer("dn_build_selector", "BuildMove", "Short Name", None, SELECTOR_ALT, 1, rows=10, multi=True)
    v["visual"]["objects"]["selection"][0]["properties"]["selectAllCheckboxEnabled"] = b(False)
    return v


def p2_visuals():
    v = [dyn(P2, "z_headline2", "Headline P2 (text)", size=28, colour=ZONE_TEXT, font=DISPLAY)]
    v += header_line(P2, "2", 2)  # the hint, 'Revisit the facts' F1 to F4 and Definitions in the masthead's slot (12 Nov evening)
    v.append(dyn(P2, "c_subtitle2", "Subtitle P2 (text)", size=S, colour=ZONE_MUTED))

    # ---- the scatter card, rec state: title, zoom toggle, the reading guide (round 4: 'what am I looking at' before
    # the dots, on an Ice tile), the full-size stack
    v.append(title(P2, "c_scatter_title", "Scatter Title (text)"))
    v.append(button_slicer("sl_view", "ScatterView", "View", "All packages", "Scatter view: all packages, or a zoom on the region where A, B and C sit", 2, size=S))
    v.append(decorative(tb(P2, "c_guide_kicker", "HOW TO READ THIS CHART", font=DISPLAY, size=SPX, colour=ACCENT), 11))
    v.append(decorative(tb(P2, "c_guide_legend", "", align="right",
                           runs=[("● ", DISPLAY, SPX, ACCENT, False), ("A, our recommendation      ", BODY, SPX, INK2, False),
                                 ("● ", DISPLAY, SPX, INK, False), ("B and C, considered      ", BODY, SPX, INK2, False),
                                 ("○ ", DISPLAY, SPX, INK2, False), ("every other package", BODY, SPX, INK2, False)]), 12))
    v.append(dyn(P2, "c_guide", "Guide (text)", colour=INK, alt_measure="Alt Guide (text)"))
    v += scatter_stack("hero_packages", 2)
    # ---- the small scatter card, alts and build
    v.append(title(P2, "c_scatter_title_s", "Scatter Title Short (text)"))
    v += scatter_stack("hero_s_packages", 6, build_layer=True)

    # ---- the panel's top row: state titles (left, alts and build), the tab bar, the scenario toggle
    v.append(tb(P2, "c_alts_title", "Considered, not recommended", font=DISPLAY, size=19, colour=INK))
    v.append(tb(P2, "c_alts_intro", "Both weighed against A; the chart below compares all three."))
    v.append(tb(P2, "c_build_title", "Build your own plan", font=DISPLAY, size=19, colour=INK))
    v.append(tb(P2, "c_build_intro", "Tap a move to add or remove it; the numbers, the waterfall and the chart below follow."))
    v += tab_bar()
    # the label above the scenario toggle is in the slicer's alt text, so it leaves the tab order (plan 11)
    v.append(decorative(tb(P2, "lbl_scenario", "Scenario", size=SPX, colour=INK2), 3))
    v.append(button_slicer("sl_scenario", "Scenario", "Scenario", "Expected", "Scenario: Low, Expected or High; every number on this page follows it", 3))

    # ---- rec: the recommendation tile (one supporting sentence), where the NPV comes from, the cumulative chart
    v.append(decorative(image_measure(P2, "img_rec_chip", "Chip Funded", None), 5))
    v.append(tb(P2, "c_rec_title", "Our recommendation: package A", font=DISPLAY, size=20, colour=INK))
    v.append(dyn(P2, "c_rec_mix", "Rec Mix (text)", size=S, colour=INK))
    v.append(nums_card("c_rec_nums", ["Rec Capex (text)", "Rec NPV (text)", "Rec Range (text)", "Rec Run-rate (text)"],
                       ["capex", "NPV through 2032", "NPV range, $M", "profit a year by 2032"], "Alt Rec Nums (text)"))
    v.append(dyn(P2, "c_rec_note", "Rec Note (text)", colour=INK))
    v.append(waterfall("ch_rec_waterfall", "InvestmentProjects", "Short Name", "Focus Project NPV (shown)", "Focus Project Flag", "Waterfall Y Start", "Waterfall Y End",
                       "Alt Waterfall (text)", title_measure="Waterfall Title (text)"))
    # Low dashed Tangerine (a signal), Expected dotted, High solid, the case in view thick in Coffee Blue (plan 10 D6);
    # the three context lines step aside for the case in view (Cumulative Line (…) blank when it is the case in view)
    ms = ["Cumulative Line (Low)", "Cumulative Line (Expected)", "Cumulative Line (High)", "Focus Cumulative Net (sel)"]
    v.append(cumulative_chart("ch_rec_cumulative", list(zip(ms, ["Low", "Expected", "High", "Case in view"])), [SIGNAL_MARK, SLATE, SLATE, ACCENT_MARK], [1.5, 1.5, 1.5, 3],
                              dashed=(ms[0],), dotted=(ms[1],), title_measure="Cumulative Title (text)", alt_measure="Alt Cumulative (text)"))
    # the standing uncertainty line (decision 06), in Burnt Tangerine: it is the page's caution
    v.append(dyn(P2, "c_uncertainty", "Uncertainty (text)", colour=BAD))

    # ---- alts: B and C side by side (why considered, why not picked, where their NPV comes from), the comparer
    for k, chip_deco in (("B", 7), ("C", 8)):
        lk = k.lower()
        v.append(decorative(image_measure(P2, f"img_{lk}_chip", "Chip Plain", None), chip_deco))
        v.append(dyn(P2, f"c_{lk}_title", f"Pkg Label {k} (text)", size=TITLE_PT, colour=INK, font=DISPLAY))
        v.append(nums_card(f"c_{lk}_nums", [f"Preset {k} Capex (text)", f"Preset {k} NPV (text)", f"Preset {k} Range (text)"], ["capex", "NPV through 2032", "NPV range, $M"],
                           f"Alt {k} Nums (text)", size=18))
        v.append(dyn(P2, f"c_{lk}_why", f"Alt {k} Why (text)", colour=INK))
        v.append(dyn(P2, f"c_{lk}_whynot", f"Alt {k} WhyNot (text)", colour=INK))
        # no mini waterfall (render 10 Nov: 112 px was too little for the labels; the tooltip on the dot carries the parts)
        v.append(dyn(P2, f"c_{lk}_payback", f"Preset {k} Payback (text)"))
    # A always Coffee Blue (Björn 10 Nov), B Night, C Tangerine and dashed (the signal: it never breaks even)
    v.append(cumulative_chart("ch_cmp_alts", [("Preset A Cumulative Net (sel)", "A, our recommendation"), ("Preset B Cumulative Net (sel)", "B"), ("Preset C Cumulative Net (sel)", "C")],
                              [ACCENT_MARK, INK, SIGNAL_MARK], [3, 2, 2], dashed=("Preset C Cumulative Net (sel)",), title_measure="Cmp Alts Title (text)", alt_measure="Alt Cmp Alts (text)"))

    # ---- build: the move selector, your plan (title, numbers, the rules, where its NPV comes from), the comparer
    v.append(deneb_selector() if SELECTOR == "deneb" else native_selector())
    # the title row doubles as the budget alarm (round 5, Björn): over the budget it turns into a Tangerine band with
    # white 18 pt text (WCAG large text, 4.2:1), and the sentence names the overshoot
    v.append(dyn(P2, "c_you_title", "Build Title (text)", size=18, colour=INK, font=DISPLAY, colour_measure="Build Title Ink", fill_measure="Build Title Fill"))
    # 16 pt, not 18: three columns in 464 px, and an over-budget plan prints two two-digit negatives in the range (render 10 Nov)
    v.append(nums_card("c_you_nums", ["Build Capex (text)", "Build NPV (text)", "Build Range (text)"], ["capex", "NPV through 2032", "NPV range, $M"], "Alt You Nums (text)", size=16))
    v.append(dyn(P2, "c_you_rules", "Build Valid (text)", colour_measure="Build Valid Color"))
    # FinalV2 (plan 15 S2): the $0 rest bar of the empty state reads as a waiting place, not a fault: a muted note as the tile's title
    # verification 17 (12 Nov): the bars carry BuildMove[Waterfall Label], 12 characters at most, so none ends in an ellipsis
    v.append(waterfall("ch_build_waterfall", "BuildMove", "Waterfall Label", "Build Project NPV (shown)", "Build Row Flag", "Build WF Y Start", "Build WF Y End", "Alt Build Waterfall (text)",
                       title_measure="Build WF Note (text)", muted=True))
    v.append(cumulative_chart("ch_cmp_build", [("Preset A Cumulative Net (sel)", "A, our recommendation"), ("Build Cumulative Net (sel)", "Your plan")],
                              [ACCENT_MARK, SIGNAL_MARK], [3, 3], dashed=(), title_measure="Cmp Build Title (text)", alt_measure="Alt Cmp Build (text)"))
    v.append(dyn(P2, "z_footer2", "Footer P2 (text)"))
    # 12 Nov evening: the hover signifier on every hover target (the scatter's dots, the three year charts), the footer row's extras
    v += [badge(P2, "bdg_scatter", 20), badge(P2, "bdg_scatter_s", 21), badge(P2, "bdg_rec_cum", 22), badge(P2, "bdg_cmp_alts", 23), badge(P2, "bdg_cmp_build", 24)]
    return v


# ====================================================================== the package tooltip (08-verbeterplan V2, round 4)
TT = "tt-package"


def tt_visuals():
    """The package tooltip, round 7 (Björn, 11 Nov: leaner, in the page's own skin). On the night banner the kicker
    (PACKAGE A · EXPECTED CASE) and the title; a white card with the NPV, the capex, the verdict over the three cases
    and the range bar on the shared axis; a second card with the moves and their capex and NPV, adding up to the
    package. The round-6 waterfall bars, Answers column, histogram strip and move grid left: too much for a hover.
    Grain: one Package[PackageID] from the hover layer. Every SVG has a text twin (TT Range (text), TT Moves (text))."""
    def c(name, measure, size, colour, font=BODY, bold=False, label=None, align="left"):
        x, y, w, h, z, tab = at(TT, name)
        vv = card(name, x, y, w, h, z, tab, [measure], font, size, colour, BODY, S, INK2, labels=[label] if label else None, align=align)
        if bold:
            vv["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
        return bind_alt(vv, measure)
    v = [decorative(dyn(TT, "tt_kicker", "TT Kicker (text)", size=S, colour=TT_KICKER, font=DISPLAY), 5),
         c("tt_title", "TT Title (text)", TITLE_PT, TT_TITLE, DISPLAY),
         c("tt_npv", "TT NPV (text)", 20, INK, DISPLAY, True, label="NPV through 2032"),
         c("tt_capex", "TT Capex (text)", 18, INK, DISPLAY, False, label="capex"),
         c("tt_payback", "TT Payback (text)", S, INK, bold=True),  # the verdict over the three cases
         decorative(image_measure(TT, "tt_range_svg", "TT Range SVG", None), 3),  # the range bar on the shared axis, numbers inside
         c("tt_moves_label", "TT Moves Label (text)", S, INK, DISPLAY),
         decorative(image_measure(TT, "tt_moves_svg", "TT Moves SVG", None), 2)]  # the moves list as one SVG (round 6)
    v[2]["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("TT NPV Color")
    v[4]["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("TT Payback Color")
    return v


# ====================================================================== pages, bookmarks, resources
# Night-glow depth (plan 10 D7 with Bjorn's waiver, plan 11): one soft shadow for every card, a heavier one under each
# page's hero card, and a Coffee Blue glow under the recommendation. Values from the comps (comps_v3.GLOW).
SHADOW = {"card": (INK, 14, 36, 84), "hero": (INK, 24, 56, 72), "glow": (ACCENT_MARK, 14, 34, 70)}
HERO_CARDS = {"kpi", "scatter", "scatter_s"}
# tiles (round 4): glow = the recommendation (Coffee Blue glow and border); tint = the reading guide (Ice fill, no
# shadow); outline = the B, C and your-plan cards inside the wide panel (white, Seam hairline, no shadow)
TILE_KIND = {"glow": (SURFACE, ACCENT_MARK, "glow"), "tint": (TINT, TINT, None), "outline": (SURFACE, HAIR, None)}


def frame(name, x, y, w, h, z, i, shadow, border=SURFACE, fill=SURFACE, radius=12):
    """An empty textbox as card furniture: a fill, radius 12, one outer shadow (visualContainer dropShadow: preset
    Custom, position Outer, angle 90 = straight down) or none, out of the tab order. A border in the fill colour
    shows the radius without a hairline (plan 10 D4)."""
    v = textbox(name, x, y, w, h, z, 0, [[("", BODY, SPX, INK2, False)]])
    vc = v["visual"]["visualContainerObjects"]
    vc["background"] = [{"properties": {"show": b(True), "color": color(fill), "transparency": num(0)}}]
    vc["border"] = [{"properties": {"show": b(True), "color": color(border), "radius": num(radius), "width": num(1)}}]
    if shadow:
        col_, dist, blur, transp = SHADOW[shadow]
        vc["dropShadow"] = [{"properties": {"show": b(True), "preset": enum("Custom"), "position": enum("Outer"), "color": color(col_),
                                            "transparency": num(transp), "shadowSpread": num(0), "shadowBlur": num(blur), "angle": num(90),
                                            "shadowDistance": num(dist)}}]
    return decorative(v, 500 + i)


def card_frames(page_name):
    """The layout's cards as visuals UNDER the content (z 100+), then the tiles (z 150+). The scene behind them is the
    page background image ('Fit', round 7); the cards stay visuals so they scale with the content in every host."""
    pg = PAGES[page_name]
    out = [frame(f"z_card_{c['id']}", c["x"], c["y"], c["w"], c["h"], 100 + i, i, c["shadow"] if "shadow" in c else ("hero" if c["id"] in HERO_CARDS else "card"))
           for i, c in enumerate(pg["cards"])]
    for j, t in enumerate(pg.get("tiles", [])):
        fill, border, shadow = TILE_KIND[t.get("kind", "glow")]
        out.append(frame(f"z_tile_{t['id']}", t["x"], t["y"], t["w"], t["h"], 150 + j, 50 + j, shadow, border=border, fill=fill, radius=t.get("radius", 12)))
    return out


CANVAS_FILE = "canvas-night.jpg"
# Round 10 (Björn, 11 Nov): tooltips at 440 px (Microsoft Learn: keep page tooltips small, 320 x 240 is the built-in size),
# the orange band carries the kicker only and the title sits in the card in Night; scaled with the canvas (useScaledTooltips).
# Round 7 (Björn, 11 Nov): a tooltip is the page in miniature, with elements made for its size: its own night scene
# (brand_canvas_v3.tooltip, the horizon 24 px under the first card), the kicker and the title on the banner, white cards
# with the page's shadow below.
TT_PAGES = [p["name"] for p in LAYOUT["pages"] if p.get("tooltip")]


def TT_CANVAS(name):
    return f"canvas-tt-{name}.jpg"


# Where the scene lives (rounds 6 to 9). A page background image with Fit is fitted into the host's display area; Desktop's
# is taller than the page, so there the scene drifts up (14 px at 100 %, 38 px at 60 % zoom, more at 45 %; the Service's
# area is the page itself). Round 9b (Björn, 11 Nov, at his zoom: "no overlay of the top visuals on the banner and the text
# is too low"): the scene is the LOWEST VISUAL on every page (z 0, out of the tab order), placed in page pixels, so the cards
# hang into the banner exactly in every host; the page background keeps the same scene with Fit only for the strip Desktop
# paints above a page. The two coincide on the page (both scale with it), so nothing shows twice.
SCENE_VISUAL = False  # round 10 (Björn, 11 Nov): the overlay is gone everywhere; the page background (Fit) carries the scene


def scene_visual(name):
    """The page's scene as a decorative image visual under everything (z 0): the night-glow canvas on a report page, the
    page's own orange scene on a tooltip page."""
    if not SCENE_VISUAL:
        return []
    cv = PAGES[name].get("canvas", LAYOUT["canvas"])
    f = TT_CANVAS(name) if PAGES[name].get("tooltip") else CANVAS_FILE
    return [decorative(image_file("z_canvas", 0, 0, cv["w"], cv["h"], 0, 0, f, None), 0)]


DATA_VISUALS = {"lineChart", "clusteredColumnChart", "clusteredBarChart", "scatterChart", "tableEx", "waterfallChart"}  # round 9: + bars (the F4 chip tooltip)


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
        # (4) round 9 (Björn, 11 Nov): Power BI's own tooltip is off brand, so it is off wherever no report-page tooltip is
        # bound. The one exception is the keyboard cloud layer (hero_packages, hero_s_packages): its Tooltips well is the
        # package card's text twin for keyboard users, and keyboard focus is the only way it opens.
        vcos = v["visual"].setdefault("visualContainerObjects", {})
        if "visualTooltip" not in vcos and v["name"] not in KEYBOARD_LAYERS:
            vcos["visualTooltip"] = [{"properties": {"show": b(False)}}]
    return visuals


KEYBOARD_LAYERS = {"hero_packages", "hero_s_packages"}


def no_card_fill(visuals):
    """cardVisual draws a white fill of its own (fillCustom, id 'default'); it showed as white boxes on the canvas in
    Desktop (7 Nov). Off everywhere: the cards' surfaces come from the card frames. Both layers closed, each with
    show=false AND 100 % transparency."""
    for v in visuals:
        if v["visual"]["visualType"] == "cardVisual":
            v["visual"]["objects"]["fillCustom"] = [{"properties": {"show": b(False), "transparency": num(100)}, "selector": {"id": "default"}}]
            if "color" not in v["visual"]["visualContainerObjects"].get("background", [{}])[0].get("properties", {}):  # not the alarm band (dyn fill_measure)
                v["visual"]["visualContainerObjects"]["background"] = [{"properties": {"show": b(False), "transparency": num(100)}}]
    return visuals


def page(name, display, visuals, filters=None, tooltip=False, interactions=None):
    # colour only: furniture (cards, logo) is drawn by visuals so it scales with the content on any viewport
    cv = PAGES[name].get("canvas", LAYOUT["canvas"])
    p = {"$schema": PAGE_SCHEMA, "name": name, "displayName": display, "displayOption": "FitToPage", "height": cv["h"], "width": cv["w"],
         # Night colour and wallpaper everywhere, so no host shows Oat around a page (round 6, Björn, 11 Nov).
         "objects": {"background": [{"properties": {"color": color(INK), "transparency": num(0)}}],
                     "outspace": [{"properties": {"color": color(INK), "transparency": num(0)}}]}}
    # The scene as the page background, scaled to the page ('Fit'): the night-glow canvas on the report pages, each
    # tooltip page's own scene on it. Pixel-exact only where the host's display area is the page (the Service); in
    # Desktop the lowest visual carries it exactly (SCENE_VISUAL, round 8) and the background fills the strip above.
    bg = TT_CANVAS(name) if tooltip else CANVAS_FILE
    p["objects"]["background"][0]["properties"]["image"] = {"image": {"name": text(bg), "scaling": text("Fit"),
        "url": {"expr": {"ResourcePackageItem": {"PackageName": "RegisteredResources", "PackageType": 1, "ItemName": bg}}}}}
    if tooltip:
        # a report-page tooltip: hidden in view mode, bound as a tooltip (page schema 2.1.0: type + pageBinding)
        p.update({"displayOption": "ActualSize", "type": "Tooltip", "visibility": "HiddenInViewMode",
                  "pageBinding": {"name": tag("binding." + name)[:20].replace("-", ""), "type": "Tooltip", "parameters": []}})
    if interactions:
        p["visualInteractions"] = interactions
    if filters:
        p["filterConfig"] = {"filters": filters}
    for vis in visuals:
        sts = states_of(name, vis["name"])
        if sts and OPEN_STATE not in sts:
            vis["isHidden"] = True
    return p, visuals


BOOKMARK_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/2.1.0/schema.json"
BOOKMARKS_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmarksMetadata/1.0.0/schema.json"


def bookmark(name, display, show_state, visuals):
    """Display-only (applyOnlyToTargetVisuals, suppressData): it shows the visuals of one state and hides the others,
    and never touches the slicers. display.mode accepts only 'hidden'; a shown visual carries no display block."""
    targets = [v for v in visuals if states_of(P2, v["name"])]
    containers = {}
    for v in targets:
        sv = {"visualType": v["visual"]["visualType"]}
        if show_state not in states_of(P2, v["name"]):
            sv["display"] = {"mode": "hidden"}
        containers[v["name"]] = {"singleVisual": sv}
    return {"$schema": BOOKMARK_SCHEMA, "displayName": display, "name": name,
            "options": {"applyOnlyToTargetVisuals": True, "targetVisualNames": [v["name"] for v in targets], "suppressActiveSection": True, "suppressData": True},
            "explorationState": {"version": "1.3", "activeSection": P2, "sections": {P2: {"visualContainers": containers}}}}


# the visuals the move selector may filter: everything of the plan being built; nothing else listens to it
BUILD_TARGETS = {"c_you_title", "c_you_nums", "c_you_rules", "ch_build_waterfall", "ch_cmp_build", "hero_s_packages_build"}


def interactions(v2):
    out = []
    # the hover layers only show tooltips, the build dot only marks: a click on them must not filter or dim anything
    for src in ("hero_packages_hover", "hero_s_packages_hover", "hero_s_packages_build"):
        out += [{"source": src, "target": o["name"], "type": "NoFilter"} for o in v2 if o["name"] != src]
    # the move selector filters the plan being built (DataFilter, never a highlight) and nothing else
    out += [{"source": "dn_build_selector", "target": o["name"], "type": "DataFilter" if o["name"] in BUILD_TARGETS else "NoFilter"}
            for o in v2 if o["name"] != "dn_build_selector"]
    return out


def main():
    v1 = finish(layered(P1, no_card_fill(scene_visual(P1) + card_frames(P1) + brand_row(P1, "") + p1_visuals())))
    v2 = finish(layered(P2, no_card_fill(scene_visual(P2) + card_frames(P2) + brand_row(P2, "2") + p2_visuals())))
    vt = finish(no_card_fill(scene_visual(TT) + card_frames(TT) + tt_visuals()))
    pages = [page(P1, "The Brand Review", v1),
             page(P2, "The Investment Strategy", v2,
                  filters=[filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_page_projects"), filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_page_brand")],
                  interactions=interactions(v2)),
             page(TT, TT, vt, tooltip=True)] + extra_tooltip_pages()
    rep = write_report(OUT, NAME, "Goodnight Inn · opzet", pages, THEME, THEME_FILE)
    res = rep / "StaticResources" / "RegisteredResources"
    # embedded, never a link (Publish to Web): the kit's reversed lockup and the one night-glow canvas both pages share
    shutil.copyfile(KIT / LOCKUP, res / LOCKUP)
    shutil.copyfile(BG / CANVAS_FILE, res / CANVAS_FILE)
    files = [LOCKUP, CANVAS_FILE]
    for pg in TT_PAGES:  # round 7: every tooltip page's own scene
        shutil.copyfile(BG / TT_CANVAS(pg), res / TT_CANVAS(pg))
        files.append(TT_CANVAS(pg))
    rj = rep / "definition" / "report.json"
    report = json.loads(rj.read_text(encoding="utf-8"))
    # round 9: Björn's Desktop setting (default tooltips off brand); round 10: useScaledTooltips, the report schema's
    # "the tooltip will scale to match canvas zoom" (Microsoft Learn: tooltip autoscale), so a 440 px tooltip page stays in
    # proportion to the page in the Service, Publish to Web and Desktop at any zoom
    report["settings"] = {"useEnhancedTooltips": False, "useScaledTooltips": True}
    for pk in report["resourcePackages"]:
        if pk["name"] == "RegisteredResources":
            pk["items"] += [{"name": f, "path": f, "type": "Image"} for f in files]
    if SELECTOR == "deneb":
        report["publicCustomVisuals"] = [DENEB_GUID]
    write_json(rj, report)
    bm = rep / "definition" / "bookmarks"
    for st, display in (("rec", "P2 Recommended"), ("alts", "P2 Considered"), ("build", "P2 Build your own")):
        write_json(bm / f"bm_p2_{st}.bookmark.json", bookmark(f"bm_p2_{st}", display, st, v2))
    write_json(bm / "bookmarks.json", {"$schema": BOOKMARKS_SCHEMA, "items": [{"name": f"bm_p2_{st}"} for st in STATES]})
    n1, n2 = len(v1), len(v2)
    core = sum(1 for v in v1 + v2 if v["visual"]["visualType"] in ("tableEx", "pivotTable", "clusteredBarChart", "clusteredColumnChart", "lineChart", "scatterChart", "waterfallChart"))
    hidden = sum(1 for v in v2 if v.get("isHidden"))
    print(f"report written: {rep}  P1 {n1} visuals, P2 {n2} visuals ({hidden} hidden in the {OPEN_STATE} state), {core} core chart/table visuals, selector {SELECTOR}")


if __name__ == "__main__":
    main()
