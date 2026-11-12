import json
from pathlib import Path

d = Path(r"E:\PowerBI_Dataviz_WC27\project\pbip\GoodnightInn-opzet.Report\definition\pages\p2-investment-strategy\visuals")


def walk(o, ms, cs):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "Measure" and isinstance(v, dict) and "Property" in v:
                ms.add(v["Property"])
            elif k == "Column" and isinstance(v, dict) and "Property" in v:
                cs.add(v["Property"])
            walk(v, ms, cs)
    elif isinstance(o, list):
        for v in o:
            walk(v, ms, cs)


for v in sorted(d.iterdir()):
    ms, cs = set(), set()
    walk(json.loads((v / "visual.json").read_text(encoding="utf-8")), ms, cs)
    if ms or cs:
        print(v.name, "| M:", sorted(ms), "| C:", sorted(cs))
print(open(r"E:\PowerBI_Dataviz_WC27\project\analysis\output\packages.csv", encoding="utf-8").readline())
