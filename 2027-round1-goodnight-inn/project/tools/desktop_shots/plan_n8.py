import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
REV = HERE / "review3"
TAB_JS = ("(() => { const e = [...document.querySelectorAll('.textLabel')].find(x => x.textContent.trim() === 'The Investment Strategy');"
          " const r = e.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; })()")
steps = [{"op": "metrics", "w": 2356, "h": 1400, "dsf": 1}, {"op": "wait", "ms": 3000}, {"op": "tab", "js": TAB_JS}, {"op": "wait", "ms": 6000}, {"op": "pagebox"},
         {"op": "pclick", "lx": 1488, "ly": 980, "ctrl": True}, {"op": "wait", "ms": 2500},
         {"op": "phover", "lx": 600, "ly": 1060, "from": 0}, {"op": "wait", "ms": 1500},
         {"op": "phover", "lx": 1488, "ly": 1050, "from": 0}, {"op": "wait", "ms": 400},
         {"op": "phover", "lx": 1488, "ly": 982, "from": 0}, {"op": "wait", "ms": 2000},
         {"op": "pshot", "scale": 1, "out": str(REV / "L2b_mouse-on-Back.png")},
         {"op": "phover", "lx": 1488, "ly": 1050, "from": 0}, {"op": "wait", "ms": 400},
         {"op": "phover", "lx": 1300, "ly": 928, "from": 0}, {"op": "wait", "ms": 2000},
         {"op": "pshot", "scale": 1, "out": str(REV / "L2c_mouse-on-risk-line.png")}]
(HERE / "steps_n8.json").write_text(json.dumps(steps, indent=1), encoding="utf-8")
