"""Contest compliance of the entry on paper (doc 20 R-X-2; build step 11 of doc 23). Reads the generated files only.

  1. exactly two visible pages; every other page is a hidden tooltip page;
  2. at least four built-in visual types that draw data (line or area, column, bar, scatter, table), no custom visual;
  3. fonts: every font family named in the report and its theme is one Power BI ships (Segoe UI family);
  4. images: every image is a registered resource inside the report, and no file of the report or measure of the model
     points at a web address (the organisers' workbook URL in the DataFile parameter is the data source, not an image);
  5. provided data only: every M partition reads the DataFile parameter; the generator's own tables are calculated
     from those tables or are typed labels and decision data (listed, so a reader can judge them).

The three checks that need the engine (package A = three moves of which two growth, within the budget, the plan sums to
the budget) are assertions of number_checks.py; the visible growth label and the 2032 ledger are read in the renders.

  python project/tools/compliance_check.py [--out <report.txt>]        exit code 1 when a check fails
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "project" / "pbip" / "GoodnightInn-opzet.Report"
MODEL = ROOT / "project" / "pbip" / "PillowKey.SemanticModel" / "definition"
OUT = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else ROOT / "project" / "analysis" / "output" / "compliance_check.txt"
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# wf_segoe-ui_*: the names Power BI's own font stack gives Segoe UI in the service ("wf_segoe-ui_normal, helvetica, arial, sans-serif")
BUILT_IN_FONTS = {"segoe ui", "segoe ui semibold", "segoe ui light", "segoe ui bold", "wf_segoe-ui_normal", "wf_segoe-ui_semibold", "wf_segoe-ui_light", "wf_segoe-ui_bold",
                  "wf_standard-font", "din", "arial", "helvetica", "sans-serif", "tahoma", "verdana"}
DATA_TYPES = {  # visual type -> the family R-X-2 counts
    "lineChart": "line", "areaChart": "area", "stackedAreaChart": "area", "lineClusteredColumnComboChart": "column", "clusteredColumnChart": "column",
    "columnChart": "column", "clusteredBarChart": "bar", "barChart": "bar", "hundredPercentStackedBarChart": "bar", "scatterChart": "scatter",
    "tableEx": "table", "pivotTable": "table",
}
NOT_DATA = {"textbox", "shape", "image", "actionButton", "card", "cardVisual", "slicer", "advancedSlicerVisual", "basicShape"}
lines, fails = [], 0


def record(ok, title, detail):
    global fails
    fails += 0 if ok else 1
    lines.append(f"  {'ok  ' if ok else 'FAIL'}  {title}: {detail}")


# ---------------------------------------------------------------- 1 · pages
order = json.loads((REPORT / "definition" / "pages" / "pages.json").read_text(encoding="utf-8"))["pageOrder"]
pages = {p: json.loads((REPORT / "definition" / "pages" / p / "page.json").read_text(encoding="utf-8")) for p in order}
visible = [p for p in order if pages[p].get("visibility") != "HiddenInViewMode"]
hidden = [p for p in order if p not in visible]
not_tooltip = [p for p in hidden if pages[p].get("type") != "Tooltip"]
record(len(visible) == 2 and not not_tooltip, "two visible pages, the rest hidden tooltip pages",
       f"visible: {', '.join(pages[p]['displayName'] for p in visible)}; hidden tooltip pages: {', '.join(hidden)}" + (f"; hidden but no tooltip: {not_tooltip}" if not_tooltip else ""))

# ---------------------------------------------------------------- 2 · visual types
types, unknown, texts = {}, set(), []
for p in order:
    for vf in (REPORT / "definition" / "pages" / p / "visuals").glob("*/visual.json"):
        raw = vf.read_text(encoding="utf-8")
        texts.append((vf, raw))
        vt = json.loads(raw)["visual"]["visualType"]
        if vt in DATA_TYPES:
            if p in visible:
                types.setdefault(DATA_TYPES[vt], {}).setdefault(vt, []).append(vf.parent.name)
        elif vt not in NOT_DATA:
            unknown.add(vt)
rep = json.loads((REPORT / "definition" / "report.json").read_text(encoding="utf-8"))
custom = rep.get("publicCustomVisuals", []) + [r for r in rep.get("resourcePackages", []) if r.get("type") == "CustomVisual"]
record(len(types) >= 4 and not unknown and not custom, "four or more built-in visual types on the two pages, no custom visual",
       "; ".join(f"{fam}: " + ", ".join(f"{vt} x{len(v)}" for vt, v in sorted(d.items())) for fam, d in sorted(types.items()))
       + (f"; unknown types {sorted(unknown)}" if unknown else "") + (f"; custom visuals {custom}" if custom else ""))

# ---------------------------------------------------------------- 3 · fonts
theme_files = list((REPORT / "StaticResources").rglob("*.json"))
fonts = {}
for f, raw in texts + [(t, t.read_text(encoding="utf-8")) for t in theme_files]:
    for mt in re.finditer(r'"(?:fontFamily|fontFace)"\s*:\s*(?:"([^"]+)"|\{[^{}]*?"Value"\s*:\s*"\'{0,3}([^"]+?)\'{0,3}")', raw):
        for fam in re.split(r",\s*", (mt.group(1) or mt.group(2)).replace("'", "")):
            fonts.setdefault(fam.strip().lower(), set()).add(Path(f).parent.name if Path(f).name == "visual.json" else Path(f).name)
odd = sorted(f for f in fonts if f not in BUILT_IN_FONTS)
record(not odd, "built-in fonts only", ", ".join(f"{f} ({len(v)} files)" for f, v in sorted(fonts.items())) + (f"; not built in: {odd}" if odd else ""))

# ---------------------------------------------------------------- 4 · images
registered = sorted(p.name for p in (REPORT / "StaticResources" / "RegisteredResources").glob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".svg", ".gif"))
web = []
for f in list(REPORT.rglob("*.json")):
    raw = f.read_text(encoding="utf-8")
    for mt in re.finditer(r"https?://[^\s\"'\\)]+", raw):
        u = mt.group(0)
        if raw[max(0, mt.start() - 14):mt.start()].replace(" ", "").endswith('"$schema":"') or u.startswith("http://www.w3.org/"):
            continue  # the $schema of a file format, an SVG namespace: names, never fetched
        web.append(f"{f.relative_to(REPORT)}: {u}")
model_web = []
for f in MODEL.rglob("*.tmdl"):
    for i, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for mt in re.finditer(r"https?://[^\s\"'\\)]+", ln):
            u = mt.group(0)
            if u.startswith("http://www.w3.org/") or (f.name == "expressions.tmdl" and "datavizcontests.blob.core.windows.net" in u):
                continue
            model_web.append(f"{f.name}:{i}: {u}")
record(not web and not model_web, "embedded images only",
       f"{len(registered)} registered images in the report ({', '.join(registered)}); web addresses in the report: {len(web)}; in the model: {len(model_web)}"
       + ("; " + "; ".join((web + model_web)[:8]) if web or model_web else ""))

# ---------------------------------------------------------------- 5 · provided data only
m_parts, calc, other = [], [], []
for f in sorted((MODEL / "tables").glob("*.tmdl")):
    raw = f.read_text(encoding="utf-8")
    if re.search(r"(?m)^\tpartition .+ = m$", raw):
        if f.stem == "_Measures":
            continue  # the measure table's one-cell placeholder
        (m_parts if "Web.Contents(DataFile)" in raw else other).append(f.stem)
    elif re.search(r"(?m)^\tpartition .+ = calculated$", raw):
        calc.append(f.stem + (" (typed labels or decision data)" if "DATATABLE" in raw else ""))
    else:
        other.append(f.stem)
# build step 12: the submission trim leaves out the organisers' sheets nothing reads (12 of the 16 stay); what counts
# is that every table with a Power Query reads one of the sixteen sheets through DataFile, and nothing else.
ORGANISERS = {"Date", "Region", "Scenario", "Brands", "Hotels", "Renovations", "MonthlyPerformance", "GuestSegments", "BookingChannels", "GuestExperience",
              "GuestComplaints", "InvestmentProjects", "InvestmentProjectProperties", "InvestmentScenarios", "FinanceAssumptions", "FinanceParameters"}
record(bool(m_parts) and set(m_parts) <= ORGANISERS and not other, "provided data only",
       f"{len(m_parts)} tables read the organisers' workbook through the DataFile parameter; {len(calc)} tables are calculated in the model: {', '.join(calc)}"
       + (f"; other sources: {other}" if other else ""))

text = f"compliance_check (R-X-2, files only): {len(lines)} checks, {fails} failed\n\n" + "\n".join(lines) + "\n"
print(text)
OUT.write_text(text, encoding="utf-8")
sys.exit(1 if fails else 0)
