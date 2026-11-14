"""Writes the report set-up (opzet) as a PBIP report on the shared model. v4 of 2026-11-10: feedback round 4
(12-feedbackronde-4.md) on the D1 briefing (06-d1-briefing-opzet.md): P1 = headline, four benchmarked KPIs, findings
F1-F3 with one chart each, F4 where we are full; P2 = the package scatter and a right panel in three states.

Run from the repo root, after sketch_model.py and brand_canvas_v3.py (plan 11):
    python project/tools/opzet_report.py                   # writes project/pbip/GoodnightInn-opzet.pbip + .Report
    python project/tools/opzet_report.py --out DIR         # dry run elsewhere (validation outside project/pbip)
    python project/tools/opzet_report.py --state=alts      # a throwaway copy (…-alts) that OPENS in the alts state

Source of truth:
  positions  project/design-prototypes/opzet-layout.json (the slot map, with the state of every slot, tile and card)
  bindings   this file (one function per visual, measures from project/tools/sketch_model.py)
  decisions  project/project-state/active/06-, 08-, 11- and 12-feedbackronde-4.md
Canvas 1920x1080; brand kit goodnight-inn-wakeup 3.1, night header with the night-glow canvas (plans 10 and 11;
theme: project/deliverables/theme.json, canvas: project/tools/brand_canvas_v3.py).

Two visible pages, both named after the contest's questions. P2 has three states swapped by display-only bookmarks
(bm_p2_rec / bm_p2_alts / bm_p2_build), reached through the tab bar in the masthead. The scenario lives in the Scenario
slicer, so a bookmark never changes it (fx-focus rules 1-2). Shapes not yet exercised in Desktop are marked VERIFY.

FinalV3 (doc 23, the rebuild to the comp rebuild-comp-v10.html, one step per session): P1 is rebuilt (step 5). P2 runs
on the v10 slot map since step 6, which built the frame (p2_frame) and the decision card of Recommended
(p2_decision_card), step 7 the hero table and the capital plan (p2_hero, p2_capital_plan), step 8 What waits (p2_proof,
p2_waits), step 9 Build your own (p2_build):
  rec    Recommended: A: the hero table and the capital plan (built in step 7), the decision card (built)
  alts   What waits, and why: the small scatter, the table of what waits, the comparison with A (built in step 8)
  build  Build your own: the native move selector beside the moves table, your plan, the comparison with A (built in step 9;
         the Deneb selector and the waterfalls are gone, the report needs no custom visual)
"""
import copy
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pbir_lib import (visual, textbox, card, write_report, vco, axis, legend, labels, series_colors, line_styles,  # noqa: E402
                      table_objects, proj_col, proj_mea, mref, filter_in, sort_by_measure,
                      sort_by_column, b, num, integer, enum, text, color, write_json, tag, PAGE_SCHEMA)

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
# Build steps 5 and 6 (doc 23 rule 9): the v10 slot map is opzet-layout.json for every page; opzet-layout-v9.json is no longer read
from slot_map import load_layout  # noqa: E402
import sketch_model as sm  # noqa: E402  (build step 7: the hero table's geometry and the gate year, defined once beside the measures)
LAYOUT = load_layout()
THEME = json.loads((ROOT / "project" / "deliverables" / "theme.json").read_text(encoding="utf-8"))
THEME_FILE = "goodnight-inn-wakeup.json"
THEME["name"] = THEME_FILE  # the registered file name (pbir_lib / pbir_detect convention)
BG = ROOT / "project" / "deliverables" / "backgrounds"

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
EYEBROW_V10 = {"p1-brand-review": "1 / 2 · THE WAKE-UP CALL", "p2-investment-strategy": "2 / 2 · ROOM TO INVEST"}
LOCKUP = "gi-lockup-reversed@2x.png"
# Kit type scale (brand.yaml 3.1 scale_pt 30 / 20 / 14 / 12 / 12): textboxes in px, cards and visual objects in pt.
# Floor 12 pt (16 px at 1920) for notes, axes, tables, slicers and tooltips alike (plan 11). S = small text in pt,
# SPX the same in px.
S = 12
SPX = 16
TITLE_PT = 14  # card titles (kit scale step 3)
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


def fv(measure):
    """Field-value color: a measure that returns a hex string."""
    return {"solid": {"color": {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}}}}}


def mtext(measure):
    """Field-value text (title text, axis ends, image URLs bound to a measure; rendered 7 and 9 Nov)."""
    return {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": measure}}}


def at(page, name):
    s = SLOT[page][name]
    return s["x"], s["y"], s["w"], s["h"], s["z"], s["tab"]


# build step 8: the plan dot of the small scatter shares the stack's slot (alts and build) but is drawn in Build only;
# build step 9: so is its name "You"
STATE_ONLY = {"hero_s_packages_build": ("build",), "hero_s_packages_you": ("build",)}


def states_of(page, name):
    """The states a visual is shown in (a list), or None when it is always visible. Visuals derived from a slot
    (kpi_occ_label from kpi_occ, hero_packages_hover from hero_packages) share the slot's state; card frames
    (z_card_<id>) and tiles (z_tile_<id>) read the layout's cards and tiles."""
    pg = PAGES[page]
    if name in STATE_ONLY:
        return list(STATE_ONLY[name])
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


def kpi_cell(slot, label, value_measure, context_measure, alt_measure, colour_measure, code=None):
    """One KPI of the band: a label, the value and one comparison (DC-051), stacked inside the slot (24 + 40 + 24 px).
    One tab stop per KPI (plan 11): the value reads label, value and comparison aloud (Alt KPI ... (text)); the label
    and the context line are the same words on the canvas, so they leave the tab order. Round 4: the context line's
    colour comes from a measure (Burnt Tangerine where the news is bad, Deep Coffee where it is best of four).
    FinalV3 (R-P1-2, doc 21 4.1): the finding's code leads the label as its own run, Night semibold ("F4 · Occupancy")."""
    x, y, w, h, z, tab = at(P1, slot)
    runs = [(code, DISPLAY, SPX, INK, False), (" · " + label, BODY, SPX, INK2, False)] if code else [(label, BODY, SPX, INK2, False)]
    lab = textbox(f"{slot}_label", x, y, w, 24, z, tab, [runs])
    val = card(slot, x, y + 24, w, 48, z, tab + 1, [value_measure], DISPLAY, 28, INK)
    val["visual"]["objects"]["value"][0]["properties"]["bold"] = b(True)
    ctx = card(f"{slot}_ctx", x, y + 72, w, 24, z, tab + 2, [context_measure], BODY, S, INK2)
    ctx["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv(colour_measure)
    return [decorative(lab, 100 + tab), bind_alt(val, alt_measure), decorative(ctx, 200 + tab)]


_KICK = [0]


def kicker(page, name, txt, code_colour=BAD, sep="  ·  "):
    """The kit's eyebrow on a white card at the 12 pt floor, out of the tab order: the title after it reads the
    kicker's words first (Alt F# Title (text)). Round 4, a little more orange: the finding's code (F1) in Burnt
    Tangerine (6.2:1 on white), the words in Deep Coffee. FinalV3 (R-G3, doc 21 4.1): on the rebuilt pages the code is
    Night and the separator one space each side, as the comp ("F1 · THE MARGIN")."""
    _KICK[0] += 1
    code, _, rest = txt.partition(sep)
    runs = [(code, DISPLAY, SPX, code_colour, False), (sep + rest, DISPLAY, SPX, ACCENT, False)] if rest else [(txt, DISPLAY, SPX, ACCENT, False)]
    return decorative(tb(page, name, txt, runs=runs), 600 + _KICK[0])


def night_kicker(page, name, txt):
    """Round 7: the kicker on a tooltip's banner, the page's own eyebrow idea, out of the tab order; the title after it
    carries the words. Round 9: on the orange banner, in TT_KICKER."""
    _KICK[0] += 1
    return decorative(tb(page, name, txt, font=DISPLAY, size=SPX, colour=TT_KICKER), 600 + _KICK[0])


def title(page, name, measure, alt_measure=None, lift=0):
    """lift (FinalV3 step 5): a card centres its line in its box; the comp sets it at the top, so a 14 pt title in a 32 px
    slot sits low: 4.5 px on the stitched page render of step 5. P1 lifts its titles by 5."""
    v = dyn(page, name, measure, size=TITLE_PT, colour=INK, font=DISPLAY, alt_measure=alt_measure)
    if lift:
        v["position"]["y"] -= lift
    return v


def headline(page, name, measure):
    """The page headline on the Night zone, 28 pt semibold. The card centres its line 2.2 px above the comp's (measured in
    build step 6 on page 2's tile render with the Night zone drawn in; step 5 could not see the header), so the card sits
    2 px under its slot, on both pages alike."""
    v = dyn(page, name, measure, size=28, colour=ZONE_TEXT, font=DISPLAY)
    v["position"]["y"] += 2
    return v


# A cardVisual centres its text block in its box, at a 21.9 px pitch for 12 pt, and shows a line only when the box leaves
# room for it (2 lines from 60 px, 3 from 88; the calibration page of build step 5, 13 Nov). The comp sets the same lines
# from the top of the slot at 21.3 px. So a note of n lines gets the height CARD_H[n], centred on the comp's text block:
# every line then lands within 1 px of the comp. The box overlaps its neighbours a little; the card is transparent.
CARD_H = {1: 24, 2: 64, 3: 92, 4: 120}


def note(page, name, measure, lines, colour=INK2):
    v = dyn(page, name, measure, colour=colour)
    y = SLOT[page][name]["y"]
    centre = y + lines * 21.3 / 2 - 0.7  # measured on the stitched page render: the five notes land within 2 px
    v["position"]["height"] = CARD_H[lines]
    v["position"]["y"] = round(centre - CARD_H[lines] / 2)
    return v


def p1_visuals():
    """FinalV3 build step 5 (doc 23): P1 as the comp rebuild-comp-v10.html (#p1) draws it; slots from the v10 slot map,
    content from doc 20, construction from doc 21 sections 4.1 to 4.5 and doc 22 sections 2 and 3. Every sentence is a
    measure of TEXT_SLOTS (sketch_model.py) or a typed slot of TEXT_STATIC; the numbers are label-safe (P-1)."""
    # headline and subtitle as cards, like P2's, so the two headers sit on one grid (REVIEW p2)
    # on the night zone (plan 10 D3): masthead and subtitle in ZONE_MUTED (10.2:1 on Night), the headline in ZONE_TEXT
    v = [headline(P1, "z_headline", "Headline P1 (text)"),
         dyn(P1, "c_subtitle", "Subtitle P1 Briefing (text)", size=S, colour=ZONE_MUTED)]

    # the KPI band: four cells in one card; values are text measures, one formatter with the context line (REVIEW M7).
    # R-P1-2: each label leads with the code of the finding it belongs to.
    v += kpi_cell("kpi_occ", "Occupancy", "KPI Occupancy GI (text)", "KPI Occupancy Context (text)", "Alt KPI Occupancy (text)", "KPI Occupancy Context Color", "F4")
    v += kpi_cell("kpi_margin", "Operating margin after commissions", "KPI Margin after GI (text)", "KPI Margin after Context (text)", "Alt KPI Margin after (text)", "KPI Margin after Context Color", "F1")
    v += kpi_cell("kpi_ota", "Room revenue booked through online agencies", "KPI OTA GI (text)", "KPI OTA Context (text)", "Alt KPI OTA (text)", "KPI OTA Context Color", "F2")
    # plan 09 R2: NPS as a guest-quality signal, not the brand's one number (Keiningham et al. 2007; CREDITS.md).
    v += kpi_cell("kpi_nps", "Guest quality: net promoter score (−100 to +100)", "KPI NPS GI (text)", "KPI NPS Context (text)", "Alt KPI NPS (text)", "KPI NPS Context Color", "F3")

    k = lambda name, txt: kicker(P1, name, txt, code_colour=INK, sep=" · ")  # noqa: E731  (R-G3: the code in Night)
    # F1 the margin (4.2): the margin after commissions with the commissions band stacked on it
    v += [k("c_f1_kicker", "F1 · THE MARGIN"), title(P1, "c_f1_title", "F1 Title (text)", "Alt F1 Title (text)", lift=5)]
    v.append(f1_area(P1, "ch_f1_margin"))
    v.append(note(P1, "c_f1_note", "F1 Note (text)", 3))
    v.append(link_line(P1, "lnk_f1", "→ Page 2: revenue management and the kiosks."))

    # F2 the middleman (4.3): two lines named at their ends, no legend and no value axis; the folio under it
    v += [k("c_f2_kicker", "F2 · THE MIDDLEMAN"), title(P1, "c_f2_title", "F2 Title (text)", "Alt F2 Title (text)", lift=5)]
    v.append(f2_ends(P1, "ch_f2_ota"))
    v.append(f2_folio_v10(P1, "tbl_f2_folio"))
    v.append(note(P1, "c_f2_note", "F2 Note (text)", 3))
    v.append(link_line(P1, "lnk_f2", "→ Page 2: the booking app with member rates."))

    # F3 the fading welcome (4.4): label-safe values over the bars; a bar opens the band's detail
    v += [k("c_f3_kicker", "F3 · THE FADING WELCOME"), title(P1, "c_f3_title", "F3 Title (text)", "Alt F3 Title (text)", lift=5)]
    v.append(f3_chart(P1, "ch_f3_age", tooltip_page=TT_F3, measure="NPS 2025 (label-safe)", v10=True))
    cnt = dyn(P1, "c_f3_count", "F3 Count (text)")
    cnt["position"]["y"] -= 3  # the card centres its line 3 px under the comp's (stitched render)
    v.append(cnt)
    v.append(note(P1, "c_f3_note", "F3 Note (text)", 3))
    v.append(link_line(P1, "lnk_f3", "→ Page 2: the refresh waits for the 2028 gate, and why."))

    # F4 where we are full (4.5, doc 22 section 3): the note and link at the left, the three location-type rows, the
    # dot plot of the 50 hotels on the average diamonds, the seven names as text boxes
    v += [k("c_f4_kicker", "F4 · WHERE WE ARE FULL"), title(P1, "c_f4_title", "F4 Title (text)", "Alt F4 Title (text)", lift=5)]
    v.append(note(P1, "c_f4_note", "F4 Note (text)", 2))
    # the number of kiosk hotels comes from the model (a11y_check: no typed number but a year), so this link is a card
    v.append(note(P1, "lnk_f4", "Link F4 (text)", 2, colour=INK))
    v += f4_rows(P1, "c_f4_rows")
    v += f4_dot_plot(P1, tooltip_page=TT_F4)
    v += f4_names(P1)

    # the footer row: source line, the page button (P-2, S-6) and the Definitions chip (P-7)
    v.append(tb(P1, "z_footer", FOOTER, alt="Source: Pillow & Key Group dataset. Guest scores weighted by survey responses; 2021 is a depressed base year."))
    v.append(nav_button(P1, "btn_next", "Next: what we fund, and why →", P2, "Next what we fund and why: page 2, The Investment Strategy"))
    v.append(chip_native(P1, "chip_def", "Chip Definitions (text)", TT_GLOSS, "Alt Definitions (text)"))
    # P-7 hover tags on the two cards whose visuals open a detail page
    v += [hover_tag_text(P1, "tag_f3", "Hover a bar", 3), hover_tag_text(P1, "tag_f4", "Hover a hotel", 4)]
    return v


# ---------------------------------------------------------------------- FinalV3 P1 builders (build step 5)
# A chart's slot is where the comp draws the chart; Power BI lays its plot area out inside the visual with margins of its
# own (axis labels, series names). PLOT_RECT is the visual rect that puts Power BI's plot where the comp has it, measured on
# the stitched page render of step 5 (tools/desktop_shots/tiles). The slot map keeps the comp's rects.
PLOT_RECT = {"ch_f1_margin": (68, 392, 526, 248), "ch_f2_ota": (700, 397, 505, 144), "ch_f3_age": (1310, 392, 560, 221)}


def plot_rect(v, rect):
    v["position"].update({"x": rect[0], "y": rect[1], "width": rect[2], "height": rect[3]})
    return v



# the ring-i of the hover tags: Burnt Tangerine, not the comp's Tangerine (#E05A22 is 3.7:1 on white, a11y_check's floor is
# 4.5:1 for any text run; Burnt Tangerine is 6.2:1, the kit's text cut of the same hue)
TAG_I = BAD


def link_line(page, name, txt):
    """A forward link line under a finding (R-P1-3 to R-P1-7): a static text box in Night at 12 pt. It points at the move
    on page 2 that answers the finding; the page button in the footer row does the navigation (one control, P-2)."""
    return tb(page, name, txt, colour=INK)


def hover_tag_text(page, name, words, i):
    """P-7 hover tag, native: a text box with two runs, the ring-i (U+24D8, S-8 passed) in Tangerine and the words in
    Night, on a white fill with a 1 px Seam border and radius 14. Decorative (an instruction to the mouse; every hover
    target's alt text says what the hover shows)."""
    v = textbox(name, *at(page, name), [[("ⓘ", BODY, SPX, TAG_I, False), (" " + words, BODY, SPX, INK, False)]], alt=None)
    vc = v["visual"]["visualContainerObjects"]
    vc["background"] = [{"properties": {"show": b(True), "color": color(SURFACE), "transparency": num(0)}}]
    vc["border"] = [{"properties": {"show": b(True), "color": color(HAIR), "radius": num(14), "width": num(1)}}]
    vc["padding"] = [{"properties": {"top": num(1), "bottom": num(0), "left": num(12), "right": num(4)}}]
    return decorative(v, 700 + i)


def chip_native(page, name, text_measure, tooltip_page, alt_measure):
    """P-7 Definitions chip: one cardVisual with its own container fill, border and radius, the text measure in Night,
    the tooltip page bound to it (the SVG pill under it is gone)."""
    v = card(name, *at(page, name), [text_measure], BODY, S, INK)
    vc = v["visual"]["visualContainerObjects"]
    vc["background"] = [{"properties": {"show": b(True), "color": color(SURFACE), "transparency": num(0)}}]
    vc["border"] = [{"properties": {"show": b(True), "color": color(HAIR), "radius": num(14), "width": num(1)}}]
    vc["padding"] = [{"properties": {"top": num(0), "bottom": num(3), "left": num(12), "right": num(12)}}]
    vc["visualTooltip"] = page_tooltip(tooltip_page)
    return bind_alt(v, alt_measure)


def nav_button(page, name, label, target, alt):
    """P-2 small control on a light surface, primary: a pill in Night with white 12 pt text; hover and pressed take the
    Seam fill with Night text (the theme's light-surface hover). The page-navigation link is S-6's shape
    (visualContainerObjects.visualLink: type PageNavigation, navigationSection = the page's folder name)."""
    st = ("hover", "selected")
    _, _, _, h_, _, _ = at(page, name)
    # the pill: tileShape rectangleRoundedByPixel with half the height, on the default state. Tried on the scratch page of step 5:
    # a shape without a selector is ignored, and 'pill' pushes the label under the middle and clips it.
    objs = {"shape": [{"properties": {"tileShape": enum("rectangleRoundedByPixel"), "rectangleRoundedCurve": integer(h_ // 2)}, "selector": {"id": "default"}}],
            "icon": [{"properties": {"shapeType": text("blank")}, "selector": {"id": "default"}}],
            "text": [{"properties": {"show": b(True)}},
                     {"properties": {"text": text(label), "fontFamily": text(BODY), "fontSize": num(S), "fontColor": color(SURFACE), "bold": b(False),
                                     "topMargin": integer(0), "bottomMargin": integer(3)}, "selector": {"id": "default"}},
                     *[{"properties": {"text": text(label), "fontColor": color(INK)}, "selector": {"id": s_}} for s_ in st]],
            "fill": [{"properties": {"show": b(True)}},
                     {"properties": {"fillColor": color(INK), "transparency": num(0)}, "selector": {"id": "default"}},
                     *[{"properties": {"fillColor": color(HAIR), "transparency": num(0)}, "selector": {"id": s_}} for s_ in st]],
            "outline": [{"properties": {"show": b(False)}}]}
    vcos = vco(alt=alt, padding=0)
    vcos["visualLink"] = [{"properties": {"show": b(True), "type": enum("PageNavigation"), "navigationSection": text(target)}}]
    return visual(name, "actionButton", *at(page, name), objects=objs, vcos=vcos)


def f1_area(page, slot):
    """F1 (doc 21 4.2, S-5 passed): a stacked area chart. The base series, the margin after commissions, is a 3 px Coffee
    Blue line with no fill (lineStyles.areaShow false on its selector); the commissions band stacked on it is Warm Grey
    at 70 % transparency with a 2 px Warm Grey edge, so its top edge is the margin before commissions. The value axis
    30 % to 50 % (the base is unfilled, so a cut axis distorts no area). Series named at the right, no legend; the series
    labels' default grey background off (step 1 open item)."""
    ms = ["Trend Margin after GI", "Trend Commission Take GI"]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]},
         "Y": {"projections": [proj_mea(ms[0], "After commissions"), proj_mea(ms[1], "Commissions")]}}
    ls = line_styles({mref(ms[0]): 3, mref(ms[1]): 2})
    ls[1]["properties"]["areaShow"] = b(False)
    ls[2]["properties"]["areaShow"] = b(True)
    # a categorical year axis: each year sits in the middle of its band, as the comp draws it (a scalar axis starts the lines on the plot's edges)
    objs = {"categoryAxis": axis(BODY, S, INK2, extra={"axisType": enum("Categorical")}),
            "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, start=0.3, end=0.5, extra={"labelPrecision": integer(0)}),
            "legend": legend(False),
            "labels": [{"properties": {"show": b(False)}}],
            "seriesLabels": [{"properties": {"show": b(True), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2),
                                             "textSize": num(S), "seriesFontFamily": text(BODY), "enableBackground": b(False), "leaderLines": b(False)}}],
            "dataPoint": [{"properties": {"transparency": num(70)}}] + series_colors({mref(ms[0]): ACCENT_MARK, mref(ms[1]): SLATE}),
            "lineStyles": ls}
    return plot_rect(chart(page, slot, "stackedAreaChart", q, objs, None, filters=[YEARS()], alt_measure="Alt F1 Chart (text)"), PLOT_RECT[slot])


def f2_ends(page, slot):
    """F2 (doc 21 4.3, P-5): the Goodnight Inn line (3 px Coffee Blue) and the other three brands as one line (2 px Warm
    Grey), named at their right ends; no legend, no value axis. The numbers are two label-only series on the same axis,
    without a line or marker: Trend OTA GI (ends) carries 2021 and 2025 above the blue line, Trend OTA Sisters (end) 2025
    below the grey one. Whole percentages, so they need no label-safe twin."""
    gi, si, gi_e, si_e = "Trend OTA GI", "Trend OTA Sisters", "Trend OTA GI (ends)", "Trend OTA Sisters (end)"
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]},
         "Y": {"projections": [proj_mea(gi, "Goodnight Inn"), proj_mea(si, "The other three brands"), proj_mea(gi_e, "Goodnight Inn, first and last year"),
                               proj_mea(si_e, "The other three brands, last year")]}}
    ls = line_styles({mref(gi): 3, mref(si): 2})
    ls += [{"properties": {"strokeShow": b(False), "showMarker": b(False)}, "selector": {"metadata": mref(m_)}} for m_ in (gi_e, si_e)]
    lab = {"fontFamily": text(BODY), "fontSize": num(S), "color": color(INK2), "labelDisplayUnits": integer(1), "labelPrecision": integer(0), "enableBackground": b(False)}
    objs = {"categoryAxis": axis(BODY, S, INK2, extra={"axisType": enum("Categorical")}),
            # the comp's 20 % to 55 % in 90 px; Power BI's plot is 101 px high in this rect, so the ends that give the same
            # pixels per point (50 % at page y 431, 33 % at 475)
            "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, start=0.201, end=0.594),
            "legend": legend(False),
            "labels": [{"properties": {"show": b(True), **lab}},
                       *[{"properties": {"showSeries": b(False)}, "selector": {"metadata": mref(m_)}} for m_ in (gi, si)],
                       {"properties": {"showSeries": b(True), "labelPosition": enum("Above")}, "selector": {"metadata": mref(gi_e)}},
                       {"properties": {"showSeries": b(True), "labelPosition": enum("Under")}, "selector": {"metadata": mref(si_e)}}],
            "seriesLabels": [{"properties": {"show": b(True), "seriesPosition": enum("Right"), "seriesMatchColor": b(False), "seriesColor": color(INK2),
                                             "textSize": num(S), "seriesFontFamily": text(BODY), "enableBackground": b(False), "leaderLines": b(False)}},
                             *[{"properties": {"show": b(False)}, "selector": {"metadata": mref(m_)}} for m_ in (gi_e, si_e)]],
            "dataPoint": series_colors({mref(gi): ACCENT_MARK, mref(si): SLATE, mref(gi_e): ACCENT_MARK, mref(si_e): SLATE}),
            "lineStyles": ls}
    return plot_rect(chart(page, slot, "lineChart", q, objs, None, filters=[YEARS()], alt_measure="Alt F2 Chart (text)"), PLOT_RECT[slot])


