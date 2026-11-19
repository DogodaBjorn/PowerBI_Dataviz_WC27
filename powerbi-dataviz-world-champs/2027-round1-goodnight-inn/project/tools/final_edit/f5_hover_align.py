"""Edit on the hand-finished report after Bjorn's save of 16 Nov 13:18 (doc 33): no raw SVG text on hover in the hero
table, and card IV of page 1 ends where the bottom card of page 2 ends.

  python f5_hover_align.py <.Report dir>

Runs on the saved report in place and can be run again (it sets, it does not add). What it sets:

  cover_hero_yield, cover_hero_npv   (page 2, new) two invisible rectangles over the ten body cells of the two bar columns
               of tbl_hero. Why: a bar is an image as high as its row (34 px), and an inline image stands on the text
               baseline, so the cell's content is 38 px in a 34 px cell. The table then treats the cell as cut off and
               shows its value in a tooltip, and the value of an image cell is its data URI ("data:image/svg+xml;utf8,<svg
               ..."). That tooltip does not listen to "Tooltips: off" (measured in Desktop 2.159: scrollHeight 38,
               clientHeight 34; desktop.PivotTableVisuals shouldHideDefaultTooltip). A box on top takes the mouse, so the
               cell is never hovered. The picture does not change; the numbers of both columns stand beside the bars as
               text. Hidden with the table in the two other views (bookmarks), out of the tab order, "no filter" from
               every chart.
  z_card_card_f4  (page 1) its foot at the foot of page 2's bottom card (z_card_bottom), and the same left edge and width.
  lnk_f4       the link line keeps its distance to the card's foot, so it moves down with it.
  btn_back     (page 2) one layer above the source line. Bjorn moved it into the footer row, where the source line's box
               (1697 px wide, its words end before the button) lay on top of it and took the click. And in the tab order
               between the source line and Definitions, as Next is on page 1 (it still came before the headline).
"""
import json
import sys
from pathlib import Path

REPORT = Path(sys.argv[1])
P1 = REPORT / "definition" / "pages" / "p1-brand-review"
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy"

# tbl_hero as built: the left edge of the cells is 1 px inside the visual, the header row is 32 px, ten rows of 34 px;
# the two bar columns start 480 and 740 px into the cells and are 196 and 184 px wide (sm.HERO_COLS). Measured on the
# page in Desktop: cells at x 536.9 and 796.9, y 255.6 to 595.6. One px more on every side, so no edge stays open at
# another zoom (the neighbours are text cells that fit, they have no tooltip to lose).
COVERS = {"cover_hero_yield": (481, 196), "cover_hero_npv": (741, 184)}
HEADER_H, ROWS, ROW_H, EDGE = 32, 10, 34, 1
LNK_F4_FROM_FOOT = 1020 - 985.7142857142857  # the link line's top above the card's foot, as Bjorn placed it


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


# ---- page 2: the covers
hero = load(P2 / "visuals" / "tbl_hero" / "visual.json")
hp = hero["position"]
low = min(v["position"]["tabOrder"] for d in (P2 / "visuals").iterdir() if d.name not in COVERS
          for v in [load(d / "visual.json")] if "tabOrder" in v["position"])
off = {"properties": {"show": lit("false")}}
for i, (name, (dx, w)) in enumerate(COVERS.items()):
    v = {"$schema": hero["$schema"], "name": name,
         "position": {"x": hp["x"] + dx - EDGE, "y": hp["y"] + HEADER_H - EDGE, "z": hp["z"] + 500 + i, "height": ROWS * ROW_H + 2 * EDGE, "width": w + 2 * EDGE,
                      "tabOrder": low - 1000 * (i + 1)},
         "visual": {"visualType": "shape",
                    "objects": {"shape": [{"properties": {"tileShape": lit("'rectangle'")}}],
                                "fill": [{"properties": {"show": lit("true")}},
                                         {"properties": {"fillColor": {"solid": {"color": lit("'#FFFFFF'")}}, "transparency": lit("100D")}, "selector": {"id": "default"}}],
                                "outline": [off], "text": [off]},
                    "visualContainerObjects": {k: [off] for k in ("title", "background", "border", "dropShadow", "visualHeader", "subTitle", "visualTooltip")}
                    | {"padding": [{"properties": {s_: lit("0D") for s_ in ("top", "bottom", "left", "right")}}]}}}
    d = P2 / "visuals" / name
    d.mkdir(exist_ok=True)
    (d / "visual.json").write_text(json.dumps(v, indent=2, ensure_ascii=False), encoding="utf-8", newline=chr(13) + chr(10))


def no_filter(page):
    have = {(i["source"], i["target"]) for i in page["visualInteractions"]}
    for src in sorted({i["source"] for i in page["visualInteractions"]}):
        page["visualInteractions"] += [{"source": src, "target": c, "type": "NoFilter"} for c in COVERS if (src, c) not in have]


edit(P2 / "page.json", no_filter)


def with_the_table(bm):
    """A cover is shown where the table is shown and hidden where it is hidden."""
    o = bm.get("options", {})
    if "targetVisualNames" in o:
        o["targetVisualNames"] = [n for n in o["targetVisualNames"] if n not in COVERS] + list(COVERS)
    for sec in bm["explorationState"]["sections"].values():
        vc = sec.get("visualContainers", {})
        if "tbl_hero" in vc:
            for c in COVERS:
                vc[c] = {"singleVisual": {"visualType": "shape", **({"display": dict(vc["tbl_hero"]["singleVisual"]["display"])} if "display" in vc["tbl_hero"]["singleVisual"] else {})}}


for f in sorted((REPORT / "definition" / "bookmarks").glob("*.bookmark.json")):
    edit(f, with_the_table)

# ---- page 1: card IV ends where page 2's bottom card ends
bottom = load(P2 / "visuals" / "z_card_bottom" / "visual.json")["position"]
foot = bottom["y"] + bottom["height"]


def card(v):
    p = v["position"]
    p["x"], p["width"], p["height"] = bottom["x"], bottom["width"], foot - p["y"]


def link(v):
    v["position"]["y"] = foot - LNK_F4_FROM_FOOT


edit(P1 / "visuals" / "z_card_card_f4" / "visual.json", card)
edit(P1 / "visuals" / "lnk_f4" / "visual.json", link)

# ---- page 2: Back above the source line's box
footer = load(P2 / "visuals" / "z_footer2" / "visual.json")["position"]
chip = load(P2 / "visuals" / "chip_def2" / "visual.json")["position"]


def above_footer(v):
    v["position"]["z"] = footer["z"] + 500
    v["position"]["tabOrder"] = (footer["tabOrder"] + chip["tabOrder"]) // 2


edit(P2 / "visuals" / "btn_back" / "visual.json", above_footer)
print(f"f5_hover_align: covers on the two bar columns, card IV's foot at y {foot:.3f}, Back above the source line")
