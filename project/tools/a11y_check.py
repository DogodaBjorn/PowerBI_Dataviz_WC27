"""Machine accessibility check of the generated opzet report (plan 11, step 6, pass 1 of 3).

usage (repo root):  python project/tools/a11y_check.py [report folder]
default report:     project/pbip/GoodnightInn-opzet.Report

Reads the PBIR the generators wrote, the model's measures (for alt-text and colour measures), the slot map (for
the panel states and the cards) and the night-glow canvas (for text on the header zone). Exit code 1 on any FAIL.
What it checks, per visual and per page:
  alt       every visual in the tab order has alt text (static or a measure that exists); no placeholder (a
            measure's name), no colour words, no typed numbers other than years, at most 250 characters, no
            leading chart type; a button's spoken name carries its visible label; decorative visuals sit out of
            the tab order (negative tabOrder, as Desktop stores 'hidden from tab order')
  order     tab order is unique per page and follows the reading order: header chrome, then the cards top to
            bottom and left to right, inside a card row by row, the footer last; checked per P2 panel state
  type      every font size at or above the 12 pt floor (16 px in text boxes), charts not responsive (it shrinks
            their text); only the Segoe UI / Arial stacks
  contrast  every text colour against what it really sits on (a white card, the Oat page or the night zone, whose
            lightest pixel under the text is read from the canvas): 4.5:1, 3:1 from 24 px; colours that come from
            a measure are checked for every hex the measure can return; marks against white 3:1; button and
            slicer states (default, hover, selected)
  data      data visuals in the tab order keep their header (focus mode, 'show as a table'); table and slicer
            labels are not blank; images are embedded (registered resources or data: URIs), never links
Practice after Meagan Longoria's Power BI accessibility checklist and WCAG 2.2 (CREDITS.md, a11y-studio). The
rendered checks (screen-reader tree, keyboard walk) and the independent review are passes 2 and 3 (plan 11).
Needs Pillow for the canvas pixels (the canvas generator, brand_canvas_v3.py, already does).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "project" / "pbip" / "GoodnightInn-opzet.Report"
MEASURES_TMDL = ROOT / "project" / "pbip" / "PillowKey.SemanticModel" / "definition" / "tables" / "_Measures.tmdl"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from slot_map import load_layout  # noqa: E402  (build step 5: P1 from v10, P2 from v9 until step 6)
LAYOUT = load_layout()
CANVAS = ROOT / "project" / "deliverables" / "backgrounds" / "canvas-night.jpg"
SURFACE = "#FFFFFF"
# what a tile paints under its visuals (opzet_report.TILE_KIND): glow and outline are white, tint is Ice, night is Night
TILE_FILL = {"glow": SURFACE, "tint": "#EAF2FB", "outline": SURFACE}
FLOOR_PT, FLOOR_PX = 12, 16
FONTS_OK = ("segoe ui", "arial")
COLOUR_WORDS = re.compile(r"\b(raspberry|plum|lilac|ember|pink|magenta|tangerine|blue|grey|gray|red|green|orange|purple|violet|coffee)\b", re.I)
NUMBER = re.compile(r"\$|%|\d[\d,]*\.\d|\b\d{2,}\b")
YEAR = re.compile(r"\b(19|20)\d\d\b")
DATA_VISUALS = {"lineChart", "clusteredColumnChart", "scatterChart", "tableEx", "waterfallChart", "pivotTable", "clusteredBarChart"}
# which property of which formatting object is text (the rest are fills, lines and borders)
TEXT_PROPS = {"labels": ["color"], "categoryAxis": ["labelColor", "titleColor"], "valueAxis": ["labelColor", "titleColor"],
              "legend": ["labelColor"], "seriesLabels": ["seriesColor"], "value": ["fontColor"], "label": ["fontColor"],
              "columnHeaders": ["fontColor"], "values": ["fontColorPrimary", "fontColorSecondary"], "items": ["fontColor"],
              "header": ["fontColor"], "y1AxisReferenceLine": ["dataLabelColor"], "categoryLabels": ["color"], "title": ["fontColor"]}

fails, notes = [], []
SVG_FONT = re.compile(r"font-size='(\d+(?:\.\d+)?)'")


TAB_FALLING = True  # the same switch as opzet_report.TAB_FALLING: the first stop of the Tab key has the highest tabOrder


def fail(where, msg):
    fails.append(f"FAIL  {where}: {msg}")


def note(where, msg):
    notes.append(f"note  {where}: {msg}")


# ---------------------------------------------------------------- colour maths (WCAG 2.2 relative luminance)
def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    def ch(v):
        v = v / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = c if isinstance(c, tuple) else rgb(c)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ---------------------------------------------------------------- model measures
MEAS = {}
for line in MEASURES_TMDL.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\tmeasure (?:'((?:[^']|'')+)'|(\S+)) = (.*)$", line)
    if m:
        MEAS[(m.group(1) or m.group(2)).replace("''", "'")] = m.group(3)
HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")


def literal(v):
    if isinstance(v, dict):
        lit = v.get("expr", {}).get("Literal", {}).get("Value")
        if lit is not None:
            return lit.strip("'") if lit.startswith("'") else lit
    return None


def measure_of(v):
    if isinstance(v, dict):
        e = v.get("expr", {}).get("Measure")
        if e:
            return e["Property"]
    return None


def ordered_colours(prop):
    """Like colours(), but in the order the measure's DAX names them (branch for branch), duplicates kept."""
    if not isinstance(prop, dict):
        return []
    inner = prop.get("solid", {}).get("color", prop)
    lit = literal(inner)
    if lit and HEX.fullmatch(lit):
        return [lit.upper()]
    mm = measure_of(inner)
    return [h.upper() for h in HEX.findall(MEAS.get(mm, ""))] if mm else []