FOLIO_COLS = (216, 171, 171)  # the spec's 216 / 172 / 172, less the 2 px a table needs beyond its columns (step 2, S-2 point 4)
# Row padding: a 12 pt header is 32.6 px at padding 0 and a row 21.3 (step 2, S-3), each plus twice the padding. The comp's
# 28 + 3 x 28 needs 112 with a header as tall as a row, which a native table cannot do: at 3.36 the table scrolled (render 1
# of step 5), at 1.8 too. 1.2 gives a 35 px header and 23.7 px rows, 106 px in the 112 slot (a deviation of the row pitch, logged).
FOLIO_PAD = 1.2


def f2_folio_v10(page, slot):
    """The folio table as the spec's construction.tables.tbl_f2_folio, as near as a native table gets (FOLIO_PAD): fixed
    columns, the header ruled in Dusk underneath, the rows in Seam."""
    fol = ("Folio OTA Guest (text)", "Folio Direct Guest (text)")
    proj = [proj_col("FolioLine", "Line", display="One room night, 2025"), proj_mea(fol[0], "Via an online agency"), proj_mea(fol[1], "Direct, web and app")]
    colfmt = [{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": mref(m_)}} for m_ in fol]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=FOLIO_PAD, header_size=S, column_formatting=colfmt)
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    objs["values"][0]["properties"]["wordWrap"] = b(False)
    objs["columnWidth"] = [{"properties": {"value": num(w)}, "selector": {"metadata": q_}}
                           for q_, w in zip(("FolioLine.Line", mref(fol[0]), mref(fol[1])), FOLIO_COLS)]
    t = visual(slot, "tableEx", *at(page, slot), query={"Values": {"projections": proj}}, objects=objs, filters=[gi_filter()], vcos=vco(padding=0))
    return bind_alt(t, "Alt F2 Folio (text)")


# F4 (doc 21 4.5 with doc 22 section 3): one plot area for both scatter layers, fixed ends from the spec
F4_X, F4_Y = (0.6, 0.95), (0.5, 3.5)
# S-4 (doc 22 section 5), measured on the stitched page render of step 5: in the slot 656, 872, 1208, 144 Power BI's plot area
# runs x 672.7 to 1848.7 and y 881.1 to 988 (margins 16.7 / 15.3 / 9.1 / 28); the comp's runs 672 to 1840 and 872 to 992. The two
# layers take the rect that puts Power BI's plot on the comp's, so the dots land where the comp has them and the seven name
# boxes keep the spec's positions (a shift alone cannot do it: the scale differed by 0.7 %).
F4_RECT = (655, 863, 1200, 161)
F4_ROWS = (("airport", "Airport", "Occupancy Airport GI (text)"), ("city", "City", "Occupancy City GI (text)"), ("highway", "Highway", "Occupancy Highway GI (text)"))
# where each value starts after its label in the 160 px slot: the label's width at 16 px Segoe UI plus a space (4.4 px),
# from `powerbi-report-author text measure` (49.5 / 27.0 / 61.2 px); set to the render in build step 5
F4_VALUE_DX = {"airport": 54, "city": 31, "highway": 66}


def f4_rows(page, slot):
    """'Airport 82.0%', 'City 79.1%', 'Highway 77.5%' as three rows of 40 px in the slot (the comp's part(i * 40, 40)): per
    row a text box with the type in Dusk and a card with the value in Night semibold beside it (a card's label can only
    sit above or below its value). One tab stop: the first value card reads the three (Alt F4 Types (text))."""
    x, y, w, h, z, tab = at(page, slot)
    out = []
    for i, (key, label, measure) in enumerate(F4_ROWS):
        ry = y + 40 * i + 8
        lab = textbox(f"{slot}_lab_{key}", x, ry, 72, 24, z, 0, [[(label, BODY, SPX, INK2, False)]])
        name = slot if i == 0 else f"{slot}_{key}"
        val = card(name, x + F4_VALUE_DX[key], ry, w - F4_VALUE_DX[key], 24, z, tab, [measure], DISPLAY, S, INK, off_grid=True)
        out.append(decorative(lab, 140 + i))
        out.append(bind_alt(val, "Alt F4 Types (text)") if i == 0 else decorative(val, 150 + i))
    return out


def f4_axes(objs, labels_colour):
    objs["categoryAxis"] = axis(BODY, S, labels_colour, gridlines=True, grid_color=HAIR, start=F4_X[0], end=F4_X[1], extra={"labelPrecision": integer(0), "labelDisplayUnits": integer(1)})
    objs["valueAxis"] = axis(BODY, S, INK2, show=False, gridlines=False, start=F4_Y[0], end=F4_Y[1])
    return objs


def f4_dot_plot(page, tooltip_page=None):
    """Two scatter layers on one rect (ch_f4_avg under ch_f4_dots), the same axis ends, so their plot areas match. Bottom:
    three Dusk diamonds, one per location type at its 2025 occupancy; the same axis as the top layer (labels and
    gridlines drawn twice on the same pixels: a white label here would fail a11y_check), so the plot areas match. Top: the 50 hotels at (Occupancy % 2025, F4 Row Y), Night for the
    seven fullest and Warm Grey for the rest (F4 Dot Color), no category labels (doc 22: the names are text boxes), the X
    axis ticks and gridlines, and the 90 % constant line dashed in Dusk with its label; it opens the hotel's tooltip page."""
    x, y, w, h, z, tab = at(page, "ch_f4_dots")
    base = {"legend": legend(False), "categoryLabels": [{"properties": {"show": b(False)}}],
            "markers": [{"properties": {"borderShow": b(False)}}],
            "bubbles": [{"properties": {"bubbleSize": integer(-10), "markerRangeType": enum("magnitude"), "preventOverflow": b(False)}}]}
    # bottom layer: the location-type averages
    qa = {"Category": {"projections": [proj_col("Hotels", "LocationType", display="Location type")]},
          "X": {"projections": [proj_mea("F4 Type Avg", "Occupancy 2025")]}, "Y": {"projections": [proj_mea("F4 Row Y", "Row")]}}
    oa = f4_axes(copy.deepcopy(base), INK2)
    oa["bubbles"][0]["properties"].update({"markerShape": enum("diamond"), "bubbleSize": integer(0)})
    oa["dataPoint"] = [{"properties": {"fill": color(INK2)}, "selector": WILD}]
    _, _, _, _, za, ta = at(page, "ch_f4_avg")
    avg = decorative(visual("ch_f4_avg", "scatterChart", *F4_RECT, za, ta, query=qa, objects=oa, filters=[gi_filter()], vcos=vco(padding=0), off_grid=True), 160)
    # top layer: the hotels
    qd = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name", display="Hotel")]},
          "X": {"projections": [proj_mea("Occupancy % 2025", "Occupancy 2025")]}, "Y": {"projections": [proj_mea("F4 Row Y", "Row")]}}
    od = f4_axes(copy.deepcopy(base), INK2)
    od["dataPoint"] = [{"properties": {"fill": fv("F4 Dot Color")}, "selector": WILD}]
    od["xAxisReferenceLine"] = [{"properties": {"show": b(True), "value": num(0.9), "lineColor": color(INK2), "transparency": num(0), "width": num(1), "style": enum("dashed"),
                                                "position": enum("back"), "displayName": text("90%"), "dataLabelShow": b(True), "dataLabelText": enum("Name"),
                                                "dataLabelColor": color(INK), "dataLabelHorizontalPosition": enum("right"), "dataLabelVerticalPosition": enum("under")},
                                 "selector": {"id": "1"}}]
    vc = vco(padding=0)
    if tooltip_page:
        vc["visualTooltip"] = page_tooltip(tooltip_page)
    dots = bind_alt(visual("ch_f4_dots", "scatterChart", *F4_RECT, z, tab, query=qd, objects=od, filters=[gi_filter()], vcos=vc, off_grid=True), "Alt F4 Chart (text)")
    return [avg, dots]


F4_NAMES = ("kingston", "orlando", "kuala_lumpur", "kansas_city", "phoenix", "gatwick_montreal", "toronto")
F4_NAME_TEXT = {"kingston": "Kingston", "orlando": "Orlando", "kuala_lumpur": "Kuala Lumpur", "kansas_city": "Kansas City", "phoenix": "Phoenix",
                "gatwick_montreal": "Gatwick, Montréal", "toronto": "Toronto"}
F4_NAME_DX = 0  # S-4: the shift of the seven boxes when the rendered plot area differs from the comp's (x 16 to 1184 in the visual)


def f4_names(page):
    """The seven name boxes beside their dots (doc 22 section 3): 12 pt Night on a white fill, no border, decorative and
    out of the tab order. Static: P1 does not follow the scenario, so the dots never move; the placement avoids all 50
    dots, so no box covers a dot's tooltip. Positions from the spec (construction.charts.ch_f4.name_slots), not on the grid."""
    out = []
    for i, key in enumerate(F4_NAMES):
        name = f"lbl_f4_{key}"
        x, y, w, h, z, tab = at(page, name)
        v = textbox(name, x + F4_NAME_DX, y, w, h, z, tab, [[(F4_NAME_TEXT[key], BODY, SPX, INK, False)]], off_grid=True)
        v["visual"]["visualContainerObjects"]["background"] = [{"properties": {"show": b(True), "color": color(SURFACE), "transparency": num(0)}}]
        out.append(decorative(v, 170 + i))
    return out


YEARS = lambda: filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_hist")  # noqa: E731


def f3_chart(page, slot, tooltip_page=None, measure="NPS 2025 (signed)", v10=False):
    """measure (FinalV3 step 5, P-1): on P1 the label-safe twin, so the bars print '+6.8' and '−4.9' in any locale."""
    q = {"Category": {"projections": [proj_col("Hotels", "Renovation Age Label", display="Years since the last renovation")]}, "Y": {"projections": [proj_mea(measure, "NPS 2025")]}}
    objs = {"categoryAxis": axis(BODY, S, INK), "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False),
            "dataPoint": [{"properties": {"fill": fv("Age Band Color")}, "selector": WILD}], "labels": labels(True, BODY, 12, INK), "legend": legend(False),
            # the zero line the bars hang from (REVIEW m4); same object shape as the scatter's, which Desktop rendered
            # FinalV2 (plan 15 N4): 2 px, a line and not a bar (Björn, 7 Nov: thin, in Dusk); the width key as on the scatter's line
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "width": num(2), "style": enum("solid"), "position": enum("front"),
                                                    "dataLabelShow": b(False)}, "selector": {"id": "1"}}]}
    if v10:
        # The comp's bars: 72 px wide, 186.7 px apart. Power BI's two paddings do not map to that directly; six variants on a
        # scratch page (step 5) gave step 188.4 and width 72.1 at 54 / 26, step 183.0 at 54 / 30. The value ends put zero at
        # page y 500 and +6.8 at 436 in Power BI's plot.
        objs["categoryAxis"][0]["properties"].update({"innerPadding": integer(54), "outerPadding": integer(27)})
        objs["valueAxis"][0]["properties"].update({"start": num(-8.11), "end": num(10.3)})
        return plot_rect(chart(page, slot, "clusteredColumnChart", q, objs, None,
                               filters=[gi_filter(), filter_in("Hotels", "Renovation Age Sort", [1, 2, 3], "flt_dated")], sort=sort_by_column("Hotels", "Renovation Age Label"),
                               alt_measure="Alt F3 Chart (text)", tooltip_page=tooltip_page), PLOT_RECT[slot])
    return chart(page, slot, "clusteredColumnChart", q, objs, None,
                 filters=[gi_filter(), filter_in("Hotels", "Renovation Age Sort", [1, 2, 3], "flt_dated")], sort=sort_by_column("Hotels", "Renovation Age Label"),
                 alt_measure="Alt F3 Chart (text)", tooltip_page=tooltip_page)


