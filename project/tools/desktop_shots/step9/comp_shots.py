"""The comp at page pixels for the Build views (build step 9 of doc 23): one PNG of 1920 x 1080 per view.

usage: python comp_shots.py <out dir> [view ...]        views: see VIEWS (default: all)

A scratch copy of project/design-prototypes/rebuild-comp-v10.html reads the scenario and the picked moves from the query
string (?scen=Low&picked=GI-01,GI-10), nothing else changes. Headless Edge at --window-size=1952,1300 puts the page at
(16, 94) at scale 1 (tiles/README.txt); Edge returns before the PNG exists, so the script waits for the file.
"""
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
COMP = ROOT / "project" / "design-prototypes" / "rebuild-comp-v10.html"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
A = "GI-01,GI-10,GI-02"
# view -> (state, scenario, picked ProjectIDs or None for the comp's own opening selection)
VIEWS = {
    "build_Low": ("build", "Low", None), "build_Expected": ("build", "Expected", None), "build_High": ("build", "High", None),
    "build_none": ("build", "Expected", ""),                    # nothing picked
    "build_over": ("build", "Expected", "GI-03,GI-07,GI-08"),   # energy + refresh + Boston: over the budget
    "build_rule": ("build", "Expected", "GI-02,GI-09,GI-10"),   # kiosks without the app: a broken rule
    "build_six": ("build", "Expected", "GI-01,GI-10,GI-02,GI-09,GI-05,GI-04"),  # six moves: the bars share the plot
    "alts_Expected": ("alts", "Expected", None), "rec_Expected": ("rec", "Expected", None),
}

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
src = COMP.read_text(encoding="utf-8")
old = "const ST = {page:'p1', state:'rec', scen:'Expected', picked:new Set(A.ids), slots:false};"
assert old in src
new = ("const QS = new URLSearchParams(location.search);\n"
       "const ST = {page:'p1', state:'rec', scen:(QS.get('scen') || 'Expected'), "
       "picked:new Set(QS.has('picked') ? QS.get('picked').split(',').filter(Boolean) : A.ids), slots:false};")
scratch = out / "comp_scratch.html"
scratch.write_text(src.replace(old, new), encoding="utf-8")
for view in (sys.argv[2:] or list(VIEWS)):
    state, scen, picked = VIEWS[view]
    url = scratch.resolve().as_uri() + f"?scen={scen}" + ("" if picked is None else f"&picked={picked}") + f"#{state}"
    raw = out / f"_{view}.png"
    raw.unlink(missing_ok=True)
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1952,1300", f"--user-data-dir={out / '_edge'}",
                    f"--screenshot={raw}", url], capture_output=True, timeout=120)
    for _ in range(60):
        if raw.exists() and raw.stat().st_size > 0:
            break
        time.sleep(0.5)
    time.sleep(0.5)
    Image.open(raw).convert("RGB").crop((16, 94, 16 + 1920, 94 + 1080)).save(out / f"comp_{view}.png")
    raw.unlink()
    print("comp", view, "->", out / f"comp_{view}.png")
