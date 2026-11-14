"""Build step 12 of doc 23: write the step files web.mjs runs on the published report.

usage: python plan.py <out dir> <run> [tag]
  run = p1       page 1: capture, the two page tooltips, the glossary, a visual header, the texts
        p2       page 2 through the Next button: Recommended in Expected, Low, High, the package and year tooltips
        states   page 2: What waits and Build through their tabs, a selector tile, the invitation, Back
        keys     Tab from the top of page 1: what takes the focus, ten stops
        touch    taps instead of clicks: Next, a tab, a scenario pill, a tooltip target
Coordinates are the report's own 1920 x 1080 (slot map v10), so the same plan runs in any window size.
"""
import json
import sys
from pathlib import Path

OUT, RUN = Path(sys.argv[1]), sys.argv[2]
TAG = sys.argv[3] if len(sys.argv) > 3 else "en"
OUT.mkdir(parents=True, exist_ok=True)
f = lambda name: str(OUT / f"{TAG}_{name}").replace("\\", "/")

NEXT, BACK = (1552, 1058), (836, 30)
TAB = {"rec": (1332, 80), "alts": (1556, 80), "build": (1780, 80)}
SCEN = {"Low": (1648, 128), "Expected": (1744, 128), "High": (1840, 128)}
steps = [{"op": "ready"}, {"op": "meta"}, {"op": "wait", "ms": 3000}]
wait = lambda ms=2500: steps.append({"op": "wait", "ms": ms})
shot = lambda name: steps.append({"op": "pshot", "out": f(name + ".png")})
full = lambda name: steps.append({"op": "shot", "out": f(name + ".png")})


def hover(name, x, y, whole=True):
    steps.append({"op": "pmove", "lx": x - 6, "ly": y - 4}); wait(300)
    steps.append({"op": "pmove", "lx": x, "ly": y}); wait(2500)
    (full if whole else shot)(name)
    steps.append({"op": "pmove", "lx": 1900, "ly": 140}); wait(600)


def click(xy, ms=4000, op="pclick"):
    steps.append({"op": op, "lx": xy[0], "ly": xy[1]}); wait(ms)


if RUN == "p1":
    shot("p1"); steps.append({"op": "texts", "out": f("p1.txt")})
    hover("p1_tt_f3_oldest", 1770, 525)
    hover("p1_tt_f4_toronto", 1735, 891)
    hover("p1_tt_glossary", 1816, 1058)
    hover("p1_tag_f3", 1792, 338)
    hover("p1_header_f1", 300, 520)
elif RUN == "p2":
    click(NEXT, 7000); shot("p2_rec_expected"); steps.append({"op": "texts", "out": f("p2_rec_expected.txt")})
    hover("p2_tt_chip_a", 1132, 200)
    hover("p2_tt_hero_row", 300, 300)
    hover("p2_tt_year", 1500, 900)
    hover("p2_tt_glossary", 1816, 1058)
    for s in ("Low", "High"):
        click(SCEN[s], 5000); shot(f"p2_rec_{s.lower()}"); steps.append({"op": "texts", "out": f(f"p2_rec_{s.lower()}.txt")})
    click(SCEN["Expected"], 4000); shot("p2_rec_expected_again")
elif RUN == "states":
    click(NEXT, 7000)
    click(TAB["alts"], 5000); shot("p2_alts"); steps.append({"op": "texts", "out": f("p2_alts.txt")})
    hover("p2_alts_tt_dot", 392, 440)
    click(TAB["build"], 5000); shot("p2_build"); steps.append({"op": "texts", "out": f("p2_build.txt")})
    click((900, 500), 5000); shot("p2_build_tile_clicked")
    click(TAB["rec"], 5000); shot("p2_rec_back")
    click((1696, 626), 5000); shot("p2_invite_clicked")
    click(BACK, 6000); shot("p1_after_back")
elif RUN == "more":
    hover("p1_tt_f4_free_dot", 1680, 880)
    click(NEXT, 7000); click(TAB["alts"], 5000)
    hover("p2_alts_tt_a", 188, 345); hover("p2_alts_tt_c", 465, 448); hover("p2_alts_tt_grey", 315, 394)
    hover("p2_alts_tt_year", 1055, 860)
    click(TAB["build"], 5000); hover("p2_build_tt_you", 188, 300)
    click((900, 520), 5000); shot("p2_build_tile8"); click((900, 520), 5000); shot("p2_build_tile8_off")
elif RUN == "clicks":  # a click on a mark or a row must not change any other visual (cross-filter, cross-highlight)
    def probe(name, x, y, reset):
        shot(name + "_before"); click((x, y), 3500); steps.append({"op": "pmove", "lx": 1900, "ly": 140}); wait(800); shot(name + "_after")
        click((x, y), 3500); steps.append({"op": "pmove", "lx": 1900, "ly": 140}); wait(800)
    probe("ck_p1_f3_bar", 1770, 525, None); probe("ck_p1_f4_dot", 1680, 880, None); probe("ck_p1_folio_row", 760, 620, None); probe("ck_p1_f1_area", 284, 560, None)
    click(NEXT, 7000)
    probe("ck_rec_hero_row", 300, 322, None); probe("ck_rec_ledger_row", 1300, 460, None); probe("ck_rec_plan_bar", 1100, 800, None); probe("ck_rec_cum_line", 1500, 900, None)
    click(TAB["alts"], 5000)
    probe("ck_alts_waits_row", 1000, 440, None); probe("ck_alts_cmp_line", 1055, 800, None); probe("ck_alts_dot_a", 188, 345, None); probe("ck_alts_grey", 315, 394, None)
    click(TAB["build"], 5000)
    probe("ck_build_moves_row", 1150, 330, None); probe("ck_build_bar", 1680, 482, None); probe("ck_build_cmp", 1055, 860, None)
elif RUN == "tips":  # the tooltips again, for the 1366 px window
    hover("p1_tt_f3_oldest", 1770, 525); hover("p1_tt_f4_free_dot", 1680, 880); hover("p1_tt_glossary", 1816, 1058)
    click(NEXT, 7000); shot("p2_rec"); hover("p2_tt_year", 1500, 900)
    click(TAB["alts"], 5000); hover("p2_alts_tt_a", 188, 345)
elif RUN == "keys":
    # the embed takes Tab for its own chrome first; Ctrl+Enter on the report enters it
    steps.append({"op": "key", "key": "Tab"}); wait(400); steps.append({"op": "focus"})
    steps.append({"op": "key", "key": "Enter", "ctrl": True}); wait(800); steps.append({"op": "focus"})
    for i in range(14):
        steps.append({"op": "key", "key": "Tab"}); wait(400); steps.append({"op": "focus"})
    full("p1_tab14")
elif RUN == "touch":
    click(NEXT, 7000, "ptap"); shot("touch_p2")
    click(TAB["alts"], 5000, "ptap"); shot("touch_alts")
    click(SCEN["Low"], 5000, "ptap"); shot("touch_alts_low")
    click((392, 440), 3000, "ptap"); full("touch_dot")
    click(BACK, 6000, "ptap"); shot("touch_back")
else:
    sys.exit("unknown run " + RUN)
out = OUT / f"{TAG}_{RUN}.json"
out.write_text(json.dumps(steps, indent=0), encoding="utf-8")
print(out)