def colours(prop):
    """Hex colours a colour property can take: a literal, or every hex a field-value measure returns."""
    if not isinstance(prop, dict):
        return []
    inner = prop.get("solid", {}).get("color", prop)
    lit = literal(inner)
    if lit and HEX.fullmatch(lit):
        return [lit.upper()]
    mm = measure_of(inner)
    if mm:
        return sorted({h.upper() for h in HEX.findall(MEAS.get(mm, ""))})
    return []


# ---------------------------------------------------------------- canvas pixels (night zone and Oat page)
try:
    from PIL import Image
    IMG = Image.open(CANVAS).convert("RGB")
except Exception as exc:  # noqa: BLE001
    IMG = None
    fail("canvas", f"cannot read {CANVAS.name} ({exc}); install Pillow, the canvas generator needs it too")


TT_IMGS = {}


def tooltip_extremes(pname, x, y, w, h):
    """Round 7: a tooltip page has a scene of its own (canvas-tt-<page>.jpg, actual size), so text on its banner is
    checked against the lightest and darkest pixel under it, like text on the page's night zone."""
    img = TT_IMGS.get(pname)
    if img is None:
        f = CANVAS.parent / f"canvas-tt-{pname}.jpg"
        img = TT_IMGS[pname] = Image.open(f).convert("RGB") if (IMG is not None and f.exists()) else False
    return extremes(img, x, y, w, h, 1, 1) if img else None


def canvas_extremes(x, y, w, h):
    """The lightest and the darkest pixel under a rectangle of the 1920x1080 canvas (every 2nd pixel)."""
    if IMG is None:
        return None
    return extremes(IMG, x, y, w, h, IMG.width / LAYOUT["canvas"]["w"], IMG.height / LAYOUT["canvas"]["h"])


def extremes(IMG, x, y, w, h, sx, sy):
    lo = hi = None
    for yy in range(int(y * sy), int((y + h) * sy), 2):
        for xx in range(int(x * sx), int((x + w) * sx), 2):
            p = IMG.getpixel((min(xx, IMG.width - 1), min(yy, IMG.height - 1)))
            L = lum(p)
            if hi is None or L > hi[0]:
                hi = (L, p)
            if lo is None or L < lo[0]:
                lo = (L, p)
    return lo[1], hi[1]


# ---------------------------------------------------------------- report
def page_layout(name):
    return next((p for p in LAYOUT["pages"] if p["name"] == name), None)


STATES = ("rec", "alts", "build")  # the P2 panel states (round 4); a slot's state is a list of them, or absent


def _states(entry):
    st = (entry or {}).get("state")
    if st is None:
        return None
    return [st] if isinstance(st, str) else list(st)


def state_of(pl, vname):
    """The states a visual is shown in (a list) or None when always visible; cards and tiles read their own entries."""
    if pl is None:
        return None
    if vname.startswith("z_card_"):
        return _states(next((c for c in pl.get("cards", []) if f"z_card_{c['id']}" == vname), None))
    if vname.startswith("z_tile_"):
        return _states(next((t for t in pl.get("tiles", []) if f"z_tile_{t['id']}" == vname), None))
    slots = {v["name"]: v for v in pl["visuals"]}
    base = vname if vname in slots else vname.rsplit("_", 1)[0]
    return _states(slots.get(base))


