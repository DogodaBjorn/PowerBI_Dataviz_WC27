"""Write steps_static.json for batch 2: every fixed state, built from the stored bookmark + slicer values, reloaded
through the Desktop Bridge and captured at 1x (exactly 1920 x 1080) and 2x inside one DevTools session.
usage: python plan_static.py <pid> [comma-separated state numbers]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PID = sys.argv[1]
PY = r"C:\Users\TRAINE~1\AppData\Local\Temp\claude\c836afdd204b78b7\52e24e6a-d9ba-4cc6-bc1f-7bdcf2915666\scratchpad\venv\Scripts\python.exe"
REV = HERE / "review3"
RAW = HERE / "raw3x"
REV.mkdir(exist_ok=True)
RAW.mkdir(exist_ok=True)

STATES = [  # name, state, focus, scenario, page, scatter view
    ("01_P1_brand-review", "shortlist", "A", "Expected", "p1", "all"),
    ("02_P2_landing_A_Expected", "shortlist", "A", "Expected", "p2", "all"),
    ("03_P2_landing_A_Low", "shortlist", "A", "Low", "p2", "all"),
    ("04_P2_landing_A_High", "shortlist", "A", "High", "p2", "all"),
    ("05_P2_landing_focusB_Expected", "shortlist", "B", "Expected", "p2", "all"),
    ("06_P2_landing_focusC_Expected", "shortlist", "C", "Expected", "p2", "all"),
    ("07_P2_landing_A_Expected_zoom", "shortlist", "A", "Expected", "p2", "zoom"),
    ("08_P2_plan_A_Expected", "plan", "A", "Expected", "p2", "all"),
    ("09_P2_plan_A_Low", "plan", "A", "Low", "p2", "all"),
    ("10_P2_plan_A_High", "plan", "A", "High", "p2", "all"),
    ("11_P2_plan_B_Expected", "plan", "B", "Expected", "p2", "all"),
    ("12_P2_plan_C_Expected", "plan", "C", "Expected", "p2", "all"),
    ("13_P2_plan_C_Low", "plan", "C", "Low", "p2", "all"),
    ("14_P2_plan_B_Low", "plan", "B", "Low", "p2", "all"),
    ("15_P2_landing_focusC_Low_zoom", "shortlist", "C", "Low", "p2", "zoom"),
]

ONLY = sys.argv[2].split(",") if len(sys.argv) > 2 else None
# A bridge reload keeps the page that is open (pages.json activePageName only counts on open), so the page is chosen
# by clicking its tab in the canvas, once, before the first state on that page.
TAB = {"p1": "The Brand Review", "p2": "The Investment Strategy"}
TAB_JS = ("(() => { const e = [...document.querySelectorAll('.textLabel')].find(x => x.textContent.trim() === '%s');"
          " const r = e.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })()")
steps = [{"op": "metrics", "w": 2356, "h": 1400, "dsf": 1}, {"op": "wait", "ms": 2000}]
current = None
for name, state, focus, scen, page, view in STATES:
    if ONLY and name[:2] not in ONLY:
        continue
    cmd = (f"& '{PY}' -I '{HERE / 'make_variant.py'}' {state} {focus} {scen} {page} {view} | Out-Null; "
           f"powerbi-desktop reload --pid {PID} --wait-seconds 180")
    steps += [{"op": "sh", "cmd": cmd}, {"op": "wait", "ms": 12000}]
    if page != current:
        steps += [{"op": "tab", "js": TAB_JS % TAB[page]}, {"op": "wait", "ms": 6000}]
        current = page
    steps += [{"op": "pagebox"},
              {"op": "pshot", "scale": 1, "out": str(REV / f"{name}.png")},
              {"op": "pshot", "scale": 2, "out": str(RAW / f"{name}@2x.png")}]
(HERE / "steps_static3.json").write_text(json.dumps(steps, indent=1), encoding="utf-8")
print(sum(1 for s in steps if s["op"] == "pshot") // 2, "states")
