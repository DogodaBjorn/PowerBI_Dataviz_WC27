"""Every alt text of the report as a screen reader gets it, per case (build step 10 of doc 23; R-X-1, R-P2-9).

Reads the generated report, takes every visual in the tab order of the two report pages and of the tooltip pages, and
prints what its alt text says: a typed text as it is, a measure evaluated by the engine of a running Power BI Desktop
(a THROWAWAY copy, doc 23 rule 6) in Low, Expected and High. The tooltip pages get the context a hover gives them
(package A, the year 2030, the oldest renovation band, the fullest hotel). Flags: a "Never" word of R-G2
(build_checks.NEVER), a colour word, an empty text, more than LIMIT characters (the practice of plan 11 for a chart or a
card; a table's summary, and a card that reads its own sentence, may run longer and are listed, not failed). Page 2 is
read twice: with nothing picked in Build your own, and with package A picked, as the state opens.

  python project/tools/alt_texts.py --port <AS port> [--out <file>]
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "project" / "pbip" / "GoodnightInn-opzet.Report"
PORT = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "0"
OUT = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else ROOT / "project" / "analysis" / "output" / "alt_texts.txt"
LIMIT = 250
CASES = ("Low", "Expected", "High")
GI = 'InvestmentProjects[Brand] = "Goodnight Inn", Brands[Brand] = "Goodnight Inn"'
# the filter context of each page: the page filters of the report pages, the hovered item on a tooltip page
CONTEXT = {
    "p1-brand-review": "",
    "p2-investment-strategy": GI,
    "p2-investment-strategy|Build with package A picked": GI + ', TREATAS ( { "Booking app", "Revenue management", "Kiosks at 20 desks" }, BuildMove[Short Name] )',
    "tt-package": 'TREATAS ( { LOOKUPVALUE ( Package[PackageID], Package[Preset], "A" ) }, Package[PackageID] )',
    "tt-year": "'Date'[Year] = 2030",
    "tt-f3-band": 'Brands[Brand] = "Goodnight Inn", Hotels[Renovation Age Sort] = 3',
    "tt-f4-hotel": 'Brands[Brand] = "Goodnight Inn", TREATAS ( { "GI027" }, Hotels[HotelID] )',
    "tt-glossary": "",
}
NEVER = [r"\bbroken even\b|\bbreaks? even\b|\bbreak-even\b", r"(?<!cash )\bpositive from\b", r"\binitiatives?\b", r"\brun-rate\b", r"\bprofit a year by\b",
         r"\bROI\b|\bIRR\b|\byield\b", r"\bfacts?\b", r"\brenovate\b", r"\bphases?\b|\bwaves?\b", r"\btrigger\b|\brevisit\b"]
COLOUR = r"\b(blue|orange|tangerine|grey|gray|red|green|dark line|coffee blue)\b"

rows = []  # (page, tab, visual, type, kind, text or measure)
for pdir in sorted((REPORT / "definition" / "pages").iterdir()):
    if not pdir.is_dir():
        continue
    for vd in (pdir / "visuals").iterdir():
        v = json.loads((vd / "visual.json").read_text(encoding="utf-8"))
        tab = v["position"].get("tabOrder", 0)
        if tab < 0:
            continue
        g = v["visual"].get("visualContainerObjects", {}).get("general", [{}])[0].get("properties", {}).get("altText")
        e = (g or {}).get("expr", {})
        if "Measure" in e:
            rows.append((pdir.name, tab, v["name"], v["visual"]["visualType"], "measure", e["Measure"]["Property"]))
        else:
            lit = e.get("Literal", {}).get("Value", "")
            rows.append((pdir.name, tab, v["name"], v["visual"]["visualType"], "typed", lit[1:-1].replace("''", "'") if lit else ""))
# a second view of page 2: the Build state as it opens, with package A picked (the first view has nothing picked)
PICKED = "p2-investment-strategy|Build with package A picked"
rows += [(PICKED, *r[1:]) for r in rows if r[0] == "p2-investment-strategy" and r[4] == "measure"]
rows.sort(key=lambda r: (list(CONTEXT).index(r[0]) if r[0] in CONTEXT else 99, -r[1]))  # Tab runs from the highest tabOrder down (step 10)

queries, index = [], []
for page in CONTEXT:
    ms = sorted({r[5] for r in rows if r[0] == page and r[4] == "measure"})
    if not ms:
        continue
    for case in CASES:
        flt = ", ".join(x for x in (f'Scenario[Scenario] = "{case}"', CONTEXT[page]) if x)
        cols = ", ".join(f'"{m}", [{m}]' for m in ms)
        queries.append(f"EVALUATE CALCULATETABLE ( ROW ( {cols} ), {flt} )")
        index.append((page, case))
values = {}
with tempfile.TemporaryDirectory() as td:
    qf, of = Path(td) / "q.dax", Path(td) / "r.json"
    qf.write_text("\n".join(queries), encoding="utf-8")
    run = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / "project" / "tools" / "run_dax.ps1"), "-Port", PORT, "-Query", str(qf), "-Out", str(of)],
                         capture_output=True, text=True)
    if run.returncode:
        sys.exit("run_dax.ps1 failed:\n" + (run.stdout + run.stderr)[-1500:])
    for (page, case), table in zip(index, json.loads(of.read_text(encoding="utf-8-sig"))):
        for k, val in table[0].items():
            values[(page, case, k.strip("[]"))] = val

lines, flags = [], 0
cur = None
for page, tab, name, vtype, kind, what in rows:
    if page != cur:
        lines.append(f"\n=== {page}" + (f"   (context: {CONTEXT.get(page)})" if CONTEXT.get(page) else ""))
        cur = page
    texts = {"": what} if kind == "typed" else {c: values.get((page, c, what)) for c in CASES}
    if page == PICKED and all(texts[c] == values.get(("p2-investment-strategy", c, what)) for c in CASES):
        continue  # the same as with nothing picked
    exp = texts.get("Expected", texts.get(""))
    marks = []
    for c, t_ in texts.items():
        t_ = t_ or ""
        if not t_:
            marks.append(f"EMPTY {c}".strip())
        if any(re.search(p, t_, re.IGNORECASE) for p in NEVER):
            marks.append(f"R-G2 word {c}".strip())
        if re.search(COLOUR, t_, re.IGNORECASE):
            marks.append(f"colour word {c}".strip())
    longest = max(len(t_ or "") for t_ in texts.values())
    if longest > LIMIT:
        # a table's summary and a card that reads its own sentence (no Alt measure) may run longer: listed, not failed
        own = kind == "measure" and not what.startswith("Alt ")
        marks.append(f"long ({longest})" if vtype == "tableEx" or own else f"OVER {LIMIT} ({longest})")
    hard = [m_ for m_ in marks if not m_.startswith("long")]
    flags += len(hard)
    lens = "/".join(str(len(t_ or "")) for t_ in texts.values())
    lines.append(f"{tab:>5} {name} ({vtype}) [{what if kind == 'measure' else 'typed'}] {lens} chars" + (("   <-- " + "; ".join(marks)) if marks else ""))
    lines.append("      " + (exp or "").replace("⁠", ""))
    if kind == "measure":
        for c in ("Low", "High"):
            if texts[c] != exp:
                lines.append(f"      {c}: " + (texts[c] or "").replace("⁠", ""))
head = f"alt_texts: {len(rows)} visuals in the tab order, {sum(1 for r in rows if r[4] == 'measure')} on a measure, {flags} flag(s)"
OUT.write_text(head + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
print(head)
print(f"written: {OUT}")
sys.exit(1 if flags else 0)