# ====================================================================== the hover detail pages (round 6; tt-f1 to tt-f4 left in build step 6, N-4)
TT_F3, TT_F4 = "tt-f3-band", "tt-f4-hotel"
TT_YEAR = "tt-year"  # round 9: the one designed tooltip the three cumulative charts share
TT_GLOSS = "tt-glossary"  # 12 Nov evening (Björn): the definitions page behind the Definitions chip in the footer row of both pages
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
    (weakest guest scores / who fills the hotel). Build step 10: the three figures are text measures (R-G1: points in
    any locale)."""
    if which == TT_F3:
        head, nums, labels_, alt_nums, vs, foot = ("Band Header (text)", ["TT NPS 2025 (text)", "TT Occupancy 2025 (text)", "TT RevPAR 2025 (text)"], ["NPS 2025", "occupancy 2025", "RevPAR 2025"],
                                                  "Alt Band Nums (text)", "Band vs Brand (text)", "Weakest Scores (text)")
        ch_title = "NPS by year, this band against the brand"
        ch = line_pair(which, "ttd_chart", "Date", "Year", "NPS Band (line)", "NPS Brand (line)", "This band", "Goodnight Inn", [YEARS()], alt_measure="Alt NPS Band Line (text)")
    else:
        head, nums, labels_, alt_nums, vs, foot = ("Hotel Header (text)", ["TT Occupancy 2025 (text)", "TT ADR 2025 (text)", "TT RevPAR 2025 (text)"], ["occupancy 2025", "ADR 2025", "RevPAR 2025"],
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
    """The round-6 tooltip pages in the round-7 skin (their own night scene, the kicker and title on the banner,
    the content in cards), Goodnight Inn as a page filter on the two detail pages (the hovered bar brings the band or
    the hotel, not the brand)."""
    out = []
    for pg in (TT_F3, TT_F4):
        out.append(page(pg, pg, finish(no_card_fill(scene_visual(pg) + card_frames(pg) + detail_page_visuals(pg))), tooltip=True,
                        filters=[filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_tt_brand")]))
    out.append(page(TT_YEAR, TT_YEAR, finish(no_card_fill(scene_visual(TT_YEAR) + card_frames(TT_YEAR) + year_page_visuals())), tooltip=True))
    out.append(page(TT_GLOSS, TT_GLOSS, finish(no_card_fill(scene_visual(TT_GLOSS) + card_frames(TT_GLOSS) + glossary_page_visuals())), tooltip=True))
    return out


# 12 Nov evening (Björn): the definitions behind the Definitions chip. The short words of both pages, one line each, in the
# report's own words (the subtitle of P2 already defines NPV in situ; this is the place to look them all up). Years only, no
# typed figures: the rate and the budget live in the model and on the pages.
# Build step 10 (R-TT-3): the report's own words (R-G2), "Case in view" gone; two columns, the decision words of page 2 at
# the left, the scenarios and the measures of page 1 at the right. "Run-rate" and "yield" appear here and nowhere else.
GLOSSARY = ((("Move", "one of the ten investments Goodnight Inn can make."),
             ("Package", "a set of moves funded together. A is the package we recommend."),
             ("Growth", "a move the dataset marks as growth; a package needs at least one."),
             ("Capex", "the one-off investment a move takes; the brand's budget caps what a package may spend."),
             ("NPV", "net present value: benefits minus capex and disruption through 2032, in 2025 dollars at the organisers' rate."),
             ("Pays back by 2032", "the NPV through 2032 is zero or more."),
             ("Cash positive", "from that year on, the cumulative net impact, undiscounted, is above zero."),
             ("A year by 2032", "the operating profit a move adds in a full year once it is live, measured in 2032 (its run-rate)."),
             ("A year on cost", "a year by 2032 divided by capex (a yield).")),
            (("Tranche", "a part of the budget, funded by one Board decision."),
             ("The 2028 gate", "the Board meeting in mid-2028 that decides on the next tranche, by the rule on page 2."),
             ("Low, Expected, High", "the organisers' three scenarios for every move; page 2 follows the one picked under Scenario."),
             ("Topped 90%", "a month in which a hotel sold 90% or more of its room nights."),
             ("NPS", "net promoter score: promoters minus detractors among surveyed guests, weighted by responses."),
             ("ADR", "average daily rate: room revenue per room night sold."),
             ("RevPAR", "revenue per available room: room revenue per room night available, sold or not."),
             ("OTA, online agencies", "booking sites that take a commission on every room night they bring.")))


def glossary_page_visuals():
    pg = TT_GLOSS
    out = [night_kicker(pg, "ttg_kicker", "DEFINITIONS"),
           tb(pg, "ttg_title", "The terms on these pages", font=DISPLAY, size=19, colour=INK)]
    for name, terms, alt in (("ttg_list", GLOSSARY[0], "The words of the investment decision, one line each"),
                             ("ttg_list2", GLOSSARY[1], "The scenarios and the measures of the brand review, one line each")):
        paras = [[(term, DISPLAY, SPX, INK, False), ("  " + what, BODY, SPX, INK2, False)] for term, what in terms]
        out.append(textbox(name, *at(pg, name), paras, alt=alt))
    return out


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


def ctl_button(page, name, label, style, link, alt, large=False):
    """P-2 (doc 21 section 3), one control language: an actionButton in one of three looks, the comp's .btn classes.
    night_on   on the Night masthead, the current tab: Oat White fill, Night text
    night_off  on the Night masthead, secondary: a SOLID Night fill (the hanger artwork runs behind the control row),
               1 px Mist outline, Oat White text; hover and pressed: Mist fill, Night text
    light_sec  on a white card, secondary: white, 1 px Dusk outline, Night text; hover and pressed: Seam fill
    large = a state tab (40 px high, radius 8, Segoe UI Semibold 12 pt); otherwise a pill (radius = half the height,
    Segoe UI 12 pt). link: ("PageNavigation", page folder) as S-6 found it, or ("Bookmark", bookmark name).
    Shape and state selectors as nav_button() (step 5): 'show' without a selector, the look under default / hover /
    selected; the masthead looks set every state themselves, the theme carries the light surface only."""
    x, y, w, h, z, tab = at(page, name)
    fill, ink, line, h_fill, h_ink = {"night_on": (ZONE_TEXT, INK, ZONE_TEXT, ZONE_TEXT, INK), "night_off": (INK, ZONE_TEXT, ZONE_MUTED, ZONE_MUTED, INK),
                                      "light_sec": (SURFACE, INK, INK2, HAIR, INK)}[style]
    st = ("hover", "selected")
    font = DISPLAY if large else BODY
    objs = {"shape": [{"properties": {"tileShape": enum("rectangleRoundedByPixel"), "rectangleRoundedCurve": integer(8 if large else h // 2)}, "selector": {"id": "default"}}],
            "icon": [{"properties": {"shapeType": text("blank")}, "selector": {"id": "default"}}],
            "text": [{"properties": {"show": b(True)}},
                     {"properties": {"text": text(label), "fontFamily": text(font), "fontSize": num(S), "fontColor": color(ink), "bold": b(False),
                                     # a 28 px pill sets its line 1.5 px low without the 3 px (step 5); a 40 px tab centres it
                                     "topMargin": integer(0), "bottomMargin": integer(0 if large else 3)}, "selector": {"id": "default"}},
                     *[{"properties": {"text": text(label), "fontColor": color(h_ink)}, "selector": {"id": s_}} for s_ in st]],
            "fill": [{"properties": {"show": b(True)}},
                     {"properties": {"fillColor": color(fill), "transparency": num(0)}, "selector": {"id": "default"}},
                     *[{"properties": {"fillColor": color(h_fill), "transparency": num(0)}, "selector": {"id": s_}} for s_ in st]],
            "outline": [{"properties": {"show": b(True)}},
                        {"properties": {"lineColor": color(line), "weight": num(1), "transparency": num(0)}, "selector": {"id": "default"}},
                        *[{"properties": {"lineColor": color(line), "weight": num(1), "transparency": num(0)}, "selector": {"id": s_}} for s_ in st]]}
    vcos = vco(alt=alt, padding=0)
    kind, target = link
    vcos["visualLink"] = [{"properties": {"show": b(True), "type": enum(kind), "navigationSection" if kind == "PageNavigation" else "bookmark": text(target)}}]
    return visual(name, "actionButton", x, y, w, h, z, tab, objects=objs, vcos=vcos)


# The tab bar: three tabs in the masthead, each drawn twice (its current and its other look) and shown by the bookmarks,
# so the state in view is always marked. FinalV3 (R-P2-2, doc 21 section 5): the labels of the rebuild. The a11y check
# needs the visible label inside the spoken name letter for letter.
TABS = [("rec", "Recommended: A", "the recommendation, package A"),
        ("alts", "What waits, and why", "the moves that wait for the 2028 gate, and why"),
        ("build", "Build your own", "pick moves and compare your plan with A")]


def tab_bar():
    out = []
    for key, label, what in TABS:
        spoken = re.sub(r"[^A-Za-z ]", "", label)  # the visible label inside the spoken name (WCAG 2.5.3, a11y_check)
        bm = ("Bookmark", f"bm_p2_{key}")
        out.append(ctl_button(P2, f"tab_{key}_on", label, "night_on", bm, f"{spoken}, the current view: {what}", large=True))
        out.append(ctl_button(P2, f"tab_{key}_off", label, "night_off", bm, f"{spoken}: show {what}", large=True))
    return out


def button_slicer(name, table, column, selected, alt, cols, size=S, rows=1, multi=False, night=False):
    """night (FinalV3 step 6, P-2): the pills on the Night masthead: off = solid Night with a 1 px Mist outline and Oat
    White text, hover = Mist with Night text, on = Oat White with Night text, all in regular weight (the comp's .btn.sm).
    The house-style toggle (08-verbeterplan V5/S1, brand-guide section 6 'scenario toggle'): a button slicer whose
    tiles are thin rounded outlines on white, the selected one Night with white text. State ids as the built-in
    themes write them (interaction:hover, selection:selected). Rendered 7 and 9 Nov."""
    x, y, w, h, z, tab = at(P2, name)
    st = lambda i: {"id": i}  # noqa: E731
    radius = (h // rows) // 2 if rows > 1 else h // 2
    # fill, text and outline per state: (default, hover and press, selected)
    f_, t_, o_ = (((INK, ZONE_MUTED, ZONE_TEXT), (ZONE_TEXT, INK, INK), (ZONE_MUTED, ZONE_MUTED, ZONE_TEXT)) if night else
                  ((SURFACE, HAIR, INK), (INK, INK, SURFACE), (INK2, INK2, INK)))
    objs = {
        "shapeCustomRectangle": [{"properties": {"tileShape": enum("rectangleRoundedByPixel"), "rectangleRoundedCurve": integer(radius)}, "selector": st("default")}],
        "layout": [{"properties": {"rowCount": integer(rows), "columnCount": integer(cols), "maxTiles": integer(rows * cols), "cellPadding": integer(8)}}],
        "fillCustom": [{"properties": {"show": b(True), "fillColor": color(f_[0]), "transparency": num(0)}, "selector": st("default")},
                       {"properties": {"fillColor": color(f_[1])}, "selector": st("interaction:hover")},
                       {"properties": {"fillColor": color(f_[1])}, "selector": st("interaction:press")},
                       {"properties": {"fillColor": color(f_[2])}, "selector": st("selection:selected")}],
        "outline": [{"properties": {"show": b(True), "lineColor": color(o_[0]), "weight": num(1), "transparency": num(0)}, "selector": st("default")},
                    {"properties": {"lineColor": color(o_[2])}, "selector": st("selection:selected")}],
        "value": [{"properties": {"show": b(True), "fontFamily": text(BODY), "fontSize": num(size), "fontColor": color(t_[0]), "bold": b(False),
                                  "horizontalAlignment": text("center" if rows == 1 else "left"), "verticalAlignment": text("middle")}, "selector": st("default")},
                  # the hover and press states name their text colour too: on the masthead the hover fill is light
                  *[{"properties": {"fontColor": color(t_[1])}, "selector": st(i_)} for i_ in ("interaction:hover", "interaction:press")],
                  {"properties": {"fontColor": color(t_[2]), "bold": b(not night)}, "selector": st("selection:selected")}],
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


def brand_row(page_name, sfx):
    """The 3.1 lockup on the night zone and the eyebrow beside it (plan 11): first in the reading order, so a screen
    reader starts with whose report this is and which page."""
    pg = PAGES[page_name]
    L = pg["logo"]
    out = [image_file("z_logo", L["x"], L["y"], L["w"], L["h"], 1003, L["tab"], LOCKUP, "Goodnight Inn"),
           # ZONE_EYEBROW on Night 9.5:1; at the 12 pt floor instead of the kit's 11 pt eyebrow
           # FinalV3 (R-P1-1, doc 21 4.1): the rebuilt page 1 says where the reader is, "1 / 2 · THE WAKE-UP CALL · THE BRAND REVIEW"
           tb(page_name, f"z_eyebrow{sfx}", (EYEBROW_V10[page_name] + " · " + EYEBROW[page_name][1]) if page_name in EYEBROW_V10 else "  ·  ".join(EYEBROW[page_name]),
              runs=([(EYEBROW_V10[page_name], DISPLAY, SPX, ZONE_EYEBROW, False), (" · " + EYEBROW[page_name][1], DISPLAY, SPX, ZONE_MUTED, False)] if page_name in EYEBROW_V10 else
                    [(EYEBROW[page_name][0], DISPLAY, SPX, ZONE_EYEBROW, False), ("  ·  " + EYEBROW[page_name][1], DISPLAY, SPX, ZONE_MUTED, False)]),
              alt=("Page 1 of 2, the wake-up call: the brand review" if sfx == "" else "Page 2 of 2, room to invest: the investment strategy"))]
    return out


# FinalV3 build step 8 (doc 21 7.1, spec charts.hero_s_packages): the proof chart's axes are the spec's, typed once. Every
# layer carries the same ends and the same tick format (whole $M, sketch_model SUSDM0 / USDM0), so the plot areas match.
PROOF_X, PROOF_Y = (5_000_000, 62_000_000), (-60_000_000, 20_000_000)
# The visual rect that puts Power BI's plot on the comp's (PLOT_RECT of step 5): the comp draws the plot at x 144 to 716 and
# y 280 to 588 of the page (x0 88, x1 w - 12, y0 8, y1 h - 52 inside the slot 56, 272, 672, 368). Measured in build step 8.
PROOF_RECT = (56, 268, 682, 369)
# The A/B/C layer: the lettered discs of the comp (R-W-1, R-W-4), 22 px (Named Point Size (small) at this multiplier). On a
# sized dot Power BI sets the category label under the dot at this plot size (measured again in step 8), so the letters are a
# layer of their own (sketch_model PROOF_LETTER_LIFT): the tag under the dot, doc 21 7.1's fallback, is not needed.
NAMED_BUBBLE = -22
# the cloud's dots: 8 px, the comp's r 4 (0 gave 11 px; measured in step 8)
CLOUD_BUBBLE = -15


def scatter_axes(objs):
    """The scatter's axis ends, shared by all layers so their plot areas match exactly."""
    objs["categoryAxis"][0]["properties"].update({"start": num(PROOF_X[0]), "end": num(PROOF_X[1])})
    objs["valueAxis"][0]["properties"].update({"start": num(PROOF_Y[0]), "end": num(PROOF_Y[1])})
    return objs


# Build step 9, the plan dot: 12 px (the comp's r 6). Without a size field bubbleSize -15 gives 8 px (build step 8), 5 gave
# 14.1 px and 2 gives 13.1 px on the strip render of step 9 (the comp's dot reads 11 to 12 px there).
YOU_BUBBLE = 2
# The name "You" above the plan dot (doc 22 section 3): a layer of its own with both axes hidden, so its plot is its visual
# rect, and a value axis that runs YOU_HEAD above the proof chart's: the name hangs from an invisible point 42.7 px above the
# dot (sketch_model YOU_LABEL_LIFT), and that point of a plan near the top of the chart lies above +$20M (A in the High
# case: +$12.7M + $11.1M). Same scale as the proof chart: 308 px for $80M, so $20M more are 77 px more.
YOU_HEAD = 20_000_000
# the proof chart's plot (page x 144 to 716, y 280 to 588), 77 px taller at the top, and 8 px higher: at (144, 203) the name
# stood 7.4 px under the comp's (strip render of step 9); at 195 it is within 1.5 px in Low, Expected and High
YOU_RECT = (144, 195, 572, 385)


def you_label(slot, z):
    q = {"Category": {"projections": [proj_col("BuildPoint", "Name", display="Your plan")]},
         "X": {"projections": [proj_mea("Build Capex", "Capex")]}, "Y": {"projections": [proj_mea("Build You Label NPV", "NPV through 2032")]}}
    objs = {"categoryAxis": axis(BODY, S, INK2, show=False, gridlines=False, units=1, start=PROOF_X[0], end=PROOF_X[1]),
            "valueAxis": axis(BODY, S, INK2, show=False, gridlines=False, units=1, start=PROOF_Y[0], end=PROOF_Y[1] + YOU_HEAD),
            "bubbles": [{"properties": {"bubbleSize": integer(CLOUD_BUBBLE), "markerRangeType": enum("magnitude"), "preventOverflow": b(False)}}], "legend": legend(False),
            "markers": [{"properties": {"transparency": num(100), "borderShow": b(False)}}],
            "categoryLabels": [{"properties": {"show": b(True), "fontFamily": text(DISPLAY), "fontSize": num(S), "color": fv("Build You Ink"), "bold": b(True),
                                               "enableBackground": b(True)}}]}  # white and opaque from the theme (compile_theme.py)
    x, y, w, h = YOU_RECT
    return visual(f"{slot}_you", "scatterChart", x, y, w, h, z, 0, query=q, objects=objs, vcos=vco(padding=0), off_grid=True)


def scatter_stack(slot, deco_base):
    """The proof chart (R-W-1): the package scatter as layers on one plot area (same axis ends and tick formats,
    preventOverflow off on all, so the plot areas match). 1 the cloud: every package but A, B and C, Warm Grey. 2 the plan
    being built, one dot under the discs (Build state only). 3 A, B and C as 22 px discs: Power BI draws larger markers
    first, so a cloud in the same visual painted over B and C (REVIEW M2). 4 their letters. 5 the plan's name "You" above its
    dot (Build only; you_label()). 6 a hover layer on top: all 456 packages, fully transparent markers, wired to the tooltip
    page, so every dot shows its own card (08-verbeterplan V2). The band where a package pays back by 2032 is shaded and
    named at its right end.
    z and tab order of the layers: opzet-layering.json."""
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
            # The zero line in Dusk (the comp). The band above it, where a package pays back by 2032, is shaded in Coffee
            # Blue at 90 % transparency (Ice, the spec's #EAF2FB, on white) and says so at its right end.
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("back"), "displayName": text("Pays back by 2032"),
                                                    "dataLabelShow": b(True), "dataLabelText": text("Name"), "dataLabelColor": color(INK2),
                                                    "dataLabelHorizontalPosition": enum("right"), "dataLabelVerticalPosition": enum("above"),
                                                    "shadeShow": b(True), "shadeRegion": enum("after"), "shadeColor": color(ACCENT_MARK), "shadeTransparency": num(90)},
                                     "selector": {"id": "1"}}]}
    scatter_axes(objs)
    x, y, w, h, z, tab = at(P2, slot)
    if PROOF_RECT:
        x, y, w, h = PROOF_RECT
    place = lambda *a, **k: visual(*a, **k, off_grid=True)  # noqa: E731  (PROOF_RECT is measured, not placed by hand)
    q_cloud = {k: val for k, val in q.items() if k != "Size"}
    o_cloud = copy.deepcopy(objs)
    o_cloud["bubbles"][0]["properties"]["bubbleSize"] = integer(CLOUD_BUBBLE)
    # The cloud is a tab stop after the A/B/C layer (pass-3 review: the package card is hover-only). Its header gives
    # 'Show as table', and the card's facts ride in its Tooltips well, so a keyboard user reads every package's
    # capex, NPV, payback, range and initiatives there (the axis measures print whole $M since step 8, so the exact
    # amounts ride along as text). The hover layer stays out of the tab order (mouse only).
    q_cloud_kb = {**q_cloud, "Tooltips": {"projections": [proj_mea("TT Capex (text)", "Capex, exact"), proj_mea("TT NPV (text)", "NPV through 2032, exact"),
                                                          proj_mea("TT Payback (text)", "Payback"), proj_mea("TT Range (text)", "NPV in Low, Expected, High"),
                                                          proj_mea("TT Moves (text)", "Moves and their NPV"), proj_mea("TT Not Included (text)", "Not in it")]}}
    v.append(bind_alt(place(slot, "scatterChart", x, y, w, h, z, tab + 1, query=q_cloud_kb, objects=o_cloud, filters=[filter_in("Package", "Preset", [""], "flt_cloud")],
                            vcos=vco(padding=0)), "Alt Scatter Cloud (text)"))
    quiet = lambda o: (o["valueAxis"][0]["properties"].__setitem__("gridlineShow", b(False)), o.pop("y1AxisReferenceLine", None), o)[-1]  # noqa: E731
    # the plan being built (R-B-3, doc 22 section 3): one dot from the one-row BuildPoint table at (Build Capex, Build NPV),
    # 12 px (the comp's r 6), Night, Tangerine while over the budget (Build Point Color), drawn under the discs (layering
    # file): at the opening state it lies under A. No size field: the point is blank, so absent, while nothing is picked.
    # Shown in the Build state only (STATE_ONLY): the comp draws no "You" in What waits.
    q4 = {"Category": {"projections": [proj_col("BuildPoint", "Label", display="Your plan")]},
          "X": {"projections": [proj_mea("Build Capex", "Capex")]}, "Y": {"projections": [proj_mea("Build NPV (sel)", "NPV through 2032")]}}
    o4 = quiet(copy.deepcopy(objs))
    o4["dataPoint"] = [{"properties": {"fill": fv("Build Point Color")}, "selector": WILD}]
    o4["bubbles"][0]["properties"]["bubbleSize"] = integer(YOU_BUBBLE)
    v.append(decorative(place(f"{slot}_build", "scatterChart", x, y, w, h, z + 3, 0, query=q4, objects=o4, vcos=vco(padding=0)), deco_base + 1))
    # A, B and C: their own, equal size (Named Point Size (small)), no label of their own
    q2 = {**q, "Category": {"projections": [proj_col("Package", "Preset", display="Package")]},
          "Size": {"projections": [proj_mea("Named Point Size (small)", "Marker size")]}}
    o2 = quiet(copy.deepcopy(objs))
    o2["dataPoint"] = [{"properties": {"fill": fv("Named Point Color")}, "selector": WILD}]
    o2["bubbles"][0]["properties"]["bubbleSize"] = integer(NAMED_BUBBLE)
    named = [filter_in("Package", "Preset", ["A", "B", "C"], "flt_named")]
    v.append(bind_alt(place(f"{slot}_named", "scatterChart", x, y, w, h, z + 2, tab, query=q2, objects=o2, filters=named, vcos=vco(padding=0)), "Alt Scatter (text)"))
    # their letters: the same three packages as invisible, unsized points a fixed lift above their dots, so the label Power
    # BI sets under each point lands in the middle of its disc (sketch_model PROOF_LETTER_LIFT). White semibold, decorative.
    qL = {"Category": {"projections": [proj_col("Package", "Preset", display="Package")]}, "X": q["X"],
          "Y": {"projections": [proj_mea("Named Letter NPV (sel)", "NPV through 2032")]}}
    oL = quiet(copy.deepcopy(o_cloud))
    oL["markers"] = [{"properties": {"transparency": num(100), "borderShow": b(False)}}]
    oL["dataPoint"] = [{"properties": {"fill": fv("Named Point Color")}, "selector": WILD}]  # the disc under the letter (a11y_check reads the letter against it)
    oL["categoryLabels"] = [{"properties": {"show": b(True), "fontFamily": text(DISPLAY), "fontSize": num(S), "color": color(SURFACE), "bold": b(True)}}]
    v.append(decorative(place(f"{slot}_letters", "scatterChart", x, y, w, h, z + 3, 0, query=qL, objects=oL,
                              filters=[filter_in("Package", "Preset", ["A", "B", "C"], "flt_letters")], vcos=vco(padding=0)), deco_base + 2))
    v.append(decorative(you_label(slot, z + 3), deco_base + 3))
    o3 = quiet(copy.deepcopy(o_cloud))
    o3["markers"] = [{"properties": {"transparency": num(100), "borderShow": b(False)}}]
    hv = vco(padding=0)
    hv["visualTooltip"] = [{"properties": {"show": b(True), "type": enum("Canvas"), "section": text(TT)}}]
    v.append(decorative(place(f"{slot}_hover", "scatterChart", x, y, w, h, z + 4, 0, query=q_cloud, objects=o3, vcos=hv), deco_base))
    return v


