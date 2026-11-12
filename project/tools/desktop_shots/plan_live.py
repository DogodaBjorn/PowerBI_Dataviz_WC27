"""Write steps_live.json for batch 2: real clicks on the canvas (CDP mouse events; Ctrl+click is how Desktop fires a
button in edit mode). Every sequence starts from a fresh reload of the stored file state (landing, A, Expected,
all packages), so an accidental edit-mode move can never carry into the next sequence."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PID = sys.argv[1]
PY = r"C:\Users\TRAINE~1\AppData\Local\Temp\claude\c836afdd204b78b7\52e24e6a-d9ba-4cc6-bc1f-7bdcf2915666\scratchpad\venv\Scripts\python.exe"
REV = HERE / "review2"

BTN = (1488, 988)                      # btn_open_plan and btn_back share this slot (1112,968 752x40)
TILE = {"Low": (1187, 244), "Expected": (1297, 244), "High": (1407, 244)}   # sl_scenario tiles
A_DOT = (270, 434)                     # the raspberry A in batch-2 shot 02 (capex axis to $62M)
DROPDOWN = (1680, 238)                 # sl_package box
VIEW = {"all": (814, 216), "zoom": (970, 216)}  # sl_view tiles
ITEM_JS = ("(() => { const e = [...document.querySelectorAll('.slicerText, .slicerItemContainer, span, div')]"
           ".filter(x => x.children.length === 0 && x.textContent.trim().startsWith('%s'))"
           ".map(x => x.getBoundingClientRect()).filter(r => r.width > 0 && r.height > 0).pop();"
           " return [e.x + Math.min(e.width / 2, 60), e.y + e.height / 2]; })()")


def shot(name):
    return [{"op": "wait", "ms": 6000}, {"op": "pagebox"}, {"op": "pshot", "scale": 1, "out": str(REV / f"{name}.png")}]


def click(xy, ctrl=False, settle=True):
    return [{"op": "pclick", "lx": xy[0], "ly": xy[1], "ctrl": ctrl, "nosettle": not settle}]


def reset():
    cmd = f"& '{PY}' -I '{HERE / 'make_variant.py'}' shortlist A Expected p2 all | Out-Null; powerbi-desktop reload --pid {PID} --wait-seconds 180"
    return [{"op": "sh", "cmd": cmd}, {"op": "wait", "ms": 12000}]


steps = [{"op": "metrics", "w": 2356, "h": 1400, "dsf": 1}, {"op": "wait", "ms": 2000}]
# L1: the button round trip (test 1 and 3, package A)
steps += reset() + shot("L1a_live_landing_A_before-click")
steps += click(BTN, ctrl=True) + shot("L1b_live_after-ctrl-click-Open-the-plan")
steps += click(BTN, ctrl=True) + shot("L1c_live_after-ctrl-click-Back")
# L2: change the scenario by clicking its tile, then the round trip (does the plan follow the scenario?)
steps += reset() + click(TILE["High"]) + shot("L2a_live_clicked-High-tile")
steps += click(BTN, ctrl=True) + shot("L2b_live_High_after-Open-the-plan")
steps += click(BTN, ctrl=True) + shot("L2c_live_High_after-Back")
# L3: pick C in the dropdown, open the plan, come back (does C survive the round trip? the Back hover state)
steps += reset() + click(DROPDOWN, settle=False) + shot("L3a_live_dropdown-open")
steps += [{"op": "tab", "js": ITEM_JS % "C · Refresh"}] + shot("L3b_live_picked-C-in-dropdown")
steps += click(BTN, ctrl=True) + shot("L3c_live_C_after-Open-the-plan")
steps += click(BTN, ctrl=True) + shot("L3d_live_C_after-Back")
# L4 (test 4): click the A dot, then swap layouts
steps += reset() + click(A_DOT, settle=False) + shot("L4a_live_clicked-scatter-point-A")
steps += click(BTN, ctrl=True) + shot("L4b_live_after-Open-the-plan-with-point-selected")
steps += click(BTN, ctrl=True) + shot("L4c_live_after-Back")
# L5: the scatter view switch (Björn 7 Nov), then back
steps += reset() + click(VIEW["zoom"]) + shot("L5a_live_clicked-Zoom-on-A-B-C")
steps += click(VIEW["all"]) + shot("L5b_live_clicked-All-packages")
(HERE / "steps_live.json").write_text(json.dumps(steps, indent=1), encoding="utf-8")
print(len(steps), "steps")