def container(pl, x, y, w, h, st=None):
    """The card a visual sits in (by its centre), or None for chrome on the canvas; in a state, only that state's cards."""
    cx, cy = x + w / 2, y + h / 2
    for c in (pl or {}).get("cards", []):
        if st and _states(c) and st not in _states(c):
            continue
        if c["x"] <= cx <= c["x"] + c["w"] and c["y"] <= cy <= c["y"] + c["h"]:
            return c
    return None


def tile_of(pl, x, y, w, h, st=None):
    """The tile a visual sits in (by its centre), or None."""
    cx, cy = x + w / 2, y + h / 2
    for t in (pl or {}).get("tiles", []):
        if st and _states(t) and st not in _states(t):
            continue
        if t["x"] <= cx <= t["x"] + t["w"] and t["y"] <= cy <= t["y"] + t["h"]:
            return t
    return None


def walk(o, fn, path=()):
    if isinstance(o, dict):
        fn(o, path)
        for k, v in o.items():
            walk(v, fn, path + (k,))
    elif isinstance(o, list):
        for v in o:
            walk(v, fn, path)


# SVG-in-DAX images (round 6): every font-size inside an image measure's SVG is held to the 16 px floor, because the
# pixel check cannot see inside a data: URI
for _name, _dax in MEAS.items():
    if "data:image/svg" in _dax:
        for _px in SVG_FONT.findall(_dax):
            if float(_px) < FLOOR_PX:
                fail(f"measure [{_name}]", f"SVG text at {_px} px is under the {FLOOR_PX} px floor")