HORIZON = lambda: filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon")  # noqa: E731


def nums_card(name, measures, labels_, alt_measure, size=21):
    v = card(name, *at(P2, name), measures, DISPLAY, size, INK, BODY, S, INK2, labels=labels_)
    return bind_alt(v, alt_measure)


MIX_A = "Booking app with member rates + Revenue management + Kiosks at the 20 busiest hotels"  # R-P2-6: static, A's composition never changes
LEDGER_COLS = (112, 280, 88, 96, 176)  # the spec's construction.tables.tbl_ledger (doc 22 section 3)
# Row padding 0.5: a 12 pt line is 21.28 px and a ruled row carries 1 px for its rule (measured on the tile render of step
# 6: 46.0 px for a two-line row at padding 1.2), so a two-line row is 44.6 px (the comp's 45) and the three-line row 65.8
# (64): the four row tops stay within 1 px of the comp's. The native header is 34 px at this padding (the comp's 28; step 5,
# "Found" 5), so the table starts LEDGER_LIFT px above its slot and the rows sit where the comp has them; the slot's bottom
# edge stays. The visual is 2 px wider than its columns (step 2, S-2 point 4: at exactly the column sum Desktop shows a
# scrollbar), and starts 1 px left of the slot: a native cell pads 7.7 px on the left, the comp 5.
LEDGER_PAD, LEDGER_LIFT, LEDGER_SLACK, LEDGER_DX = 0.5, 6, 2, -1


