"""Two renders at 1366 px page width (08-verbeterplan R4): the landing and the plan state.  usage: python plan_1366.py <pid>"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
PID = sys.argv[1]
PY = r"C:\Users\TRAINE~1\AppData\Local\Temp\claude\c836afdd204b78b7\52e24e6a-d9ba-4cc6-bc1f-7bdcf2915666\scratchpad\venv\Scripts\python.exe"
REV = HERE / "review3"
TAB_JS = ("(() => { const e = [...document.querySelectorAll('.textLabel')].find(x => x.textContent.trim() === 'The Investment Strategy');"
          " const r = e.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })()")
steps = [{"op": "metrics", "w": 1802, "h": 1250, "dsf": 1}, {"op": "wait", "ms": 2000}]
for i, (state, name) in enumerate((("shortlist", "W1366a_P2_landing_A_Expected"), ("plan", "W1366b_P2_plan_A_Expected"), ("shortlist", "W1366c_P1_brand-review"))):
    page = "p1" if "P1" in name else "p2"
    steps += [{"op": "sh", "cmd": f"& '{PY}' -I '{HERE / 'make_variant.py'}' {state} A Expected {page} all | Out-Null; powerbi-desktop reload --pid {PID} --wait-seconds 180"},
              {"op": "wait", "ms": 12000}]
    if i == 0:
        steps += [{"op": "tab", "js": TAB_JS}, {"op": "wait", "ms": 5000}]
    if page == "p1":
        steps += [{"op": "tab", "js": TAB_JS.replace("The Investment Strategy", "The Brand Review")}, {"op": "wait", "ms": 5000}]
    steps += [{"op": "pagebox"}, {"op": "pshot", "scale": 1, "out": str(REV / f"{name}.png")}]
(HERE / "steps_1366.json").write_text(json.dumps(steps, indent=1), encoding="utf-8")
print("ok")
