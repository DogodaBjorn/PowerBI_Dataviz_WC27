"""Build checks of the FinalV3 rebuild (doc 21 P-8, doc 23 step 4): run after every generator run.

  1. every measure and column the report binds exists in the model (would have caught TT Payback Color);
  2. no visible string carries a "Never" word of R-G2 (strict for the rebuilt copy; reported, not failed, for the old
     report and the old measures, which steps 5 to 11 replace and prune);
  3. no text measure prints money in $M with two decimals (fm's own two-decimal branch below $0.05M is the named
     exception, and so are the folio's per-night dollars);
  4. exactly one measure holds the release rule (Gate Rule (text)), and no other measure or text box contains
     "release", "revisit" or "broken even";
  5. every text measure of sketch_model.TEXT_SLOTS, evaluated in Low, Expected and High (and Build with nothing picked),
     equals the approved text of design-prototypes/rebuild-v10-spec.json -> text (U+2060 stripped first).

Checks 1 to 4 read the files only. Check 5 asks a running Desktop that has the model open and refreshed (in practice the
throwaway copy) through run_dax.ps1:
    python project/tools/build_checks.py [--port <AS port>] [--static] [--out <report.txt>]
--static skips check 5. Exit code 1 when a check fails; differences that are an open question for Bjorn are KNOWN.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import sketch_model as sm  # noqa: E402  (the measures as the generator writes them, and the slot map of the text)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


PORT = int(arg("--port", "0"))
STATIC = "--static" in sys.argv
OUT = Path(arg("--out", str(ROOT / "project" / "analysis" / "output" / "build_checks.txt")))
MODEL = ROOT / "project" / "pbip" / "PillowKey.SemanticModel" / "definition"
REPORT = ROOT / "project" / "pbip" / "GoodnightInn-opzet.Report" / "definition"
SPEC = json.loads((ROOT / "project" / "design-prototypes" / "rebuild-v10-spec.json").read_text(encoding="utf-8"))["text"]
WJ = "⁠"
A_IDS = ["GI-01", "GI-02", "GI-10"]  # package A, the opening selection of Build your own (doc 22: the Build views)
# open question 1 of doc 23: the kiosks' Expected 'a year on cost' is exactly 20.55 %; the spec prints 20.5 (the browser's
# rounding), the model 20.6 (Power BI's). Bjorn decides; until then this one difference is expected wherever it shows.
KNOWN = [("P2 rec Expected", "c_hero_title", "20.5%", "20.6%"), ("P2 rec Expected", "tbl_hero", "20.5%", "20.6%")]

results = []  # (check, key, state, detail)


def record(check, key, ok, detail=""):
    results.append((check, key, "ok" if ok else "FAIL", detail))


def dax_literals(dax):
    return [s.replace('""', '"') for s in re.findall(r'"((?:[^"]|"")*)"', dax)]


TEXT_MEASURES = [(n, d) for n, d, f, *_ in sm.MEASURES if f == sm.TXT]


# ---------------------------------------------------------------- the model and the report on disk
def tmdl_name(raw):
    raw = raw.strip()
    return raw[1:-1].replace("''", "'") if raw.startswith("'") else raw


model = {}  # table -> {"measures": set, "columns": set}
for f in (MODEL / "tables").glob("*.tmdl"):
    tbl = None
    for line in f.read_text(encoding="utf-8").splitlines():
        mt = re.match(r"^table\s+(.+?)\s*$", line)
        if mt:
            tbl = tmdl_name(mt.group(1))
            model[tbl] = {"measures": set(), "columns": set()}
        mm = re.match(r"^\t(measure|column)\s+('(?:[^']|'')*'|[^\s=]+)", line)
        if mm and tbl:
            model[tbl][mm.group(1) + "s"].add(tmdl_name(mm.group(2)))
all_measures = set().union(*(t["measures"] for t in model.values()))
all_columns = set().union(*(t["columns"] for t in model.values()))


def walk(node, refs, texts):
    if isinstance(node, dict):
        for kind in ("Measure", "Column"):
            v = node.get(kind)
            if isinstance(v, dict) and "Property" in v and isinstance(v.get("Expression"), dict):
                sr = v["Expression"].get("SourceRef", {})
                refs.append((kind, sr.get("Entity"), v["Property"]))
        lit = node.get("Literal")
        if isinstance(lit, dict) and isinstance(lit.get("Value"), str) and lit["Value"].startswith("'") and lit["Value"].endswith("'"):
            texts.append(lit["Value"][1:-1].replace("''", "'"))
        if "textStyle" in node and isinstance(node.get("value"), str):  # a text box run
            texts.append(node["value"])
        for v in node.values():
            walk(v, refs, texts)
    elif isinstance(node, list):
        for v in node:
            walk(v, refs, texts)


refs, report_texts, files = [], [], 0
for f in REPORT.rglob("*.json"):
    files += 1
    walk(json.loads(f.read_text(encoding="utf-8")), refs, report_texts)

# ---------------------------------------------------------------- 1 · every bound measure and column exists
missing = sorted({(k, e, p) for k, e, p in refs
                  if not ((e in model and p in model[e][k.lower() + "s"]) if e else p in (all_measures if k == "Measure" else all_columns))})
record("1 bound fields exist", f"{len(refs)} references in {files} report files", not missing, "; ".join(f"{k} {e}[{p}]" for k, e, p in missing))

# ---------------------------------------------------------------- 2 · R-G2: no "Never" word in a visible string
NEVER = [  # (pattern, the R-G2 term to use)
    (r"\bbroken even\b|\bbreaks? even\b|\bbreak-even\b|\bbreaking even\b", "pays back by 2032 / cash positive from"),
    (r"(?<!cash )\bpositive from\b", "cash positive from"),
    (r"\binitiatives?\b", "moves"),
    (r"\brun-rate\b", "a year by 2032"),
    (r"\bprofit a year by\b", "a year by 2032"),
    (r"\bROI\b|\bIRR\b|\byield\b", "a year on cost"),
    (r"\bfacts?\b", "findings"),
    (r"\brenovate\b", "the refresh"),
    (r"\bphases?\b|\bwaves?\b", "tranche"),
    (r"\btrigger\b|\brevisit\b", "the 2028 gate"),
]
# "plan" for a set of moves is not machine-checkable: the approved copy uses it for the capital plan ("The $60M plan")


def never_hits(text):
    return [(pat, term) for pat, term in NEVER if re.search(pat, text, flags=re.IGNORECASE)]


rebuilt = set()
for group in sm.TEXT_SLOTS.values():
    for spec in group.values():
        for x in (spec if isinstance(spec, list) else spec.get("cols", []) if isinstance(spec, dict) else [spec]):
            for y in (x if isinstance(x, list) else [x]):
                if isinstance(y, str) and not y.startswith("=") and "[" not in y:
                    rebuilt.add(y)
txt = dict(TEXT_MEASURES)
strict = [(n, lit, pat) for n in sorted(rebuilt) for lit in dax_literals(txt.get(n, "")) for pat, _ in never_hits(lit)]
record("2 R-G2 vocabulary, rebuilt copy (strict)", f"{len(rebuilt)} text measures of the slot map", not strict,
       "; ".join(f"{n}: '{lit[:60]}'" for n, lit, _ in strict))
old_m = sorted({n for n, d in TEXT_MEASURES if n not in rebuilt and any(never_hits(lit) for lit in dax_literals(d))})
old_r = sorted({t for t in report_texts if never_hits(t)})
results.append(("2 R-G2 vocabulary, old report and old measures (open until step 11)", f"{len(old_m)} measures, {len(old_r)} report strings", "open",
                "; ".join(old_m[:40]) + (" | report: " + "; ".join(old_r[:20]) if old_r else "")))

# ---------------------------------------------------------------- 3 · no money in $M with two decimals
FM_EXCEPTION = 'IF ( __r1 = 0 && __r2 > 0, FORMAT ( __r2, "0.00", "en-US" )'  # fm / sfm: two decimals only below $0.05M
two_dec = []
for n, d in TEXT_MEASURES:
    body = d.replace(FM_EXCEPTION, "")
    if '"$#,0.0#"' in body:
        two_dec.append(n)
        continue
    for mt in re.finditer(r'"((?:[^"]|"")*)"', body):  # the string literals, in order (a format string is one of them)
        if not re.search(r"0\.0[0#]", mt.group(1)):
            continue
        after = body[mt.end():mt.end() + 40]
        if "M" in mt.group(1) or re.match(r'\s*(?:,\s*"[^"]*"\s*)?\)\s*&\s*"M', after):
            two_dec.append(n)
            break
record("3 no two-decimal $M in a text measure", f"{len(TEXT_MEASURES)} text measures", not two_dec, "; ".join(two_dec))

# ---------------------------------------------------------------- 4 · one release rule
RULE = r"\breleases?\b"
OTHER = r"\breleases?\b|\brevisit\b(?! the facts\b)|\bbroken even\b"  # 'Revisit the facts': the old pill's label, no rule (gone in step 6)
holders = sorted({n for n, d, *_ in sm.MEASURES if any(re.search(RULE, lit, re.IGNORECASE) for lit in dax_literals(d))})
others = sorted({n for n, d, *_ in sm.MEASURES if n != "Gate Rule (text)" and any(re.search(OTHER, lit, re.IGNORECASE) for lit in dax_literals(d))})
rep = sorted({t for t in report_texts if re.search(OTHER, t, re.IGNORECASE)})
record("4 one release rule", "Gate Rule (text)", holders == ["Gate Rule (text)"] and not others and not rep,
       f"holders {holders}; other measures {others}; report strings {rep}")

# ---------------------------------------------------------------- 5 · the text measures against the approved text
VIEWS = [("P1", "P1", "Expected", False)] + [(f"P2 {g} {s}", g, s, g == "build") for g in ("rec", "alts", "build") for s in ("Low", "Expected", "High")] \
    + [("P2 build Expected, nothing picked", "build", "Expected", False)]


def measures_of(spec):
    out = []
    for x in (spec if isinstance(spec, list) else [spec]):
        for y in (x if isinstance(x, list) else [x]):
            if isinstance(y, str) and not y.startswith("="):
                out.append(y)
    return out


def filters(scn, picked):
    f = [f'TREATAS ( {{ "{scn}" }}, Scenario[Scenario] )']
    if picked:
        f.append("TREATAS ( { " + ", ".join(f'"{p}"' for p in A_IDS) + " }, BuildMove[ProjectID] )")
    return f


if not STATIC:
    queries, plan = [], []  # plan: (view, slot, kind, query index)
    for view, group, scn, picked in VIEWS:
        slots = {k: v for k, v in sm.TEXT_SLOTS[group].items() if k.split(".")[0] in SPEC[view]}
        scal = sorted({mn for k, v in slots.items() if not isinstance(v, dict) for mn in measures_of(v)})
        queries.append("EVALUATE CALCULATETABLE ( ROW ( " + ", ".join(f'"{mn}", [{mn}]' for mn in scal) + " ), " + ", ".join(filters(scn, picked)) + " )")
        plan.append((view, None, "scalars", len(queries) - 1))
        for k, v in slots.items():
            if isinstance(v, dict):
                cols = [c for c in v["cols"] if c and "[" not in c]
                fl = filters(scn, picked and not v.get("unfiltered")) + ([v["filter"]] if v.get("filter") else []) \
                    + (['TREATAS ( { "Goodnight Inn" }, Brands[Brand] )'] if k == "tbl_f2_folio" else [])
                queries.append(f"EVALUATE SUMMARIZECOLUMNS ( {v['rows']}, {v['sort']}, " + ", ".join(fl) + ", " + ", ".join(f'"{c}", [{c}]' for c in cols) + " )")
                plan.append((view, k, "table", len(queries) - 1))
    with tempfile.TemporaryDirectory() as td:
        qf, rf = Path(td) / "q.dax", Path(td) / "r.json"
        qf.write_text("\n".join(queries) + "\n", encoding="utf-8")
        run = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(HERE / "run_dax.ps1"), "-Port", str(PORT), "-Query", str(qf), "-Out", str(rf)],
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(run.stdout.strip())
        if not rf.exists():
            print(run.stderr.strip())
            sys.exit(2)
        T = json.loads(rf.read_text(encoding="utf-8"))

    def clean(v):
        return "" if v is None else str(v).replace(WJ, "")

    def key(k):
        return k[1:-1] if k.startswith("[") and k.endswith("]") else k

    def known(view, slot, want, got):
        return any(v == view and s == slot and got.replace(b, a) == want for v, s, a, b in KNOWN)

    vals = {}
    for view, slot, kind, i in plan:
        rows = [{key(k): v for k, v in r.items()} for r in T[i]]
        if kind == "scalars":
            vals[view] = rows[0] if rows else {}
            continue
        spec = sm.TEXT_SLOTS[[g for vv, g, *_ in VIEWS if vv == view][0]][slot]
        sort_col = spec["sort"]
        rows.sort(key=lambda r: r.get(sort_col, r.get(sort_col.split("[")[1][:-1])))
        want_rows = SPEC[view][slot][1:]
        cells = []
        for r in rows:
            cells.append([None if c is None else clean(r.get(c, r.get(c.split("[")[1][:-1]) if "[" in c else r.get(c))) for c in spec["cols"]])
        got = [[c for c in row] for row in cells]
        ok = len(got) == len(want_rows)
        diffs = []
        for wr, gr in zip(want_rows, got):
            for j, (w, g) in enumerate(zip(wr, gr)):
                if g is None:
                    continue
                if w != g:
                    diffs.append((w, g))
        state_known = diffs and all(known(view, slot, w, g) for w, g in diffs)
        detail = "" if ok else f"{len(got)} rows, spec {len(want_rows)}. "
        detail += " | ".join(f"spec {w!r} model {g!r}" for w, g in diffs[:6])
        results.append(("5 text against the spec", f"{view} · {slot}", "KNOWN" if ok and state_known else ("ok" if ok and not diffs else "FAIL"), detail))
    for view, group, scn, picked in VIEWS:
        for slot, spec in sm.TEXT_SLOTS[group].items():
            base, _, sub = slot.partition(".")
            if base not in SPEC[view] or isinstance(spec, dict):
                continue
            want = SPEC[view][base][sub] if sub else SPEC[view][base]
            parts = spec if isinstance(spec, list) else [spec]
            got = "\n".join("".join(p[1:] if p.startswith("=") else clean(vals[view].get(p)) for p in (line if isinstance(line, list) else [line])) for line in parts)
            if got == want:
                results.append(("5 text against the spec", f"{view} · {slot}", "ok", ""))
            else:
                results.append(("5 text against the spec", f"{view} · {slot}", "KNOWN" if known(view, slot, want, got) else "FAIL", f"spec {want!r} | model {got!r}"))
    # coverage: every slot of the spec is mapped here, typed in the report (TEXT_STATIC), or a chart's labels (number_checks.py)
    unmapped = sorted({f"{view}: {slot}" for view, group, *_ in VIEWS for slot, v in SPEC[view].items()
                       if slot not in sm.TEXT_SLOTS[group] and slot not in sm.TEXT_STATIC and not (isinstance(v, dict) and set(v) <= {"labels", "title"}
                                                                                                    and (("title" not in v) or f"{slot}.title" in sm.TEXT_SLOTS[group]))})
    record("5 every spec slot is accounted for", "mapped, static or chart labels", not unmapped, "; ".join(unmapped))
    # check 2 on what the rebuilt measures actually print
    printed = [(k, v) for view in vals for k, v in vals[view].items() if isinstance(v, str) and never_hits(v)]
    record("2 R-G2 vocabulary, printed text (strict)", "every evaluated scalar", not printed, "; ".join(f"{k}: {v[:60]!r}" for k, v in printed))

# ---------------------------------------------------------------- report
fails = [r for r in results if r[2] == "FAIL"]
lines = [f"build_checks: {len(results)} results, {sum(r[2] == 'ok' for r in results)} ok, {sum(r[2] == 'KNOWN' for r in results)} known, "
         f"{sum(r[2] == 'open' for r in results)} open, {len(fails)} failed" + (" (static: check 5 skipped)" if STATIC else ""), ""]
groups = {}
for c, k, st, d in results:
    groups.setdefault(c, []).append(st)
for c, sts in groups.items():
    lines.append(f"  {('FAIL' if 'FAIL' in sts else 'open' if 'open' in sts else 'ok  ')}  {c}: " + ", ".join(f"{sts.count(s)} {s}" for s in ("ok", "KNOWN", "open", "FAIL") if sts.count(s)))
for title, st in (("KNOWN (not failures)", "KNOWN"), ("OPEN (expected until the old visuals are gone, step 11)", "open"), ("FAILED", "FAIL")):
    rows = [r for r in results if r[2] == st]
    if rows:
        lines += ["", title]
        lines += [f"  {c} · {k}: {d}" for c, k, _, d in rows]
text = "\n".join(lines) + "\n"
print(text)
OUT.write_text(text, encoding="utf-8")
sys.exit(1 if fails else 0)