def rec_head():
    """The decision card's head (doc 21 6.2): a text box with two paragraphs, the recommendation in 20 px semibold and the
    mix line in Night. The words are typed (TEXT_STATIC); a screen reader gets them from the model (Alt Rec Head (text)),
    because a11y_check allows no typed number in a static alt text."""
    x, y, w, h, z, tab = at(P2, "c_rec_head")
    v = textbox("c_rec_head", x, y, w, h, z, tab, [[("Our recommendation: package A", DISPLAY, 20, INK, False)], [(MIX_A, BODY, SPX, INK, False)]])
    return bind_alt(v, "Alt Rec Head (text)")


def rec_nums():
    """Four callouts in one card (doc 21 6.2): capex, NPV through 2032, a year by 2032, a year on cost; the value in 21 pt
    semibold (the comp's 28 px), the label under it in Dusk. The two signed numbers take their ink from the model: Burnt
    Tangerine below zero (the comp's .neg), Night otherwise; the sign says it too."""
    ms = ["Rec Capex (text)", "Rec NPV (text)", "Rec Run-rate (text)", "Rec A Year on Cost (text)"]
    v = nums_card("c_rec_nums", ms, ["capex", "NPV through 2032", "a year by 2032", "a year on cost"], "Alt Rec Nums (text)")
    v["visual"]["objects"]["value"] += [{"properties": {"fontColor": fv(ink)}, "selector": {"metadata": mref(m_)}}
                                        for m_, ink in ((ms[1], "Rec NPV Ink"), (ms[2], "Rec Run-rate Ink"))]
    v["position"]["y"] -= 4  # the card centres value and label in its 64 px; the comp sets them from the top (tile render: 4.5 px low)
    return v


def rec_lines():
    """The two lines under the numbers. A card value never breaks a line (spike S-7), so each line is its own card, the
    second 21 px under the first (the comp's 21.3 px pitch); each card centres its line, so the pair sits where the comp
    sets the two lines from the top of the slot (note()). One tab stop: the first card reads both lines."""
    x, y, w, h, z, tab = at(P2, "c_rec_lines")
    top = round(y + 21.3 / 2 - 0.7 - CARD_H[1] / 2)
    out = []
    for i, measure in enumerate(("Rec Line 1 (text)", "Rec Line 2 (text)")):
        v = card("c_rec_lines" if i == 0 else "c_rec_lines_2", x, top + 21 * i, w, CARD_H[1], z, tab, [measure], BODY, S, INK, off_grid=True)
        out.append(bind_alt(v, "Rec Lines (text)") if i == 0 else decorative(v, 30))
    return out


def ledger():
    """The 2032 ledger (R-P2-5, doc 21 6.2 with the v10 columns): a native table on the Finding table, its four text measures
    switching on the finding. 'What we track' carries a line break (UNICHAR(10), spike S-7) and wraps; it is set in Dusk.
    The header in Dusk with a 1 px Dusk rule under it, the rows ruled in Seam, no outline. The rows come in the model's
    order (Finding[Label] is sorted by Ledger Sort), so the visual carries no sort and no arrow."""
    ms = ("Ledger Measure (text)", "Ledger 2025 (text)", "Ledger 2032 (text)", "Ledger Status (text)")
    proj = [proj_col("Finding", "Label", display="Finding"), proj_mea(ms[0], "What we track"), proj_mea(ms[1], "2025"), proj_mea(ms[2], "2032 with A"), proj_mea(ms[3], "Status")]
    colfmt = [{"properties": {"fontColor": color(INK2), "styleHeader": b(False), "styleValues": b(True)}, "selector": {"metadata": mref(ms[0])}}]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=LEDGER_PAD, header_size=S, column_formatting=colfmt)
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    objs["values"][0]["properties"]["wordWrap"] = b(True)
    objs["columnWidth"] = [{"properties": {"value": num(w_)}, "selector": {"metadata": q_}}
                           for q_, w_ in zip(("Finding.Label", *[mref(m_) for m_ in ms]), LEDGER_COLS)]
    x, y, w, h, z, tab = at(P2, "tbl_ledger")
    t = visual("tbl_ledger", "tableEx", x + LEDGER_DX, y - LEDGER_LIFT, w + LEDGER_SLACK, h + LEDGER_LIFT, z, tab, query={"Values": {"projections": proj}}, objects=objs,
               vcos=vco(padding=0), off_grid=True)
    return bind_alt(t, "Alt Ledger (text)")


def p2_frame():
    """FinalV3 build step 6 (doc 23): the frame every state of page 2 shares, as the comp rebuild-comp-v10.html (#rec) draws
    it; slots from the v10 slot map, construction from doc 21 section 5 and P-2. The eyebrow and the logo come from
    brand_row(), the five cards from card_frames()."""
    v = [ctl_button(P2, "btn_back", "← The Brand Review", "night_off", ("PageNavigation", P1), "Back to The Brand Review, page 1"),
         headline(P2, "z_headline2", "Headline P2 (text)"),
         note(P2, "c_subtitle2", "Subtitle P2 (text)", 2, colour=ZONE_MUTED)]
    v += tab_bar()
    # the label beside the scenario pills is in the slicer's alt text, so it leaves the tab order (plan 11); the comp sets
    # it 5 px under the top of its slot, on the pills' text line
    lab = tb(P2, "lbl_scenario", "Scenario", size=SPX, colour=ZONE_MUTED)
    lab["visual"]["visualContainerObjects"]["padding"] = [{"properties": {"top": num(5), "bottom": num(0), "left": num(0), "right": num(0)}}]
    v.append(decorative(lab, 3))
    v.append(button_slicer("sl_scenario", "Scenario", "Scenario", "Expected", "Scenario: Low, Expected or High; every number on this page follows it", 3, night=True))
    # the footer row: the source line with the three valuation parameters from the model (R-P2-12) and the Definitions chip (P-7)
    v.append(note(P2, "z_footer2", "Footer P2 (text)", 1))
    v.append(chip_native(P2, "chip_def2", "Chip Definitions (text)", TT_GLOSS, "Alt Definitions (text)"))
    return v


def p2_decision_card():
    """FinalV3 build step 6: the decision card of the Recommended state (doc 21 6.2, slots of doc 22 section 2). No tile,
    no glow: the card is the tile (R-P2-6). Reading order: head, numbers, lines, ledger, caption, invitation (R-P2-9)."""
    v = [decorative(image_measure(P2, "img_rec_chip", "Chip Funded", None), 5), rec_head(), rec_nums()]
    v += rec_lines()
    v.append(ledger())
    v.append(tb(P2, "c_ledger_caption", "2025 brand plus A's full yearly effect, in 2025 dollars."))
    v.append(ctl_button(P2, "btn_build_invite", "Think you can beat A? Build your own →", "light_sec", ("Bookmark", "bm_p2_build"),
                        "Think you can beat A Build your own: show the state where you pick moves and compare your plan with A"))
    return v


# ---------------------------------------------------------------------- FinalV3 build step 7: the hero table and the capital plan
# The hero table as spike S-2 found it (doc 23, log of step 2; doc 21 6.1): the comp's columns with the three corrections a
# native table needs (an image column is its image + 11 px, "−$27.3M" needs 74 px, 2 px of slack against a scrollbar). The
# geometry lives in sketch_model.py, beside bar_cell(), so the bars, the reference lines and their two labels cannot drift.
HERO_SLACK = 2
# Measured in build step 7 on a scratch page that shows the table whole (a tile seam through a table is no reference: at a
# fractional zoom Desktop snaps a table by up to 1.6 page px): header 32.5 px plus its 1 px rule, ten rows of 34.0 px, 373 px
# in all, so at the slot's 372 the table showed both scrollbars. A cell's text is set from the top of its row: its cap
# centre is 12.25 px under the row's top (header: 12.05), where the comp centres it at 17.5 (header: 16.5). So the table
# starts HERO_DY px under its slot and the bars sit sm.HERO_TEXT_LIFT px higher in their cells: row text, header text and
# bars land within 1.3 px of the comp's. The price is the header rule and the two reference lines, 4.5 px under the comp's.
HERO_DY, HERO_DH = 4, 2
# R-P2-3 caption, as approved (rebuild-v10-spec.json). Open question 3 of doc 23: its second sentence is not true in the data.
HERO_CAPTION = "A year on cost = what a move adds to operating profit in 2032 ÷ what it costs. Late moves are still ramping up in 2032."
ZW = "​"  # the header of a value column: the comp leaves it empty, a table column needs a name (one and two zero-width spaces)