report = json.loads((REPORT / "definition" / "report.json").read_text(encoding="utf-8"))
registered = {i["name"] for pk in report.get("resourcePackages", []) for i in pk.get("items", [])}
pages_meta = json.loads((REPORT / "definition" / "pages" / "pages.json").read_text(encoding="utf-8"))
visible_pages = 0
for pname in pages_meta["pageOrder"]:
    pdir = REPORT / "definition" / "pages" / pname
    page = json.loads((pdir / "page.json").read_text(encoding="utf-8"))
    if page.get("visibility") != "HiddenInViewMode":
        visible_pages += 1
        if not page.get("displayName", "").strip():
            fail(pname, "page without a display name")
    pl = page_layout(pname)
    page_bg = colours(page.get("objects", {}).get("background", [{}])[0].get("properties", {}).get("color")) or [SURFACE]
    tooltip = page.get("type") == "Tooltip"
    visuals = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((pdir / "visuals").glob("*/visual.json"))]
    tabs = {}
    for v in visuals:
        name, pos, vis = v["name"], v["position"], v["visual"]
        where = f"{pname}/{name}"
        vtype = vis["visualType"]
        tab = pos.get("tabOrder", 0)
        vco = vis.get("visualContainerObjects", {})
        alt = (vco.get("general") or [{}])[0].get("properties", {}).get("altText")
        alt_text, alt_meas = literal(alt), measure_of(alt)

        # -------- alt text and the tab order
        if tab >= 0:
            if tab in tabs:
                fail(where, f"tabOrder {tab} also used by {tabs[tab]}")
            tabs[tab] = name
            if not (alt_text or alt_meas):
                fail(where, "in the tab order without alt text")
            if alt_meas and alt_meas not in MEAS:
                fail(where, f"alt text measure [{alt_meas}] is not in the model")
            if alt_text:
                if alt_text in MEAS or alt_text.endswith("(text)") or any(alt_text == k.replace(" (text)", "") for k in MEAS):
                    fail(where, f"placeholder alt text (a measure name): {alt_text!r}")
                if alt_text.lower().startswith("decorative"):
                    fail(where, "decorative alt text on a visual that is in the tab order")
                if COLOUR_WORDS.search(alt_text):
                    fail(where, f"colour word in alt text: {alt_text!r}")
                if NUMBER.search(YEAR.sub("", alt_text)):
                    fail(where, f"typed number in static alt text (bind it to a measure): {alt_text!r}")
            if alt_meas and COLOUR_WORDS.search(re.sub(r'\[[^\]]*\]|\'[^\']*\'', "", MEAS.get(alt_meas, ""))):
                fail(where, f"colour word in the alt text measure [{alt_meas}]")
            if alt_text and len(alt_text) > 250:
                fail(where, f"static alt text is {len(alt_text)} characters (Desktop's limit is 250)")
            if alt_meas and re.match(r'\s*"(line chart|column chart|bar chart|scatter|table|waterfall|chart)\b', MEAS.get(alt_meas, ""), re.I):
                fail(where, f"alt text measure [{alt_meas}] opens with the chart type, which Power BI already announces")
            if vtype == "actionButton":
                lab = next((e["properties"].get("text") for e in vis.get("objects", {}).get("text", []) if e.get("selector", {}).get("id") == "default"), None)
                if measure_of(lab) and not alt_meas:
                    fail(where, "button label comes from a measure but its alt text is static: the spoken name may not carry the visible label (WCAG 2.5.3)")
                elif literal(lab) and alt_text and re.sub(r"[^a-z ]", "", literal(lab).lower()).strip() not in alt_text.lower():
                    fail(where, f"button alt text does not contain its visible label {literal(lab)!r} (WCAG 2.5.3)")
            if vtype in DATA_VISUALS and not literal((vco.get("visualHeader") or [{}])[0].get("properties", {}).get("show")) == "true":
                fail(where, "data visual in the tab order with its header off (no focus mode / show as a table)")
        else:
            if alt_text or alt_meas:
                note(where, "out of the tab order but still carries alt text")

        if vtype in DATA_VISUALS - {"tableEx", "pivotTable"} and literal((vis.get("objects", {}).get("general") or [{}])[0].get("properties", {}).get("responsive")) != "false":
            fail(where, "chart is responsive: Power BI may shrink its text under the floor in a small slot")
        # -------- type: sizes and families
        def type_check(o, path):
            for k in ("fontSize", "textSize", "titleFontSize"):
                if k in o:
                    val = o[k]
                    if not isinstance(val, str):  # px sizes belong to text-box runs, checked below with their text
                        lit = literal(val)
                        if lit and lit.endswith("D") and float(lit[:-1]) < FLOOR_PT:
                            fail(where, f"{'/'.join(path[-2:])}.{k} {lit[:-1]} pt is under the {FLOOR_PT} pt floor")
            for k in ("fontFamily", "seriesFontFamily", "titleFontFamily"):
                if k in o:
                    fam = o[k] if isinstance(o[k], str) else literal(o[k])
                    if fam and not any(f in fam.lower() for f in FONTS_OK):
                        fail(where, f"font {fam!r} is not Segoe UI or Arial")
        walk(vis, type_check)
        # text box runs: size in px, colour in hex
        runs = []
        for par in (vis.get("objects", {}).get("general") or [{}])[0].get("properties", {}).get("paragraphs", []):
            for r in par.get("textRuns", []):
                st = r.get("textStyle", {})
                if r.get("value", "").strip():
                    runs.append((st.get("color", "#000000").upper(), float(st.get("fontSize", "16px")[:-2]), st.get("fontFamily", "")))
                    if float(st.get("fontSize", "16px")[:-2]) < FLOOR_PX:
                        fail(where, f"text run at {st.get('fontSize')} is under the {FLOOR_PX} px floor: {r['value'][:40]!r}")

        # -------- contrast: what the text sits on
        x, y, w, h = pos["x"], pos["y"], pos["width"], pos["height"]
        card = container(pl, x, y, w, h) if pl else None
        if card is not None:
            bgs = [SURFACE]
        elif tooltip:  # round 7: outside its cards a tooltip page shows its own night scene (the banner)
            ext = tooltip_extremes(pname, x, y, w, h)
            bgs = ["#%02X%02X%02X" % ext[0], "#%02X%02X%02X" % ext[1]] if ext else page_bg
        elif vtype == "image":
            bgs = []
        else:
            ext = canvas_extremes(x, y, w, h)
            bgs = ["#%02X%02X%02X" % ext[0], "#%02X%02X%02X" % ext[1]] if ext else page_bg
        # a tile paints its own fill under the visual (round 5: the tooltip's night header band)
        v_states = state_of(pl, name)
        tile = tile_of(pl, x, y, w, h, v_states[0] if v_states else None)
        if tile is not None:
            bgs = [TILE_FILL.get(tile.get("kind", "glow"), SURFACE)]
        # a visual with its own background (round 5: the budget alarm band): a literal fill replaces the surface; a
        # fill from a measure is paired branch for branch with the text colour measure (the two IFs share a condition)
        own_bg = (vco.get("background") or [{}])[0].get("properties", {})
        own_fill = own_bg.get("color") if literal(own_bg.get("show")) == "true" and own_bg.get("color") else None
        paired = bool(own_fill) and measure_of(own_fill.get("solid", {}).get("color", own_fill)) is not None
        if own_fill and not paired:
            bgs = colours(own_fill) or bgs
        texts = [(c, px >= 24) for c, px, _ in runs]
        objs = vis.get("objects", {})
        marks = sorted({c for dp in objs.get("dataPoint", []) for k in ("fill", "defaultColor") for c in colours(dp.get("properties", {}).get(k))})
        on_marks = []  # text drawn on a marker (scatter letters): checked against the marker colours
        for obj, keys in TEXT_PROPS.items():
            for e in objs.get(obj, []) + (vco.get(obj, []) if obj == "title" else []):
                pr = e.get("properties", {})
                size = literal(pr.get("fontSize") or pr.get("textSize") or pr.get("titleFontSize")) or "12D"
                big = float(size.rstrip("D")) >= 18
                if obj == "seriesLabels" and literal(pr.get("show")) == "true" and literal(pr.get("seriesMatchColor")) == "true":
                    texts += [(c, big) for c in marks]  # a label in its line's colour
                for k in keys:
                    if paired and obj == "value" and k == "fontColor":
                        inks, fills_ = ordered_colours(pr.get(k)), ordered_colours(own_fill)
                        if len(inks) != len(fills_) or not inks:
                            fail(where, f"text colour measure and background measure do not pair branch for branch ({len(inks)} vs {len(fills_)})")
                        for ic, fc in zip(inks, fills_):
                            if ratio(ic, fc) < (3.0 if big else 4.5):
                                fail(where, f"text {ic} on its own fill {fc}: {ratio(ic, fc):.2f}:1 (needs {3.0 if big else 4.5}:1)")
                        continue
                    for c in colours(pr.get(k)):
                        if obj == "categoryLabels" and literal(pr.get("enableBackground")) == "true" and colours(pr.get("backgroundColor")):
                            # build step 9: a category label on a background of its own (the plan's name "You" on white)
                            for bg in colours(pr.get("backgroundColor")):
                                if ratio(c, bg) < (3.0 if big else 4.5):
                                    fail(where, f"label {c} on its own background {bg}: {ratio(c, bg):.2f}:1")
                            continue
                        (on_marks if obj == "categoryLabels" else texts).append((c, big))
        if vtype not in ("actionButton", "advancedSlicerVisual", "image") and bgs:
            for c, big in texts:
                for bg in bgs:
                    need = 3.0 if big else 4.5
                    r = ratio(c, bg)
                    if r < need:
                        fail(where, f"text {c} on {bg}: {r:.2f}:1 (needs {need}:1)")
        for c, big in on_marks:
            for mk in marks:
                if ratio(c, mk) < (3.0 if big else 4.5):
                    fail(where, f"label {c} on its marker {mk}: {ratio(c, mk):.2f}:1")

        # -------- marks against the white card
        for dp in vis.get("objects", {}).get("dataPoint", []):
            for k in ("fill", "defaultColor"):
                for c in colours(dp.get("properties", {}).get(k)):
                    if ratio(c, SURFACE) < 3.0:
                        fail(where, f"mark {c} on white: {ratio(c, SURFACE):.2f}:1 (needs 3:1)")
        for sc in vis.get("objects", {}).get("sentimentColors", []):
            for k, cc in sc.get("properties", {}).items():
                for c in colours(cc):
                    if ratio(c, SURFACE) < 3.0:
                        fail(where, f"waterfall {k} {c} on white: {ratio(c, SURFACE):.2f}:1")

        # -------- buttons and button slicers: text against its own fill, per state
        if vtype in ("actionButton", "advancedSlicerVisual"):
            objs = vis.get("objects", {})
            fills = {e.get("selector", {}).get("id", "default"): colours(e["properties"].get("fillColor")) for e in objs.get("fill", []) + objs.get("fillCustom", [])
                     if e.get("properties", {}).get("fillColor")}
            inks = {e.get("selector", {}).get("id", "default"): colours(e["properties"].get("fontColor")) for e in objs.get("text", []) + objs.get("value", [])
                    if e.get("properties", {}).get("fontColor")}
            norm = lambda s: s.split(":")[-1]
            fills = {norm(k): v2 for k, v2 in fills.items()}
            inks = {norm(k): v2 for k, v2 in inks.items()}
            for st in sorted(set(fills) | set(inks)):
                for fc in fills.get(st) or fills.get("default", []):
                    for ic in inks.get(st) or inks.get("default", []):
                        if ratio(ic, fc) < 4.5:
                            fail(where, f"{st} state: text {ic} on {fc}: {ratio(ic, fc):.2f}:1")

        # -------- tables, slicers, images
        if vtype == "tableEx":
            for pr in vis.get("query", {}).get("queryState", {}).get("Values", {}).get("projections", []):
                if not (pr.get("displayName", pr.get("nativeQueryRef", "")) or "").strip():
                    fail(where, f"table column without a header: {pr.get('queryRef')}")
        if vtype in ("slicer", "advancedSlicerVisual") and tab >= 0 and not (alt_text or alt_meas):
            fail(where, "slicer without a header or alt text")
        if vtype == "image":
            img = (vis.get("objects", {}).get("image") or [{}])[0].get("properties", {})
            src = img.get("sourceFile", {}).get("image", {}).get("url", {}).get("expr", {}).get("ResourcePackageItem", {}).get("ItemName")
            url_m = measure_of(img.get("sourceUrl", {}))
            if src:
                if src not in registered:
                    fail(where, f"image {src} is not a registered resource")
            elif url_m:
                if 'data:image' not in MEAS.get(url_m, ""):
                    fail(where, f"image measure [{url_m}] is not a data: URI")
            else:
                fail(where, "image without an embedded source")

    # -------- reading order: chrome, cards (top to bottom, left to right), footer; per P2 panel state
    if pl and not tooltip:
        for st in STATES:
            cards = sorted([c for c in pl.get("cards", []) if not _states(c) or st in _states(c)], key=lambda c: (c["y"], c["x"]))
            first_card_y = min(c["y"] for c in cards)
            seq = []
            for v in visuals:
                t = v["position"].get("tabOrder", 0)
                s_ = state_of(pl, v["name"])
                if t < 0 or v.get("isHidden") and s_ is None or (s_ and st not in s_):
                    continue
                p = v["position"]
                c = container(pl, p["x"], p["y"], p["width"], p["height"], st)
                grp = (cards.index(c) + 1) if c else (0 if p["y"] < first_card_y else len(cards) + 1)
                # a tile is a sub-card (round 4: B and C side by side): a visual inside one is placed by the tile's
                # rectangle against visuals outside it, so a tile is read whole before the next tile or row
                tile = tile_of(pl, p["x"], p["y"], p["width"], p["height"], st)
                # build step 10: Tab runs from the highest tabOrder to the lowest (opzet_report.TAB_FALLING, measured in Desktop)
                seq.append((-t if TAB_FALLING else t, grp, p["y"], p["y"] + p["height"], p["x"], p["x"] + p["width"], v["name"], tile))
            seq.sort(key=lambda e: e[:2])
            for a, b2 in zip(seq, seq[1:]):
                if b2[1] < a[1]:
                    fail(f"{pname}[{st}]", f"tab order goes back to an earlier card: {a[6]} -> {b2[6]}")
                elif b2[1] == a[1]:
                    ra, rb = a[2:6], b2[2:6]
                    if a[7] != b2[7]:
                        ra = (a[7]["y"], a[7]["y"] + a[7]["h"], a[7]["x"], a[7]["x"] + a[7]["w"]) if a[7] else ra
                        rb = (b2[7]["y"], b2[7]["y"] + b2[7]["h"], b2[7]["x"], b2[7]["x"] + b2[7]["w"]) if b2[7] else rb
                    above = rb[1] <= ra[0]
                    same_row_left = not (rb[1] <= ra[0] or rb[0] >= ra[1]) and rb[3] <= ra[2]
                    if above or same_row_left:
                        fail(f"{pname}[{st}]", f"tab order against the reading order: {a[6]} (y {a[2]}, x {a[4]}) -> {b2[6]} (y {b2[2]}, x {b2[4]})")

if visible_pages != 2:
    fail("report", f"{visible_pages} visible pages (the contest asks for exactly two)")

for n in notes:
    print(n)
for f in fails:
    print(f)
print(f"a11y_check: {len(fails)} failure(s), {len(notes)} note(s) over {REPORT.name}")
sys.exit(1 if fails else 0)
