"""Fix round of doc 29 (15 Nov 2026): one page-2 view of the THROWAWAY copy at the two sizes a judge sees it in
(never the project; doc 23 rule 6).

  python shoot.py <pid> <copy dir> <out dir> <name> <state> <scenario> [picked] [--only 1920,1366]

state rec | alts | build (page 2) or p1 (page 1, scenario "-"); scenario Low | Expected | High; picked: the moves of Build your own as short names separated
by semicolons, "-" for nothing picked, left out for the saved selection (package A).

What it writes, per view:
  <name>_1920.png   the page at 100 %: one capture px per page px, as a 1920 px wide browser window draws it
  <name>_1366.png   the page at 64 %: the size Power BI fits the page to in a 1366 px wide window
  <name>_2x.png     the page at 1.84 px per page px, for the small text

How. The session's Desktop window is narrow, so the page is cut into four strips of 480 x 1080 in the copy
(..\\step9\\round.py view, ..\\tiles\\mk_tiles.py) and each strip is captured through the Desktop Bridge at three
device scales: 3 (1.84 px per page px), 1.6327 (1.00) and 1.0442 (0.64). The text is drawn by Desktop at that size,
not resampled from a larger capture. A capture can come too early and miss visuals (step 9 took every strip twice;
in this round both takes of a strip came out without half its visuals, and two takes in a row could miss the same
ones). So the three sizes check each other: a strip must show the same things at all three, and the size that
disagrees is captured again. Use at least two sizes for that reason. Look at every result all the same.

Desktop slows down over a long session: after some forty reloads a capture took 33 s instead of 10 and one of its
processes held 6.5 GB. Close the throwaway window and open the copy again (and refresh the model) when that happens.

Limit. These are renders of Desktop's canvas, not of a browser on the published report: the scale is the one a
1366 px or a 1920 px window gives, the browser's own bar and the service's header strip are not in them. Vertical
seams at page x 480, 960 and 1440 can shift a visual's marks by up to 1.6 px (tiles\\README.txt).
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHOTS = HERE.parent
PY = sys.executable
SCALES = (("2x", "3"), ("1920", "1.6327"), ("1366", "1.0442"))
if "--only" in sys.argv:  # --only 1920,1366: just these sizes (the option and its value come last)
    keep = sys.argv[sys.argv.index("--only") + 1].split(",")
    SCALES = tuple(s_ for s_ in SCALES if s_[0] in keep)
    del sys.argv[sys.argv.index("--only"):]


def run(*a, **k):
    r = subprocess.run([str(x) for x in a], capture_output=True, text=True, encoding="utf-8", errors="replace", **k)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit(f"failed: {a[:3]}")
    return r.stdout.strip()


def coarse(work, c):
    """One strip of a capture as 40 x 90 grey cells of 12 page px: what is on it, whatever the capture's scale."""
    import numpy as np
    from PIL import Image
    x0, x1, y0, y1 = map(int, (work / "t_cal.txt").read_text().split())
    im = Image.open(work / f"t_0_{c}.png").convert("L").crop((x0, y0, x1, y1))
    return np.asarray(im.resize((480, 1080), Image.LANCZOS).resize((40, 90), Image.BOX)).astype(float)


pid, copy, out, name, state, scen = sys.argv[1], sys.argv[2], Path(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
picked = sys.argv[7:8]
out.mkdir(parents=True, exist_ok=True)
if state == "p1":  # final round of 16 Nov: page 1 the same way (it follows no scenario and has one state; give "-" for the scenario)
    run(PY, SHOTS / "tiles" / "mk_tiles.py", Path(copy) / "THROWAWAY.Report", "--page", "p1-brand-review", "--mast", "232", "--rows", "1")
else:
    run(PY, SHOTS / "step9" / "round.py", "view", copy, state, scen, *picked)
run("powerbi-desktop.cmd", "reload", "--pid", pid)
time.sleep(15)
works = {tag: out / "_strips" / f"{name}_{tag}" for tag, _ in SCALES}
caps = {tag: (lambda page, f, scale=scale: run("node", SHOTS / "cap.mjs", pid, page, scale, f)) for tag, scale in SCALES}
for tag, _ in SCALES:
    works[tag].mkdir(parents=True, exist_ok=True)
    caps[tag]("t_cal", works[tag] / "t_cal.png")
    run(PY, SHOTS / "step7" / "find_cal.py", works[tag] / "t_cal.png", works[tag] / "t_cal.txt")
    x0, x1, y0, y1 = map(int, (works[tag] / "t_cal.txt").read_text().split())
    if abs((x1 - x0) / (y1 - y0) - 480 / 1080) > 0.01:  # the session's screen turns now and then (round2d\README.txt)
        raise SystemExit(f"!! {name} {tag}: the strip is not drawn whole ({x1 - x0} x {y1 - y0} px): the screen is wide now; shoot again when it is tall")
    for c in range(4):
        caps[tag](f"t_0_{c}", works[tag] / f"t_0_{c}.png")
# the same strip at every size must show the same things: calibrated on this round's captures, two complete captures
# differ by at most 44 grey levels in any cell when one of them is the 2x (the text is drawn at another size) and by at
# most 31 between 1920 and 1366; a capture that misses a chart or a table by 67 or more, one that misses a single line
# of text by less (the footer "Picked: 3 moves" went missing under a limit of 55)
tags = [t for t, _ in SCALES]
for c in range(4):
    for attempt in range(5):
        cells = {t: coarse(works[t], c) for t in tags}
        off = {t: [abs(cells[t] - cells[u]).max() > (50 if "2x" in (t, u) else 40) for u in tags if u != t] for t in tags}
        odd = [t for t in tags if off[t] and all(off[t])] if len(tags) > 2 else [t for t in tags if any(off[t])]
        if not any(any(v) for v in off.values()):
            break
        again = odd or tags
        print(f"   {name} strip {c}: {', '.join(again)} captured again (a visual was missing in one of the sizes)")
        for t in again:
            caps[t](f"t_0_{c}", works[t] / f"t_0_{c}.png")
    else:
        print(f"!! {name} strip {c}: the sizes still disagree, look at it")
for tag, _ in SCALES:  # the screen may have turned while the strips were taken: the calibration must still hold
    again = works[tag] / "t_cal2.txt"
    caps[tag]("t_cal", works[tag] / "t_cal2.png")
    run(PY, SHOTS / "step7" / "find_cal.py", works[tag] / "t_cal2.png", again)
    if again.read_text() != (works[tag] / "t_cal.txt").read_text():
        raise SystemExit(f"!! {name} {tag}: the canvas changed during the round (the screen turned): shoot again")
for tag, _ in SCALES:
    work = works[tag]
    print(tag, run(PY, SHOTS / "tiles" / "stitch.py", work, work / "t_cal.txt", work / "page.png", "--rows", "1"))
    shutil.copyfile(work / "page.png", out / f"{name}_{tag}.png")
