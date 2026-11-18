"""Edit on the hand-finished report (16 Nov 2026 night, doc 39): the text of the hero table stands in the middle of its
row.

  python f10_rows_centred.py <.Report dir> <.SemanticModel dir>

Bjorn, 16 Nov: "the text in the table is aligned to the top of the row instead of the middle; this makes the highlight
look a bit odd. Can we middle the text or is that impossible?" A native table has no vertical alignment (Microsoft's
formatting catalog: values, grid, columnFormatting and columnHeaders carry none). What it has is row padding, and a row
with the same padding above and under its text has its text in the middle. This script edits the saved report in place
and can be run again (it sets, it does not add). What it sets:

  tbl_hero      row padding 5 px and an image height of 23 px: a row is 33 px (it was 34) with its text and its bar in
                the middle. The header takes the padding too, so the table starts higher by what the header grew above
                its text: the header's words stay where they were.
  the model     Hero Yield Bar SVG and Hero NPV Bar SVG are 23 px high (the generator's model): the bar in the middle and
                the reference line as high as the image. An image cannot be higher than the row minus its padding, so the
                line no longer runs unbroken: each row has its own stroke, 10 px apart, a dashed line down the table.
                It stays inside the image and so on the bars at every zoom.
  cover_hero_yield, cover_hero_npv   (doc 33) over the rows where they are now.
  hero_line_8, hero_line_0   removed if present: two rectangles over the table were tried for an unbroken line and dropped
                (Desktop snaps a shape to whole screen pixels; at some zooms the line stood a hair off the bars).
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model_sync import sync_measures  # noqa: E402

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy"

PAD, IMG_H = 5, 23                    # sketch_model.HERO_PAD, HERO_IMG_H
# Measured on a throwaway copy (doc 39): with this padding the header is HEADER_H high (it was 33.5) and a row 33.0 px.
TABLE_Y, TABLE_H = 219.5, 378          # was 224 and 374: the header's words stay at their height
HEADER_H, ROW_H, ROWS = 41.9, 33.1, 10
BODY_TOP, BODY_H = TABLE_Y + HEADER_H, ROWS * ROW_H
COVERS = ("cover_hero_yield", "cover_hero_npv")
LINES = ["hero_line_8", "hero_line_0"]


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    if out.encode("utf-8") != raw[3 if bom else 0:]:
        path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


changed, added = sync_measures(MODEL)


def table(v):
    g = v["visual"]["objects"]["grid"][0]["properties"]
    g["rowPadding"], g["imageHeight"] = lit(f"{PAD}D"), lit(f"{IMG_H}D")
    v["position"]["y"], v["position"]["height"] = TABLE_Y, TABLE_H


def cover(v):
    v["position"]["y"], v["position"]["height"] = round(BODY_TOP - 1, 1), BODY_H + 2


edit(P2 / "visuals" / "tbl_hero" / "visual.json", table)
for n in COVERS:
    edit(P2 / "visuals" / n / "visual.json", cover)

# ---- the two rectangles of the first try go, with their bookmark states and their "no filter" entries
for n in LINES:
    shutil.rmtree(P2 / "visuals" / n, ignore_errors=True)


def without_lines(bm):
    o = bm.get("options", {})
    if "targetVisualNames" in o:
        o["targetVisualNames"] = [n for n in o["targetVisualNames"] if n not in LINES]
    for sec in bm["explorationState"]["sections"].values():
        for n in LINES:
            sec.get("visualContainers", {}).pop(n, None)


def no_entries(page):
    page["visualInteractions"] = [i for i in page["visualInteractions"] if i["target"] not in LINES and i["source"] not in LINES]


for f in sorted((REPORT / "definition" / "bookmarks").glob("*.bookmark.json")):
    edit(f, without_lines)
edit(P2 / "page.json", no_entries)
print(f"f10_rows_centred: row padding {PAD}, images {IMG_H} px, the ten rows from y {BODY_TOP} to {BODY_TOP + BODY_H}; model: {len(changed)} set {changed}, {len(added)} added {added}")
