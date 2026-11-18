"""Live sequences for batch 3: hover tooltips (A, B, C, a cloud dot), the Back-button hover (N8), the scenario and view
tiles, the dropdown. Each sequence starts from a fresh reload of state 02.  usage: python plan_live3.py <pid>"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
PID = sys.argv[1]
PY = r"C:\Users\TRAINE~1\AppData\Local\Temp\claude\c836afdd204b78b7\52e24e6a-d9ba-4cc6-bc1f-7bdcf2915666\scratchpad\venv\Scripts\python.exe"
REV = HERE / "review3"
RESET = {"op": "sh", "cmd": f"& '{PY}' -I '{HERE / 'make_variant.py'}' shortlist A Expected p2 all | Out-Null; powerbi-desktop reload --pid {PID} --wait-seconds 180"}
TAB_JS = ("(() => { const e = [...document.querySelectorAll('.textLabel')].find(x => x.textContent.trim() === 'The Investment Strategy');"
          " const r = e.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })()")
ITEM_JS = ("(() => { const e = [...document.querySelectorAll('span,div')].filter(x => x.childElementCount === 0 && x.textContent.trim() === '%s').pop();"
           " const r = e.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })()")
def shot(n): return [{"op": "wait", "ms": 2500}, {"op": "pshot", "scale": 1, "out": str(REV / f"{n}.png")}]
def reset(): return [RESET, {"op": "wait", "ms": 12000}, {"op": "pagebox"}]
steps = [{"op": "metrics", "w": 2356, "h": 1400, "dsf": 1}, {"op": "wait", "ms": 2000}, {"op": "tab", "js": TAB_JS}, {"op": "wait", "ms": 5000}]
# L1 tooltips: A, B, C and one cloud dot (positions from render 02, logical page px)
steps += reset()
for n, (x, y) in (("L1a_hover-A", (209, 378)), ("L1b_hover-B", (244, 384)), ("L1c_hover-C", (637, 624)), ("L1d_hover-cloud-dot", (552, 492))):
    steps += [{"op": "phover", "lx": 1400, "ly": 1020, "from": 0}, {"op": "wait", "ms": 600}, {"op": "phover", "lx": x, "ly": y}] + shot(n)
# L2 the plan state, the mouse on Back (N8), then on the risk line, then Back
steps += reset()
steps += [{"op": "pclick", "lx": 1488, "ly": 980, "ctrl": True}] + shot("L2a_ctrl-click-Open-the-plan")
steps += [{"op": "phover", "lx": 1488, "ly": 980}] + shot("L2b_mouse-on-Back")
steps += [{"op": "phover", "lx": 1300, "ly": 928}] + shot("L2c_mouse-on-risk-line")
steps += [{"op": "pclick", "lx": 1488, "ly": 980, "ctrl": True}] + shot("L2d_ctrl-click-Back")
# L3 the scenario tiles
steps += reset()
steps += [{"op": "pclick", "lx": 1420, "ly": 244}] + shot("L3a_clicked-High")
steps += [{"op": "pclick", "lx": 1170, "ly": 244}] + shot("L3b_clicked-Low")
# L4 the dropdown: C
steps += reset()
steps += [{"op": "pclick", "lx": 1680, "ly": 244, "nosettle": True}] + shot("L4a_dropdown-open")
steps += [{"op": "tab", "js": ITEM_JS % "C · Why not renovate? For comparison", "nosettle": True}] + shot("L4b_picked-C")
steps += [{"op": "pclick", "lx": 1488, "ly": 980, "ctrl": True}] + shot("L4c_C_ctrl-click-Open-the-plan")
# L5 the view toggle
steps += reset()
steps += [{"op": "pclick", "lx": 958, "ly": 212}] + shot("L5a_clicked-Zoom")
steps += [{"op": "phover", "lx": 1400, "ly": 1020, "from": 0}, {"op": "wait", "ms": 600}]
steps += [{"op": "pclick", "lx": 778, "ly": 212}] + shot("L5b_clicked-All")
(HERE / "steps_live3.json").write_text(json.dumps(steps, indent=1), encoding="utf-8")
print(sum(1 for s in steps if s["op"] == "pshot"), "shots")