def hero_table():
    """tbl_hero (R-P2-3, P-4): the ten moves in the model's order (Move Name is sorted by Hero Sort: the Expected 'a year on
    cost', fixed at refresh), each with the finding it answers, its status as a word, and two bar cells with their values
    beside them. Row padding 0 and an image as high as the row, so each reference line runs unbroken down the ten rows.
    Status and NPV take their ink from the model (P-6: the word first, the colour second). No tooltip page."""
    ms = ("Move Answers (text)", "Move Status (text)", "Hero Yield Bar SVG", "Move Yield (text)", "Hero NPV Bar SVG", "Move NPV (text)")
    proj = [proj_col("InvestmentProjects", "Move Name", display="Move"), proj_mea(ms[0], "Answers"), proj_mea(ms[1], "Status"),
            proj_mea(ms[2], "A year on cost"), proj_mea(ms[3], ZW), proj_mea(ms[4], "NPV through 2032"), proj_mea(ms[5], ZW * 2)]
    refs = ["InvestmentProjects.Move Name", *[mref(m_) for m_ in ms]]
    colfmt = [{"properties": {"fontColor": color(INK2), "styleHeader": b(False), "styleValues": b(True)}, "selector": {"metadata": refs[1]}},
              *[{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": refs[i]}} for i in (4, 6)]]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=0, header_size=S, column_formatting=colfmt)
    objs["grid"][0]["properties"].update({"gridHorizontal": b(False), "imageHeight": num(sm.HERO_ROW_H), "imageWidth": num(sm.HERO_IMG_W)})
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    objs["values"][0]["properties"].update({"wordWrap": b(False), "urlIcon": b(False)})
    objs["values"] += [{"properties": {"fontColor": fv(ink)}, "selector": {**WILD, "metadata": refs[i]}} for i, ink in ((2, "Move Status Ink"), (6, "Move NPV Ink"))]
    objs["columnWidth"] = [{"properties": {"value": num(w_)}, "selector": {"metadata": q_}} for q_, w_ in zip(refs, sm.HERO_COLS)]
    x, y, w, h, z, tab = at(P2, "tbl_hero")
    t = visual("tbl_hero", "tableEx", x, y + HERO_DY, sum(sm.HERO_COLS) + HERO_SLACK, h + HERO_DH, z, tab, query={"Values": {"projections": proj}}, objects=objs,
               vcos=vco(padding=0), off_grid=True)
    return bind_alt(t, "Alt Hero (text)")


def p2_hero():
    """The hero card of Recommended (doc 21 6.1, slots of doc 22 section 2): the title that follows the scenario, the two
    reference labels at the x of their lines, the table, the caption."""
    x8, x0 = sm.hero_ref_x()
    s8, s0 = SLOT[P2]["lbl_hero_8"], SLOT[P2]["lbl_hero_0"]
    # the slot map carries the comp's computed x; the generator's own constants must give the same pixels
    assert s8["x"] == round(x8) and s0["x"] + s0["w"] == round(x0), (x8, x0, s8, s0)
    lab8 = textbox("lbl_hero_8", *at(P2, "lbl_hero_8"), [[("8%: our cost of money", BODY, SPX, INK2, False)]], off_grid=True)
    lab0 = textbox("lbl_hero_0", *at(P2, "lbl_hero_0"), [[("pays back by 2032 →", BODY, SPX, INK2, False)]], align="right", off_grid=True)
    return [title(P2, "c_hero_title", "Hero Title (text)", lift=5), decorative(lab8, 40), decorative(lab0, 41), hero_table(),
            tb(P2, "c_hero_caption", HERO_CAPTION)]


def line_cards(page, name, measures, alt_measure, deco, colour=INK):
    """A text block with fixed line breaks: a card value never breaks a line (spike S-7), so each line is its own card at the
    comp's 21.3 px pitch, set from the top of the slot (rec_lines() of step 6). One tab stop: the first card reads them all."""
    x, y, w, h, z, tab = at(page, name)
    top = round(y + 21.3 / 2 - 0.7 - CARD_H[1] / 2)
    out = []
    for i, measure in enumerate(measures):
        v = card(name if i == 0 else f"{name}_{i + 1}", x, top + round(21.3 * i), w, CARD_H[1], z, tab, [measure], BODY, S, colour, off_grid=True)
        out.append(bind_alt(v, alt_measure) if i == 0 else decorative(v, deco + i))
    return out


PLAN_FILL = (ACCENT_MARK, INK, "#717B8B", SLATE)  # tranche 1, tranche 2, tranche 3 (Night at 60 % on white), not needed (spec ch_plan_bar)
PLAN_LINES = {1: 2, 2: 3, 3: 3, 4: 1}             # lines of each segment's label (TEXT_SLOTS)
# the visual rects that put Power BI's plot on the comp's (PLOT_RECT of step 5), measured on the tile render of step 7.
# The bar: in its 32 px slot Power BI drew a 22.3 px bar, 8.2 px under the visual's top.
# (at 42 px high it drew 32.6 px, 9.7 px under the top). The line chart: in its slot (792, 828, 1072, 148) the plot ran
# x 864.2 to 1851.4 and y 841.9 (+$20M) to 946.0 (-$10M); the comp's runs 864 to 1856 and 846 to 948.
PLAN_RECT = {"ch_plan_bar": (56, 780, 1808, 40), "ch_plan_cum": (792, 834, 1077, 146)}
PLAN_X_END = 2032.8                 # spec ch_plan_cum.x_axis_end: room for the end labels inside the plot, no 2033 tick
PLAN_Y = (-10_000_000, 20_000_000)  # spec ch_plan_cum.y: −10 to +20 $M, ticks at −10, 0, +10, +20
# doc 22 section 3 asks for Right; a line chart knows Above and Under only (the catalog, the theme schema and Microsoft's
# validator agree). Low ends under the zero line, so its label goes under the line; Expected and High go above theirs.
PLAN_LABEL_POS = ("Under", "Above", "Above")
GATE_LINES = 4                      # lines of the gate rule at 12 pt in 704 px (the comp)


def plan_bar():
    """ch_plan_bar (R-P2-7, doc 21 6.3 with doc 22 section 3): one stacked bar of four measures, the budget from left to
    right, no axes, no legend and no data labels (the four cards above print the amounts). The value axis ends at the
    budget, so each segment starts under its card."""
    ms = ["Tranche 1 Capex", "Tranche 2 Capex", "Tranche 3 Capex", "Not Needed Capex"]
    # a bar chart needs a category: the brand, one value under the page's brand filter, so one bar
    q = {"Category": {"projections": [proj_col("Brands", "Brand", active=True)]},
         "Y": {"projections": [proj_mea(ms[0], "Tranche 1"), proj_mea(ms[1], "Tranche 2"), proj_mea(ms[2], "Tranche 3"), proj_mea(ms[3], "Not needed")]}}
    va = axis(BODY, S, INK2, show=False, gridlines=False, start=0)
    va[0]["properties"]["end"] = mtext("Move Budget (num)")
    ca = axis(BODY, S, INK2, show=False)
    ca[0]["properties"].update({"innerPadding": integer(0), "outerPadding": integer(0)})
    objs = {"categoryAxis": ca, "valueAxis": va, "legend": legend(False), "labels": [{"properties": {"show": b(False)}}],
            "layout": [{"properties": {"stackedGapSize": num(0)}}],  # no white seam between the segments (the comp draws none)
            "dataPoint": series_colors(dict(zip([mref(m_) for m_ in ms], PLAN_FILL)))}
    v = chart(P2, "ch_plan_bar", "barChart", q, objs, None, alt_measure="Alt Plan Bar (text)")
    return plot_rect(v, PLAN_RECT["ch_plan_bar"]) if "ch_plan_bar" in PLAN_RECT else v


def plan_cum():
    """ch_plan_cum (R-P2-7, doc 21 6.3 and P-5 as doc 22 section 3 amends them): package A's cumulative net impact in the
    three cases. The case in view is the 3 px Coffee Blue line; the other two are 1.5 px Warm Grey, Low dashed and High
    dotted (A Cumulative Line (...) is blank for the case in view). One data label per line on the last year: the name and
    the value from the label-safe format string, on white; the case in view in Deep Coffee semibold (one end series per
    case for it, because a series has one label position: PLAN_LABEL_POS). The end series come
    after the lines and the first line is formatted in whole $M, so the value axis prints "+$10M" in any locale (P-1 b).
    Zero line named (R-G2), the gate as a dashed line at mid-2028; a year opens the year tooltip."""
    sel = "Preset A Cumulative Net (sel)"
    thin = [(f"A Cumulative Line ({c})", f"{c} case") for c in ("Low", "Expected", "High")]
    ends = [(f"A Cumulative End {c} (label-safe)", f"{c} case, last year") for c in ("Low", "Expected", "High")]
    ends_sel = [(f"A Cumulative End Sel {c} (label-safe)", f"{c} case in view, last year") for c in ("Low", "Expected", "High")]
    series = thin + [(sel, "The case in view")] + ends + ends_sel
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea(m_, d_) for m_, d_ in series]}}
    ls = line_styles({**{mref(m_): 1.5 for m_, _ in thin}, mref(sel): 3}, dashed=(mref(thin[0][0]),))
    next(e for e in ls if e.get("selector", {}).get("metadata") == mref(thin[2][0]))["properties"]["lineStyle"] = enum("dotted")
    ls += [{"properties": {"strokeShow": b(False), "showMarker": b(False)}, "selector": {"metadata": mref(m_)}} for m_, _ in ends + ends_sel]
    lab = {"fontFamily": text(BODY), "fontSize": num(S), "color": color(INK2), "labelDisplayUnits": integer(1),
           "enableBackground": b(True)}  # white and opaque from the theme (compile_theme.py, lineChart labels)
    years = HORIZON()["filter"]["Where"][0]["Condition"]["In"]["Values"]
    first_year = int(years[0][0]["Literal"]["Value"].rstrip("L"))
    objs = {"categoryAxis": axis(BODY, S, INK2, start=first_year, end=PLAN_X_END, extra={"labelPrecision": integer(0)}),
            "valueAxis": axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, units=1, start=PLAN_Y[0], end=PLAN_Y[1]),
            "legend": legend(False), "seriesLabels": [{"properties": {"show": b(False)}}],
            "labels": [{"properties": {"show": b(True), **lab}},
                       *[{"properties": {"showSeries": b(False)}, "selector": {"metadata": mref(m_)}} for m_, _ in thin + [(sel, "")]],
                       *[{"properties": {"showSeries": b(True), "labelPosition": enum(pos)}, "selector": {"metadata": mref(m_)}} for (m_, _), pos in zip(ends, PLAN_LABEL_POS)],
                       *[{"properties": {"showSeries": b(True), "labelPosition": enum(pos), "color": color(ACCENT), "fontFamily": text(DISPLAY)},
                          "selector": {"metadata": mref(m_)}} for (m_, _), pos in zip(ends_sel, PLAN_LABEL_POS)]],
            "dataPoint": series_colors({**{mref(m_): SLATE for m_, _ in thin + ends}, mref(sel): ACCENT_MARK, **{mref(m_): ACCENT_MARK for m_, _ in ends_sel}}),
            "lineStyles": ls,
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("back"), "displayName": text("Cash positive above this line"), "dataLabelShow": b(True),
                                                    "dataLabelText": enum("Name"), "dataLabelColor": color(INK2), "dataLabelHorizontalPosition": enum("left"),
                                                    "dataLabelVerticalPosition": enum("above")}, "selector": {"id": "1"}}],
            "xAxisReferenceLine": [{"properties": {"show": b(True), "value": num(sm.GATE_YEAR + 0.5), "lineColor": color(INK), "transparency": num(0), "width": num(1),
                                                   "style": enum("dashed"), "position": enum("back"), "displayName": text(f"The {sm.GATE_YEAR} gate"), "dataLabelShow": b(True),
                                                   "dataLabelText": enum("Name"), "dataLabelColor": color(INK), "dataLabelHorizontalPosition": enum("right"),
                                                   "dataLabelVerticalPosition": enum("above")}, "selector": {"id": "1"}}]}
    v = chart(P2, "ch_plan_cum", "lineChart", q, objs, None, filters=[HORIZON()], alt_measure="Alt Plan Cum (text)", tooltip_page=TT_YEAR)
    return plot_rect(v, PLAN_RECT["ch_plan_cum"]) if "ch_plan_cum" in PLAN_RECT else v


def p2_capital_plan():
    """The capital plan in the bottom card of Recommended (doc 21 6.3, N-5; slots of doc 22 section 2): title, hover tag,
    the four segment labels above their segments, the plan bar, the gate rule, A's cumulative chart and the milestone
    line. Reading order: title, segments left to right, bar, gate, chart, milestones (R-P2-9)."""
    v = [title(P2, "c_plan_title", "Capital Plan Title (text)", lift=5), hover_tag_text(P2, "tag_plan_cum", "Hover a year", 22)]
    for k, n in PLAN_LINES.items():
        v += line_cards(P2, f"c_plan_t{k}", [f"Plan T{k} L{i} (text)" for i in range(1, n + 1)], f"Plan T{k} (text)", 50 + 10 * k)
    v.append(plan_bar())
    gate = note(P2, "c_plan_gate", "Gate Rule (text)", GATE_LINES, colour=INK)
    gate["position"]["y"] += 2  # the four lines sat 1.8 px above the comp's on the tile render
    v.append(gate)
    v.append(plan_cum())
    v.append(note(P2, "c_plan_milestones", "Milestones (text)", 1))
    return v


# ---------------------------------------------------------------------- FinalV3 build step 8: What waits, and why
PROOF_TITLE_DY = 0  # as measured on the strip render of step 8: the two lines land within 1 px of the comp's
TITLE2_H = 72  # a card that shows two 14 pt lines; it centres them, the comp sets them from the top of the slot (24.9 px a line)


def p2_proof():
    """The proof chart's card, shared by What waits and Build (doc 21 7.1, R-W-1): the two-line title that counts the
    packages, the hover tag, the subtitle that follows the scenario, and the scatter stack."""
    t = dyn(P2, "c_scatter_title_s", "Proof Title (text)", size=TITLE_PT, colour=INK, font=DISPLAY)
    t["position"]["height"] = TITLE2_H
    t["position"]["y"] = round(SLOT[P2]["c_scatter_title_s"]["y"] + 24.9 - TITLE2_H / 2) + PROOF_TITLE_DY
    sub = note(P2, "c_scatter_sub", "Proof Subtitle (text)", 1)
    return [t, hover_tag_text(P2, "tag_scatter_s", "Hover a dot", 21), sub] + scatter_stack("hero_s_packages", 6)


WAITS_COLS = (168, 224, 216, 256, 208)  # the spec's construction.tables.tbl_waits (doc 22 section 3)
# The table rules of build step 6 ("Found", 2): every cell at the top of its row, as the comp sets them here (.pbi.wrap); a
# ruled row is its lines x 21.28 px plus twice the padding plus 1 px for the rule, the comp's is lines x 21.28 + 12, so the
# padding is 5.5. The native header grows with the padding (32.6 px + twice the padding, the comp's is 32), so the table
# starts WAITS_LIFT px above its slot and the first row's rule stays on the comp's line. 2 px wider than its columns (S-2
# point 4) and 1 px left of the slot (a native cell pads 7.7 px on the left, the comp 5), as the ledger.
WAITS_PAD, WAITS_LIFT, WAITS_SLACK, WAITS_DX = 4.9, 10, 2, -1
WAITS_HEAD = ("What waits, and why", "One alternative and two tranches, each weighed against A.")


def waits_head():
    """The panel's head (doc 21 7.2): a text box with two paragraphs, the title in 20 px semibold Night and the intro in Dusk."""
    x, y, w, h, z, tab = at(P2, "c_waits_head")
    return textbox("c_waits_head", x, y, w, h, z, tab, [[(WAITS_HEAD[0], DISPLAY, 20, INK, False)], [(WAITS_HEAD[1], BODY, SPX, INK2, False)]],
                   alt=WAITS_HEAD[0] + ". " + WAITS_HEAD[1])


def waits_table():
    """tbl_waits (R-W-2, N-3; doc 21 7.2 with the v10 columns): a native table on WaitOption, three rows, its four text
    measures switching on the option. Word wrap on; 'The numbers' and 'When we decide' carry their line breaks
    (UNICHAR(10), spike S-7). The header in Dusk with a 1 px Dusk rule under it, the rows ruled in Seam, no outline. The
    rows come in the model's order (WaitOption[Title] is sorted by Sort), so the visual carries no sort and no arrow."""
    ms = ("Wait Numbers (text)", "Wait Why (text)", "Wait WhyNot (text)", "Wait When (text)")
    proj = [proj_col("WaitOption", "Title", display="Option"), proj_mea(ms[0], "The numbers"), proj_mea(ms[1], "Why it's on the table"),
            proj_mea(ms[2], "Why not now"), proj_mea(ms[3], "When we decide")]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=WAITS_PAD, header_size=S)
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    # the rule under the last row (the comp rules every row): a native table rules between rows only, so the values area gets a bottom outline in Seam
    objs["values"][0]["properties"].update({"wordWrap": b(True), "outlineStyle": enum("BottomOnly"), "outlineColor": color(HAIR), "outlineWeight": num(1)})
    objs["columnWidth"] = [{"properties": {"value": num(w_)}, "selector": {"metadata": q_}}
                           for q_, w_ in zip(("WaitOption.Title", *[mref(m_) for m_ in ms]), WAITS_COLS)]
    x, y, w, h, z, tab = at(P2, "tbl_waits")
    t = visual("tbl_waits", "tableEx", x + WAITS_DX, y - WAITS_LIFT, w + WAITS_SLACK, h + WAITS_LIFT, z, tab, query={"Values": {"projections": proj}}, objects=objs,
               vcos=vco(padding=0), off_grid=True)
    return bind_alt(t, "Alt Waits (text)")


CMP_X_END = 2032.6  # spec ch_cmp_alts.x_axis_end: room for the end labels inside the plot, no 2033 tick
# the visual rect that puts Power BI's plot on the comp's (PLOT_RECT of step 5), measured in build step 8: the comp draws
# the plot at x 128 to 1856 and y 731 to 972 of the page (under a 29 px title row in the slot 56, 688, 1808, 312)
CMP_RECT = {"ch_cmp_alts": (56, 685, 1819, 316), "ch_cmp_build": (56, 685, 1819, 316)}
# the comp leaves 14 px between its title row and the top tick; Power BI starts the plot 3 px higher. The container's
# "space below title" moves the plot 1 px per unit (default 2; measured at 5 and 8 in step 8), the title stays. The visual
# starts 3 px above its slot: Power BI sets the title 2.6 px lower in its row than the comp does.
CMP_SPACE = 8


def cmp_chart(name, lines, title_measure, alt_measure, y_prefix):
    """A comparison chart (R-W-3, R-B; doc 21 7.3 and P-5 as doc 22 section 3 amends them): cumulative net impact by year,
    the title inside the visual, no legend. lines, in drawing order (the last on top): (line measure, display name, colour,
    width, dashed, end-label measure or None, label position, emphasised: True = Deep Coffee semibold, a colour = that
    colour semibold, False = Dusk). One data label per labelled line on the last year: the name and
    the value from the label-safe format string, on white (the theme), above or under its line end so that two lines that
    end together cannot put their labels on each other. The first line measure is formatted in whole $M and the end series
    come after the lines, so the value axis prints "+$10M" in any locale (P-1 b). The value axis ends on the model's
    whole steps ([<y_prefix> Y Start / End]): one tick below zero and 8 % of headroom above the top line. The zero line is
    named (R-G2); a year opens the year tooltip."""
    ends = [l_ for l_ in lines if l_[5]]
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]},
         "Y": {"projections": [proj_mea(l_[0], l_[1]) for l_ in lines] + [proj_mea(l_[5], f"{l_[1]}, last year") for l_ in ends]}}
    ls = line_styles({mref(l_[0]): l_[3] for l_ in lines}, dashed=tuple(mref(l_[0]) for l_ in lines if l_[4]))
    ls += [{"properties": {"strokeShow": b(False), "showMarker": b(False)}, "selector": {"metadata": mref(l_[5])}} for l_ in ends]
    lab = {"fontFamily": text(BODY), "fontSize": num(S), "color": color(INK2), "labelDisplayUnits": integer(1),
           "enableBackground": b(True)}  # white and opaque from the theme (compile_theme.py, lineChart labels)
    years = HORIZON()["filter"]["Where"][0]["Condition"]["In"]["Values"]
    first_year = int(years[0][0]["Literal"]["Value"].rstrip("L"))
    va = axis(BODY, S, INK2, gridlines=True, grid_color=HAIR, units=1)
    va[0]["properties"].update({"start": mtext(f"{y_prefix} Y Start"), "end": mtext(f"{y_prefix} Y End")})
    objs = {"categoryAxis": axis(BODY, S, INK2, start=first_year, end=CMP_X_END, extra={"labelPrecision": integer(0)}),
            "valueAxis": va, "legend": legend(False), "seriesLabels": [{"properties": {"show": b(False)}}],
            "labels": [{"properties": {"show": b(True), **lab}},
                       *[{"properties": {"showSeries": b(False)}, "selector": {"metadata": mref(l_[0])}} for l_ in lines],
                       *[{"properties": {"showSeries": b(True), "labelPosition": enum(l_[6]),
                                         **({"color": color(ACCENT if l_[7] is True else l_[7]), "fontFamily": text(DISPLAY)} if l_[7] else {})},
                          "selector": {"metadata": mref(l_[5])}} for l_ in ends]],
            "dataPoint": series_colors({**{mref(l_[0]): l_[2] for l_ in lines}, **{mref(l_[5]): l_[2] for l_ in ends}}),
            "lineStyles": ls,
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(INK2), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("back"), "displayName": text("Cash positive above this line"), "dataLabelShow": b(True),
                                                    "dataLabelText": enum("Name"), "dataLabelColor": color(INK2), "dataLabelHorizontalPosition": enum("left"),
                                                    "dataLabelVerticalPosition": enum("above")}, "selector": {"id": "1"}}]}
    v = chart(P2, name, "lineChart", q, objs, None, title_measure=title_measure, filters=[HORIZON()], alt_measure=alt_measure, tooltip_page=TT_YEAR)
    if name in CMP_RECT:
        plot_rect(v, CMP_RECT[name])
    if CMP_SPACE is not None:
        v["visual"]["visualContainerObjects"]["spacing"] = [{"properties": {"customizeSpacing": b(True), "spaceBelowTitle": num(CMP_SPACE)}}]
    return v


def p2_waits():
    """FinalV3 build step 8: the What-waits state (doc 21 section 7): the panel's head and the table of the three options,
    and the comparison of A, B and C in the bottom card with its hover tag. Reading order: head, table, chart (R-P2-9).
    C first (Warm Grey, dashed), then B (Night), then A on top (Coffee Blue, 3 px), as the comp draws them."""
    lines = [("Preset C Cumulative Line", "C", SLATE, 2, True, "Preset C Cumulative End (label-safe)", "Under", False),
             ("Preset B Cumulative Net (sel)", "B", INK, 2, False, "Preset B Cumulative End (label-safe)", "Under", False),
             ("Preset A Cumulative Net (sel)", "A, our recommendation", ACCENT_MARK, 3, False, "Preset A Cumulative End (label-safe)", "Above", True)]
    return [waits_head(), waits_table(), cmp_chart("ch_cmp_alts", lines, "Cmp Alts Title (text)", "Alt Cmp Alts (text)", "Cmp Alts"),
            hover_tag_text(P2, "tag_cmp_alts", "Hover a year", 23)]


# ---------------------------------------------------------------------- FinalV3 build step 9: Build your own
BUILD_HEAD = ("Build your own", "Click a move to add or remove it.")
# The saved selection of the move selector: package A's three moves, so the state opens on A and "your plan" equals it
# (doc 21 section 8). Short names, as BuildMove[Short Name] prints them on the tiles.
A_MOVES = ("Booking app", "Revenue management", "Kiosks at 20 desks")
SELECTOR_ALT = "Moves: pick a move to add it to your plan or to take it out; the table beside it gives each move's numbers"


def build_head():
    """The panel's head (doc 21 section 8): a text box with two paragraphs, as the head of What waits."""
    x, y, w, h, z, tab = at(P2, "c_build_head")
    return textbox("c_build_head", x, y, w, h, z, tab, [[(BUILD_HEAD[0], DISPLAY, 20, INK, False)], [(BUILD_HEAD[1], BODY, SPX, INK2, False)]],
                   alt=BUILD_HEAD[0] + ". " + BUILD_HEAD[1])


def move_slicer():
    """sl_moves (R-B-1, N-1; spike S-3 of step 2): the native selector, a button slicer of ten square tiles in one column
    on BuildMove[Short Name], multi-select, the selection icon on (a Night box with a check), no outline; a tile turns Seam
    on hover and stays white when picked (the box says it). Each tile is 32 px with a 1 px Seam rule at its foot (the accent
    bar), the pitch of the rows of tbl_moves beside it. The saved selection is package A. Every tile is a button with a
    toggle state: Tab moves between tiles, Space picks (S-3)."""
    x, y, w, h, z, tab = at(P2, "sl_moves")
    st = lambda i: {"id": i}  # noqa: E731
    states = ("default", "interaction:hover", "interaction:press", "selection:selected")
    objs = {
        "shapeCustomRectangle": [{"properties": {"tileShape": enum("rectangle")}, "selector": st("default")}],
        "layout": [{"properties": {"rowCount": integer(len(MOVES_ROWS)), "columnCount": integer(1), "maxTiles": integer(len(MOVES_ROWS)), "cellPadding": integer(0)}}],
        "fillCustom": [{"properties": {"show": b(True), "fillColor": color(SURFACE), "transparency": num(0)}, "selector": st("default")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:hover")},
                       {"properties": {"fillColor": color(HAIR)}, "selector": st("interaction:press")},
                       {"properties": {"fillColor": color(SURFACE)}, "selector": st("selection:selected")}],
        "outline": [{"properties": {"show": b(False)}, "selector": st("default")}],
        "accentBar": [{"properties": {"show": b(True), "position": enum("Bottom"), "color": color(HAIR), "transparency": num(0), "width": num(1)}, "selector": st(i_)} for i_ in states],
        "value": [{"properties": {"show": b(True), "fontFamily": text(BODY), "fontSize": num(S), "fontColor": color(INK), "bold": b(False),
                                  "horizontalAlignment": text("left"), "verticalAlignment": text("middle")}, "selector": st("default")},
                  *[{"properties": {"fontColor": color(INK), "bold": b(False)}, "selector": st(i_)} for i_ in states[1:]]],
        "label": [{"properties": {"show": b(False)}, "selector": st("default")}],
        "padding": [{"properties": {"paddingSelection": text("Custom"), "topMargin": integer(0), "bottomMargin": integer(SEL_LIFT), "leftMargin": integer(SEL_LEFT), "rightMargin": integer(8)},
                     "selector": st("default")}],
        # without the colour on the selected state the checked box is white on white (S-3)
        "selectionIcon": [{"properties": {"show": b(True), "position": enum("Left"), "size": integer(16), "spacing": integer(8), "color": color(INK)}, "selector": st("default")},
                          {"properties": {"color": color(INK)}, "selector": st("selection:selected")}],
        "selection": [{"properties": {"singleSelect": b(False), "strictSingleSelect": b(False), "selectAllCheckboxEnabled": b(False)}}],
        "general": [{"properties": {"filter": {"filter": {
            "Version": 2, "From": [{"Name": "s", "Entity": "BuildMove", "Type": 0}],
            "Where": [{"Condition": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "s"}}, "Property": "Short Name"}}],
                                            "Values": [[{"Literal": {"Value": f"'{m_}'"}}] for m_ in A_MOVES]}}}]}}}}],
    }
    return visual("sl_moves", "advancedSlicerVisual", x, y, w, h, z, tab, query={"Values": {"projections": [proj_col("BuildMove", "Short Name", display="Move")]}},
                  objects=objs, vcos=vco(alt=SELECTOR_ALT, padding=0))


MOVES_ROWS = range(10)  # the ten Goodnight Inn moves (BuildMove)
# measured on the strip render of step 9: with the comp's 8 px at the left Power BI set box and name 2.5 to 3 px right of the
# comp's, and 1 to 2 px low in the tile
SEL_LEFT, SEL_LIFT = 5, 2
# tbl_moves as spike S-3 found it (doc 23, log of step 2; doc 21 section 8): the comp's columns 92 / 64 / 72 / 116 with the
# two corrections a native table needs ("−$27.3M" needs 74 px, the header "A year by 2032" 118) and 2 px of slack against a
# scrollbar. A ruled row of one 12 pt line is 21.28 px + twice the padding + 1 px for its rule (build step 6), so the
# padding is 4.86 for the selector's 32 px. The header takes the same padding and is about 42 px (the comp's 32), so the
# table starts MOVES_LIFT px above its slot and its first row begins at y 280, beside the first tile.
MOVES_COLS = (92, 64, 74, 118)
MOVES_PAD, MOVES_LIFT, MOVES_SLACK, MOVES_DX = 4.86, 10, 2, -2


def moves_table():
    """tbl_moves (R-B-1; doc 21 section 8): what each move answers, costs and returns, one row per tile of the selector and
    in its order (BuildMove[Short Name] is sorted by Sort). The selector does not filter it (interactions()), so all ten
    rows stay. The move's own name is the first column at width 0: a table needs a column of its row source, nothing shows
    (the names are on the tiles), and a screen reader reads the name with the row. Answers in Dusk; the NPV takes its ink
    from the model (Burnt Tangerine below zero, the sign says it too)."""
    ms = ("Move Answers (text)", "Move Capex (text)", "Move NPV (text)", "Move Run-rate (text)")
    proj = [proj_col("BuildMove", "Short Name", display="Move"), proj_mea(ms[0], "Answers"), proj_mea(ms[1], "Capex"), proj_mea(ms[2], "NPV"), proj_mea(ms[3], "A year by 2032")]
    refs = ["BuildMove.Short Name", *[mref(m_) for m_ in ms]]
    colfmt = [{"properties": {"fontColor": color(SURFACE), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": refs[0]}},
              {"properties": {"fontColor": color(INK2), "styleHeader": b(False), "styleValues": b(True)}, "selector": {"metadata": refs[1]}},
              *[{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": refs[i]}} for i in (2, 3, 4)]]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=MOVES_PAD, header_size=S, column_formatting=colfmt)
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    # the rule under the last row (the comp rules every row): a native table rules between rows only (build step 8)
    objs["values"][0]["properties"].update({"wordWrap": b(False), "outlineStyle": enum("BottomOnly"), "outlineColor": color(HAIR), "outlineWeight": num(1)})
    objs["values"] += [{"properties": {"fontColor": fv("Move NPV Ink")}, "selector": {**WILD, "metadata": refs[3]}}]
    objs["columnWidth"] = [{"properties": {"value": num(w_)}, "selector": {"metadata": q_}} for q_, w_ in zip(refs, (0, *MOVES_COLS))]
    x, y, w, h, z, tab = at(P2, "tbl_moves")
    t = visual("tbl_moves", "tableEx", x + MOVES_DX, y - MOVES_LIFT, sum(MOVES_COLS) + MOVES_SLACK, h + MOVES_LIFT + 2, z, tab, query={"Values": {"projections": proj}}, objects=objs,
               vcos=vco(padding=0), off_grid=True)
    return bind_alt(t, "Alt Moves (text)")


def you_title():
    """c_you_title (doc 21 section 8, the budget alarm of round 5): 18 pt semibold, set from the top of its 40 px slot (a
    card centres its line, so the plain title's card is 32 px high). Over the budget the title is the alarm: white on a
    Tangerine band that fills the slot, 12 px inside it. A card has one padding, so the band is a card of its own under
    the title: white and empty within the budget. One tab stop: the plain card reads the title in every state."""
    x, y, w, h, z, tab = at(P2, "c_you_title")
    plain = card("c_you_title", x, y, w, 32, z, tab, ["Build Title Plain (text)"], DISPLAY, 18, INK)
    alarm = card("c_you_title_alarm", x, y, w, h, z, tab, ["Build Title Alarm (text)"], DISPLAY, 18, SURFACE)
    alarm["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("Build Title Ink")
    vc = alarm["visual"]["visualContainerObjects"]
    vc["background"] = [{"properties": {"show": b(True), "color": fv("Build Title Fill"), "transparency": num(0)}}]
    vc["padding"] = [{"properties": {"top": num(0), "bottom": num(8), "left": num(12), "right": num(12)}}]
    return [decorative(alarm, 60), bind_alt(plain, "Build Title (text)")]


# c_you_nums (doc 22 section 2: 72 px high): four callouts in 464 px, 107 px each with 12 px between them (the comp's .nums).
# The value in 16 pt semibold on a 28.4 px line, the label under it in Dusk; "NPV through 2032" wraps to two lines. A card
# cannot hide its label while its value is empty, and the empty state shows nothing here (R-B-2), so each callout is a value
# card and a label card, both on measures that are empty while nothing is picked.
YOU_NUMS = (("Build Capex (text)", "Build Label Capex (text)", 1, None), ("Build NPV (text)", "Build Label NPV (text)", 2, "Build NPV Ink"),
            ("Build Run-rate (text)", "Build Label Run-rate (text)", 1, "Build Run-rate Ink"), ("Build A Year on Cost (text)", "Build Label A Year on Cost (text)", 1, None))
YOU_NUM_W, YOU_NUM_STEP, YOU_VALUE_LINE = 107, 119, 28.4
YOU_NUM_DY = 0  # tried 1 in step 9: the text moved 3.2 px on the strip render (1.6 px above the comp's became 1.6 px under it), so 0 stays


def you_nums():
    x, y, w, h, z, tab = at(P2, "c_you_nums")
    out = []
    for i, (value, label, lines, ink) in enumerate(YOU_NUMS):
        cx = x + YOU_NUM_STEP * i
        v = card("c_you_nums" if i == 0 else f"c_you_nums_v{i + 1}", cx, round(y + YOU_VALUE_LINE / 2 - 16) + YOU_NUM_DY, YOU_NUM_W + 8, 32, z, tab, [value], DISPLAY, 16, INK, off_grid=True)
        if ink:
            v["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv(ink)
        out.append(bind_alt(v, "Alt You Nums (text)") if i == 0 else decorative(v, 70 + i))
        centre = y + YOU_VALUE_LINE + lines * 21.3 / 2 - 0.7
        # the two-line label keeps the comp's 107 px so it wraps where the comp does; a one-line label gets the gap too
        lab = card(f"c_you_nums_l{i + 1}", cx, round(centre - CARD_H[lines] / 2) + YOU_NUM_DY, YOU_NUM_W + (0 if lines > 1 else 8), CARD_H[lines], z, tab, [label], BODY, S, INK2, off_grid=True)
        out.append(decorative(lab, 80 + i))
    return out


def top_text(page, name, measure, colour_measure, alt_measure=None):
    """A sentence of one or two lines set from the TOP of its slot. A card centres its text in its box, which is right for
    a known number of lines (note()); the rules line of Build is one line or two, depending on the plan. A shape sets its
    text from the top: a rectangle without fill or outline, its text and its ink bound to measures, no margins."""
    x, y, w, h, z, tab = at(page, name)
    objs = {"shape": [{"properties": {"tileShape": enum("rectangle")}, "selector": {"id": "default"}}],
            "fill": [{"properties": {"show": b(False)}}],
            "outline": [{"properties": {"show": b(False)}}],
            "text": [{"properties": {"show": b(True)}},
                     {"properties": {"text": mtext(measure), "fontFamily": text(BODY), "fontSize": num(S), "fontColor": fv(colour_measure), "bold": b(False),
                                     "horizontalAlignment": text("left"), "verticalAlignment": text("top"),
                                     "leftMargin": integer(0), "rightMargin": integer(0), "topMargin": integer(0), "bottomMargin": integer(0)}, "selector": {"id": "default"}}]}
    v = visual(name, "shape", x, y, w, h, z, tab, objects=objs, vcos=vco(padding=0))
    return bind_alt(v, alt_measure or measure)


# ch_build_bars (doc 22 section 3; spec charts.ch_build_bars): the visual rect that puts Power BI's rows and bars on the comp's
# (PLOT_RECT of step 5). The comp sets five rows of 32 px from the top of the slot (1384, 464, 464, 168) and starts the bars
# 14 px right of the longest name. Measured in build step 9: in the slot's own rect the rows stood 29.6 px apart and 10 px
# low (Power BI keeps 8 px above its plot and an outer padding of its own); with outer padding 0 and this rect five rows
# are 32 px apart from y 464. x and width: the strip render moves by about 3 px for 1 px of rect (Desktop snaps a visual to
# its device pixels at that zoom), so the two edges were settled from two renders one px apart (doc 23, log of step 9).
BARS_RECT = (1379, 462, 467, 157)
BARS_INNER = 40  # the comp's bar is 60 % of its row (measured: 16.8 px in a 32 px row, the comp's 18)


def build_bars():
    """ch_build_bars (R-B, R-G3): the NPV of each picked move, sorted from the highest down, as horizontal bars: Night for a
    move that adds NPV, Tangerine for one that costs NPV, each with its signed value outside its end (label-safe, P-1). No
    title, no value axis; the names in Dusk on the category axis, as wide as the longest picked name. Rows from BuildBar:
    the picked moves, and empty rows up to five so the bars keep the comp's pitch (sketch_model BARS_MIN_ROWS). The hidden
    value axis ends on the model's two measures, which leave the labels the comp's room. The zero line in Dusk."""
    q = {"Category": {"projections": [proj_col("BuildBar", "Name", display="Move")]},
         "Y": {"projections": [proj_mea("Build Bar NPV (label-safe)", "NPV through 2032")]},
         "Tooltips": {"projections": [proj_mea("Build Bar Order", "Order")]}}
    va = axis(BODY, S, INK2, show=False, gridlines=False)
    va[0]["properties"].update({"start": mtext("Build Bars X Start"), "end": mtext("Build Bars X End")})
    ca = axis(BODY, S, INK2, gridlines=None, extra={"maxMarginFactor": integer(45), "innerPadding": integer(BARS_INNER), "outerPadding": integer(0), "concatenateLabels": b(False)})
    objs = {"categoryAxis": ca, "valueAxis": va, "legend": legend(False),
            "dataPoint": [{"properties": {"fill": fv("Build Bar Color")}, "selector": WILD}],
            "labels": labels(True, BODY, S, INK, units=1, position="OutsideEnd"),
            # the zero line's value is a measure: blank while nothing is picked, or the empty chart would still draw the line
            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": mtext("Build Bars Zero"), "lineColor": color(INK2), "transparency": num(0), "width": num(1), "style": enum("solid"),
                                                    "position": enum("front"), "dataLabelShow": b(False)}, "selector": {"id": "1"}}]}
    v = chart(P2, "ch_build_bars", "clusteredBarChart", q, objs, None, sort=sort_by_measure("Build Bar Order"), alt_measure="Alt Build Bars (text)")
    return plot_rect(v, BARS_RECT)


def p2_build():
    """FinalV3 build step 9: the Build state (doc 21 section 8 with the slots of doc 22 section 2). The panel: head, the
    native selector beside the moves table, the footer that counts the picked moves; the your-plan tile (the outline frame
    is a tile of the layout): title or budget alarm, four numbers, the range, the rules line, the bars of the picked
    moves. The bottom card: your plan against A, with its hover tag. Reading order: head, selector, table, footer, title,
    numbers, range, rules, bars, chart (R-P2-9). The proof chart at the left is p2_proof(), with the plan dot "You".
    Your plan first (Night; Tangerine while over the budget), then A on top (Coffee Blue), as the comp draws them: when
    the state opens the two lines are one."""
    v = [build_head(), move_slicer(), moves_table(), note(P2, "c_sel_footer", "Build Picked (text)", 1)]
    v += you_title()
    v += you_nums()
    # build step 10: out of the tab order. The card is empty while nothing is picked (a stop that says nothing), and the
    # numbers' alt text (Alt You Nums) already reads the range with the four numbers.
    v.append(decorative(note(P2, "c_you_range", "Build Range (text)", 1, colour=INK), 60))
    v.append(top_text(P2, "c_you_rules", "Build Valid (text)", "Build Valid Color"))
    v.append(build_bars())
    lines = [("Build Cumulative Line", "Your plan", INK, 3, False, "Build Cumulative End Name (label-safe)", "Under", INK),
             ("Build Cumulative Line (over)", "Your plan, over the budget", SIGNAL_MARK, 3, False, None, None, False),
             ("Preset A Cumulative Line", "A, our recommendation", ACCENT_MARK, 3, False, "A Cumulative End Name (label-safe)", "Above", True)]
    v.append(cmp_chart("ch_cmp_build", lines, "Cmp Build Title (text)", "Alt Cmp Build (text)", "Cmp Build"))
    v.append(hover_tag_text(P2, "tag_cmp_build", "Hover a year", 24))
    return v


def p2_visuals():
    return p2_frame() + p2_hero() + p2_decision_card() + p2_capital_plan() + p2_proof() + p2_waits() + p2_build()


# ====================================================================== the package tooltip (08-verbeterplan V2, round 4)
TT = "tt-package"
# The moves table of the package tooltip (build step 10; R-TT-1, doc 21 section 9): Move, Capex, NPV at 12 pt on TTMove (the
# ten moves in the selector's order and a Total row; the TT Row measures are blank outside the hovered package, so only its
# moves and the total show). Columns and 2 px of slack fill the card's 416 px; the height holds the largest package
# (eight moves and the total) without a scrollbar.
TT_MOVES_COLS = (226, 86, 102)
TT_MOVES_PAD = 0.6  # measured in step 10: header 33 px, a row 21.6 px + twice the padding + its rule; eight moves and the total fit 256 px


def tt_moves_table():
    ms = ("TT Row Capex (text)", "TT Row NPV (text)")
    proj = [proj_col("TTMove", "Name", display="Move"), proj_mea(ms[0], "Capex"), proj_mea(ms[1], "NPV")]
    refs = ["TTMove.Name", *[mref(m_) for m_ in ms]]
    colfmt = [{"properties": {"alignment": enum("Right"), "styleHeader": b(True), "styleValues": b(True)}, "selector": {"metadata": r_}} for r_ in refs[1:]]
    objs = table_objects(BODY, S, INK, SURFACE, SURFACE, SURFACE, INK2, HAIR, row_padding=TT_MOVES_PAD, header_size=S, column_formatting=colfmt)
    objs["columnHeaders"][0]["properties"].update({"outlineStyle": enum("BottomOnly"), "outlineColor": color(INK2), "outlineWeight": num(1),
                                                   "autoSizeColumnWidth": b(False), "wordWrap": b(False)})
    objs["values"][0]["properties"]["wordWrap"] = b(False)
    objs["values"] += [{"properties": {"fontColor": fv("TT Row NPV Ink")}, "selector": {**WILD, "metadata": refs[2]}}]
    objs["columnWidth"] = [{"properties": {"value": num(w_)}, "selector": {"metadata": q_}} for q_, w_ in zip(refs, TT_MOVES_COLS)]
    t = visual("tt_moves_tbl", "tableEx", *at(TT, "tt_moves_tbl"), query={"Values": {"projections": proj}}, objects=objs, vcos=vco(padding=0))
    return bind_alt(t, "Alt TT Moves (text)")


def tt_visuals():
    """The package tooltip, round 7 (Björn, 11 Nov: leaner, in the page's own skin). On the night banner the kicker
    (PACKAGE A · EXPECTED CASE) and the title; a white card with the NPV, the capex, the verdict over the three cases
    and the range bar on the shared axis; a second card with the moves and their capex and NPV, adding up to the
    package. The round-6 waterfall bars, Answers column, histogram strip and move grid left: too much for a hover.
    Grain: one Package[PackageID] from the hover layer.
    Build step 10 (R-TT-1, doc 21 section 9): the range strip is one sentence (TT Range (text)) and the moves are a native
    table at body size (tt_moves_table()); no SVG is left on the page."""
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
         dyn(TT, "tt_range", "TT Range (text)"),  # R-TT-1: the three cases in one sentence, two lines at 12 pt
         c("tt_moves_label", "TT Moves Label (text)", S, INK, DISPLAY),
         tt_moves_table()]
    v[2]["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("TT NPV Color")
    v[4]["visual"]["objects"]["value"][0]["properties"]["fontColor"] = fv("TT Payback Color")
    return v


# ====================================================================== pages, bookmarks, resources
# Night-glow depth (plan 10 D7 with Bjorn's waiver, plan 11): one soft shadow for every card, a heavier one under each
# page's hero card, and a Coffee Blue glow under the recommendation. Values from the comps (comps_v3.GLOW).
SHADOW = {"card": (INK, 14, 36, 84), "hero": (INK, 24, 56, 72), "glow": (ACCENT_MARK, 14, 34, 70)}
HERO_CARDS = set()  # FinalV3: the comp draws every card frame with the one card shadow (.frame)
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


DATA_VISUALS = {"lineChart", "clusteredColumnChart", "clusteredBarChart", "barChart", "scatterChart", "tableEx", "waterfallChart"}  # round 9: + bars (the F4 chip tooltip)


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


# Build step 10 (R-X-1, R-P2-9): which way the Tab key runs. Measured in Desktop 2.159 with real key presses
# (tools/desktop_shots/step10/a11y_pass.ps1 -Do canvaswalk): Tab goes from the HIGHEST tabOrder to the lowest, Shift+Tab the
# other way; with the rising numbers the report carried until step 10, Tab started at the Definitions chip and ended at the
# logo. The generator and opzet-layering.json keep the reading order as rising numbers (10 = first stop); page() turns them
# into Desktop's falling order as its last act. Negative numbers (out of the tab order) stay as they are. If the published
# report ever shows the opposite, this one switch turns it back.
TAB_FALLING = True
TAB_TOP = 10000


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
    if TAB_FALLING:
        for vis in visuals:
            t = vis["position"]["tabOrder"]
            if t >= 0:
                assert t < TAB_TOP, (vis["name"], t)
                vis["position"]["tabOrder"] = TAB_TOP - t
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


# the visuals the move selector may filter: everything of the plan being built; nothing else listens to it, and
# tbl_moves keeps its ten rows (doc 21 section 8). The cards of the your-plan tile are named c_you_*.
BUILD_TARGETS = {"c_sel_footer", "ch_build_bars", "ch_cmp_build", "hero_s_packages_build", "hero_s_packages_you"}


def build_target(name):
    return name in BUILD_TARGETS or name.startswith("c_you_")


def interactions(v2):
    out = []
    names = {o["name"] for o in v2}
    # the hover layers only show tooltips, the build dot only marks: a click on them must not filter or dim anything
    for src in ("hero_s_packages_hover", "hero_s_packages_build", "hero_s_packages_you"):
        if src in names:
            out += [{"source": src, "target": o["name"], "type": "NoFilter"} for o in v2 if o["name"] != src]
    # the move selector (sl_moves, build step 9) filters the plan being built (DataFilter, never a highlight) and nothing else
    assert "sl_moves" in names and all(t_ in names for t_ in BUILD_TARGETS)
    out += [{"source": "sl_moves", "target": o["name"], "type": "DataFilter" if build_target(o["name"]) else "NoFilter"}
            for o in v2 if o["name"] != "sl_moves"]
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
    write_json(rj, report)
    bm = rep / "definition" / "bookmarks"
    for st, display in (("rec", "P2 Recommended: A"), ("alts", "P2 What waits, and why"), ("build", "P2 Build your own")):
        write_json(bm / f"bm_p2_{st}.bookmark.json", bookmark(f"bm_p2_{st}", display, st, v2))
    write_json(bm / "bookmarks.json", {"$schema": BOOKMARKS_SCHEMA, "items": [{"name": f"bm_p2_{st}"} for st in STATES]})
    n1, n2 = len(v1), len(v2)
    core = sum(1 for v in v1 + v2 if v["visual"]["visualType"] in ("tableEx", "pivotTable", "clusteredBarChart", "clusteredColumnChart", "lineChart", "scatterChart", "waterfallChart"))
    hidden = sum(1 for v in v2 if v.get("isHidden"))
    print(f"report written: {rep}  P1 {n1} visuals, P2 {n2} visuals ({hidden} hidden in the {OPEN_STATE} state), {core} core chart/table visuals")


if __name__ == "__main__":
    main()
