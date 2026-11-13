"""Number checks of the FinalV3 rebuild (doc 23, build step 3): the model's numbers against two independent sources.

  1. the organisers' workbook, re-derived here with pandas (the facts E5, E9 and E11 of doc 20, as in
     analysis/50_storytelling_checks.py), compared to full precision;
  2. the approved build spec (design-prototypes/rebuild-v10-spec.json, block 'text'): every number a number measure
     of step 3 feeds, in Low, Expected and High, compared as the text the model's own formatters print (E9, E10,
     E11, the cumulative end labels, the build bars, the page-1 labels).

Usage (a Desktop window with the model open and refreshed, in practice the throwaway copy):
    python project/tools/number_checks.py [--port <AS port>] [--xlsx <PillowKey_Dataset.xlsx>] [--out <report.txt>]
Exit code 1 when a check fails. Differences that are an open question for Bjorn are listed as KNOWN, not as failures.
Run with plain `python` (pandas sits in the user site).
"""
import json
import re
import subprocess
import sys
import tempfile
import warnings
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import sketch_model as sm  # noqa: E402  (the formatters and the dynamic format strings, as the model has them)

warnings.filterwarnings("ignore")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


PORT = int(arg("--port", "0"))
XLSX = Path(arg("--xlsx", str(ROOT / "project" / "data" / "PillowKey_Dataset.xlsx")))
OUT = Path(arg("--out", str(ROOT / "project" / "analysis" / "output" / "number_checks.txt")))
SPEC = json.loads((ROOT / "project" / "design-prototypes" / "rebuild-v10-spec.json").read_text(encoding="utf-8"))
TEXT = SPEC["text"]
BRAND, SCEN, A = "Goodnight Inn", ["Low", "Expected", "High"], ["GI-01", "GI-02", "GI-10"]
T2, T3 = ["GI-04", "GI-05"], ["GI-07"]
WJ, MINUS = "⁠", "−"
# open question 1 of doc 23: the kiosks' Expected "a year on cost" is exactly 20.55 %. The spec prints 20.5 (the
# browser's rounding), the model 20.6 (Power BI's). Bjorn decides; until then this one difference is expected.
KNOWN = {("hero yield", "GI-02", "Expected"): ("20.5%", "20.6%", "open question 1 of doc 23 (20.55 % exactly)")}

results = []  # (group, key, expected, actual, state)


def check(group, key, expected, actual, tol=None):
    if tol is not None and expected is not None and actual is not None:
        ok = abs(float(expected) - float(actual)) <= tol * max(1.0, abs(float(expected)))
    else:
        ok = expected == actual
    state = "ok" if ok else "FAIL"
    k = (group,) + tuple(key if isinstance(key, tuple) else (key,))
    if not ok and k in KNOWN and KNOWN[k][:2] == (expected, actual):
        state = "KNOWN"
    results.append((group, key, expected, actual, state))


def half_up(x, n):
    return float(Decimal(f"{x:.12g}").quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP))


def clean(s):
    return None if s is None else str(s).replace(WJ, "")


# ---------------------------------------------------------------- 1 · the workbook, re-derived
def sheet(name):
    return pd.read_excel(XLSX, sheet_name=name)


def year(df):
    df = df.copy()
    df["Year"] = pd.to_datetime(df.Month).dt.year
    return df


H = sheet("Hotels")
H = H[H.Brand == BRAND]
ids = set(H.HotelID)
M = year(sheet("MonthlyPerformance"))
MG = M[M.HotelID.isin(ids)]
Ball = year(sheet("BookingChannels"))
BG = Ball[Ball.HotelID.isin(ids)]
S = sheet("InvestmentScenarios")
P = sheet("InvestmentProjects")
P = P[P.Brand == BRAND].set_index("ProjectID")
BUDGET = float(sheet("Brands").set_index("Brand").loc[BRAND, "InvestmentBudgetUSD"])


def scn(pids, s, col):
    return float(S[(S.ProjectID.isin(pids)) & (S.Scenario == s)][col].sum())


def capex(pids):
    return float(P.loc[pids, "CapexUSD"].sum())


W = {}  # expected values from the workbook
for p in P.index:
    for s in SCEN:
        W["yield", p, s] = scn([p], s, "AnnualOperatingProfitImpactUSD") / capex([p])
        W["rr", p, s] = scn([p], s, "AnnualOperatingProfitImpactUSD")
hero_order = sorted(P.index, key=lambda p: -W["yield", p, "Expected"])


def yr_tot(y):
    my, by = MG[MG.Year == y], BG[BG.Year == y]
    return float(my.TotalRevenue.sum()), float(my.TotalOperatingExpenses.sum()), float(by.DistributionCost.sum()), float(by.RoomRevenue.sum())


tot, opex, dist, rroom = yr_tot(2025)
tot23, opex23, dist23, _ = yr_tot(2023)
_, _, dist21, rroom21 = yr_tot(2021)
m25, m23, d25, d21 = (tot - opex - dist) / tot, (tot23 - opex23 - dist23) / tot23, dist / rroom, dist21 / rroom21
for s in SCEN:
    prof, rev, dpts = scn(A, s, "AnnualOperatingProfitImpactUSD"), scn(A, s, "AnnualRevenueImpactUSD"), scn(A, s, "DistributionCostChangePts")
    W["Rec A Year on Cost (sel)", s] = prof / capex(A)
    W["Rec Run-rate (sel)", s] = prof
    W["Margin after 2032 with A (sel)", s] = (tot - opex - dist + prof) / (tot + rev)
    W["Dist Cost % 2032 with A (sel)", s] = d25 + dpts
    W["Dist Cost Rise Undone % (sel)", s] = (d25 - W["Dist Cost % 2032 with A (sel)", s]) / (d25 - d21)
    W["Margin Fall Recovered % (sel)", s] = (W["Margin after 2032 with A (sel)", s] - m25) / (m23 - m25)
    W["App Commission Saving (sel)", s] = -scn(["GI-01"], s, "DistributionCostChangePts") * rroom
    W["App Run-rate (sel)", s] = scn(["GI-01"], s, "AnnualOperatingProfitImpactUSD")
    W["Dist Cost % 2025 GI", s], W["KPI Margin after GI", s] = d25, m25
    W["Rec Run-rate Low", s] = scn(A, "Low", "AnnualOperatingProfitImpactUSD")
    W["Rec Capex", s] = W["Tranche 1 Capex", s] = capex(A)
    W["Tranche 2 Capex", s], W["Tranche 3 Capex", s] = capex(T2), capex(T3)
    W["Not Needed Capex", s] = BUDGET - capex(A) - capex(T2) - capex(T3)
    for k, t in ((1, A), (2, T2), (3, T3)):
        W[f"Tranche {k} Run-rate", s] = scn(t, s, "AnnualOperatingProfitImpactUSD")
        W[f"Tranche {k} Year on Cost", s] = W[f"Tranche {k} Run-rate", s] / capex(t)
    W["Build Run-rate (sel)", s], W["Build A Year on Cost (sel)", s], W["Build Capex", s] = prof, prof / capex(A), capex(A)
ally = [W["yield", p, s] for p in P.index for s in SCEN]

# F4: occupancy 2025 per hotel, the rows, the step for close neighbours (the comp's f4Points), the seven fullest
m25h = MG[MG.Year == 2025].groupby("HotelID")[["RoomsSold", "RoomsAvailable"]].sum()
occ = (m25h.RoomsSold / m25h.RoomsAvailable).to_dict()
ROWS = {"Airport": 3, "City": 2, "Highway": 1}
f4y = {}
for t, base in ROWS.items():
    row = sorted(H[H.LocationType == t].HotelID, key=lambda h: -occ[h])
    k = 0
    for i, h in enumerate(row):
        near = (i > 0 and occ[row[i - 1]] - occ[h] < 0.01) or (i < len(row) - 1 and occ[h] - occ[row[i + 1]] < 0.01)
        if near:
            k += 1
        f4y[h] = base + ((-0.3 if k % 2 == 1 else 0.3) if near else 0)
top7 = set(sorted(ids, key=lambda h: -occ[h])[:7])
last = pd.to_datetime(MG.Month).max()
m24 = MG[pd.to_datetime(MG.Month) > last - pd.DateOffset(months=24)]
m90 = m24[m24.RoomsSold / m24.RoomsAvailable >= 0.9].groupby("HotelID").size().to_dict()
types = MG[MG.Year == 2025].merge(H[["HotelID", "LocationType"]], on="HotelID").groupby("LocationType")[["RoomsSold", "RoomsAvailable"]].sum()
type_avg = (types.RoomsSold / types.RoomsAvailable).to_dict()
take = {y: yr_tot(y)[2] / yr_tot(y)[0] for y in range(2021, 2026)}


def ota(df, y):
    d = df[df.Year == y]
    return float(d[d.Channel == "Online Travel Agencies"].RoomRevenue.sum() / d.RoomRevenue.sum())


ota_gi = {y: ota(BG, y) for y in (2021, 2025)}
ota_sis = ota(Ball[~Ball.HotelID.isin(ids)], 2025)

# ---------------------------------------------------------------- 2 · the model, asked through DAX
GI_IDS = "{ " + ", ".join(f'"{p}"' for p in A) + " }"
SCEN_T = 'SELECTCOLUMNS ( ALL ( Scenario[Scenario] ), "s", Scenario[Scenario] )'
PF, SF = "InvestmentProjects[ProjectID] = p", "Scenario[Scenario] = s"


def calc(expr, *filters):
    return "CALCULATE ( " + expr + "".join(", " + f for f in filters) + " )"


def row(cols):
    return "ROW ( " + ", ".join(f'"{n}", {e}' for n, e in cols) + " )"


S_NUM = ["Rec A Year on Cost (sel)", "Rec NPV (sel)", "Rec Run-rate (sel)", "Rec NPV Low", "Rec Run-rate Low", "Rec Capex",
         "Tranche 1 Capex", "Tranche 2 Capex", "Tranche 3 Capex", "Not Needed Capex", "Tranche 1 Run-rate", "Tranche 2 Run-rate", "Tranche 3 Run-rate",
         "Tranche 1 Year on Cost", "Tranche 2 Year on Cost", "Tranche 3 Year on Cost", "Dist Cost % 2025 GI", "Dist Cost % 2032 with A (sel)",
         "Margin after 2032 with A (sel)", "KPI Margin after GI", "Dist Cost Rise Undone % (sel)", "Margin Fall Recovered % (sel)",
         "App Commission Saving (sel)", "App NPV (sel)", "App Run-rate (sel)",
         "Hero Yield Domain Min", "Hero Yield Domain Max", "Hero NPV Domain Min", "Hero NPV Domain Max"]
S_MONEY_U = ["Rec Capex", "Tranche 1 Capex", "Tranche 2 Capex", "Tranche 3 Capex", "Not Needed Capex", "App Commission Saving (sel)"]
S_MONEY_S = ["Rec NPV (sel)", "Rec Run-rate (sel)", "Rec NPV Low", "Rec Run-rate Low", "Tranche 2 Run-rate", "Tranche 3 Run-rate", "App NPV (sel)", "App Run-rate (sel)"]
S_PCT = ["Rec A Year on Cost (sel)", "Tranche 2 Year on Cost", "Tranche 3 Year on Cost", "Dist Cost % 2025 GI", "Dist Cost % 2032 with A (sel)",
         "Margin after 2032 with A (sel)", "KPI Margin after GI"]
ENDS = [n for n in sm.FMT_DEFS if "Cumulative End" in n]
B_NUM = ["Build Count", "Build Capex", "Build Run-rate (sel)", "Build A Year on Cost (sel)", "Build NPV (sel)"]

q = []
# T0 · the ten moves in the three scenarios
q.append("EVALUATE GENERATE ( CROSSJOIN ( SELECTCOLUMNS ( FILTER ( ALL ( InvestmentProjects[ProjectID], InvestmentProjects[Brand] ), InvestmentProjects[Brand] = \"Goodnight Inn\" ), \"p\", InvestmentProjects[ProjectID] ), "
         + SCEN_T + " ), VAR p = [p] VAR s = [s] RETURN " + row([
             ("yield", calc("[A Year on Cost]", PF, SF)), ("npv", calc("[NPV @ 8%]", PF, SF)), ("rr", calc("[2032 Run-rate]", PF, SF)),
             ("yield_txt", calc(sm.pct1("[A Year on Cost]"), PF, SF)), ("npv_txt", calc(sm.sfm("[NPV @ 8%]"), PF, SF)),
             ("color", calc("[Move Status Color]", PF)), ("ybar", calc("[Hero Yield Bar SVG]", PF, SF)), ("nbar", calc("[Hero NPV Bar SVG]", PF, SF)),
             ("name", calc("SELECTEDVALUE ( InvestmentProjects[Move Name] )", PF)), ("hsort", calc("SELECTEDVALUE ( InvestmentProjects[Hero Sort] )", PF)),
             ("status", "LOOKUPVALUE ( MoveDecision[Status], MoveDecision[ProjectID], p )"), ("finding", "LOOKUPVALUE ( MoveDecision[Finding], MoveDecision[ProjectID], p )"),
             ("tranche", "LOOKUPVALUE ( MoveDecision[Tranche], MoveDecision[ProjectID], p )"),
             ("bsort", "LOOKUPVALUE ( BuildMove[Sort], BuildMove[ProjectID], p )"), ("short", "LOOKUPVALUE ( BuildMove[Short Name], BuildMove[ProjectID], p )"),
             ("move_rr", calc("[Move Run-rate (num)]", "BuildMove[ProjectID] = p", SF)), ("move_rr_txt", calc(sm.sfm("[Move Run-rate (num)]"), "BuildMove[ProjectID] = p", SF)),
             ("move_npv_txt", calc(sm.sfm("[Move NPV (num)]"), "BuildMove[ProjectID] = p", SF)),
             ("move_capex_txt", calc(sm.fm("[Move Capex (num)]"), "BuildMove[ProjectID] = p")), ("move_answers", calc("[Move Answers (text)]", "BuildMove[ProjectID] = p"))]) + " )")
# T1 · scalars per scenario, as numbers and as the formatters print them
q.append("EVALUATE GENERATE ( " + SCEN_T + ", VAR s = [s] RETURN " + row(
    [(n, calc(f"[{n}]", SF)) for n in S_NUM]
    + [(n + " | txt", calc(sm.fm(f"[{n}]"), SF)) for n in S_MONEY_U] + [(n + " | txt", calc(sm.sfm(f"[{n}]"), SF)) for n in S_MONEY_S]
    + [(n + " | txt", calc(sm.pct1(f"[{n}]"), SF)) for n in S_PCT]) + " )")
# T2 · cumulative end series on 2031 and 2032, value and dynamic format string; package A picked in the Build selector
q.append("EVALUATE CALCULATETABLE ( GENERATE ( CROSSJOIN ( " + SCEN_T + ", SELECTCOLUMNS ( { 2031, 2032 }, \"y\", [Value] ) ), VAR s = [s] VAR y = [y] RETURN " + row(
    [(n, calc(f"[{n}]", SF, "'Date'[Year] = y")) for n in ENDS] + [(n + " | fmt", calc("( " + sm.FMT_DEFS[n] + " )", SF, "'Date'[Year] = y")) for n in ENDS]
    + [("A line " + c, calc(f"[A Cumulative Line ({c})]", SF, "'Date'[Year] = y")) for c in SCEN]) + f" ), BuildMove[ProjectID] IN {GI_IDS} )")
# T3 · the Build state with package A picked; T4 · with nothing picked
q.append("EVALUATE CALCULATETABLE ( GENERATE ( " + SCEN_T + ", VAR s = [s] RETURN " + row([(n, calc(f"[{n}]", SF)) for n in B_NUM]
         + [("yoc_txt", calc(sm.pct1("[Build A Year on Cost (sel)]"), SF)), ("rr_txt", calc(sm.sfm("[Build Run-rate (sel)]"), SF))]) + f" ), BuildMove[ProjectID] IN {GI_IDS} )")
q.append("EVALUATE " + row([(n, f"[{n}]") for n in B_NUM] + [("end", calc("[Build Cumulative End Name (label-safe)]", "'Date'[Year] = 2032")), ("bar", "[Build Bar NPV]")]))
# T5-T7 · the build bars per scenario (package A picked)
for s in SCEN:
    q.append("EVALUATE SUMMARIZECOLUMNS ( BuildMove[ProjectID], BuildMove[Short Name], TREATAS ( " + GI_IDS + f", BuildMove[ProjectID] ), TREATAS ( {{ \"{s}\" }}, Scenario[Scenario] ), "
             '"v", [Build Bar NPV], "ls", [Build Bar NPV (label-safe)], "fmt", ' + sm.FMT_DEFS["Build Bar NPV (label-safe)"] + ', "color", [Build Bar Color] )')
# T8 · F4 per hotel; T9 · F4 per location type; T10 · the trend years; T11 · the F3 bands
GI_H = 'TREATAS ( { "Goodnight Inn" }, Hotels[Brand] )'
q.append(f'EVALUATE SUMMARIZECOLUMNS ( Hotels[HotelID], Hotels[HotelName], Hotels[LocationType], {GI_H}, "y", [F4 Row Y], "color", [F4 Dot Color], "occ", [Occupancy % 2025], "m90", [Months Topped 90% (last 24)] )')
q.append(f'EVALUATE SUMMARIZECOLUMNS ( Hotels[LocationType], {GI_H}, "y", [F4 Row Y], "avg", [F4 Type Avg] )')
q.append("EVALUATE SUMMARIZECOLUMNS ( 'Date'[Year], \"take\", [Trend Commission Take GI], \"ota\", [Trend OTA GI (ends)], \"sis\", [Trend OTA Sisters (end)], "
         "\"ota_txt\", FORMAT ( [Trend OTA GI (ends)], \"0%\", \"en-US\" ), \"sis_txt\", FORMAT ( [Trend OTA Sisters (end)], \"0%\", \"en-US\" ) )")
q.append(f"EVALUATE SUMMARIZECOLUMNS ( Hotels[Renovation Age Sort], {GI_H}, \"v\", [NPS 2025 (label-safe)], \"fmt\", " + sm.FMT_DEFS["NPS 2025 (label-safe)"] + " )")

with tempfile.TemporaryDirectory() as td:
    qf, rf = Path(td) / "q.dax", Path(td) / "r.json"
    qf.write_text("\n".join(q) + "\n", encoding="utf-8")
    run = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(HERE / "run_dax.ps1"), "-Port", str(PORT), "-Query", str(qf), "-Out", str(rf)],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(run.stdout.strip())
    if not rf.exists():
        print(run.stderr.strip())
        sys.exit(2)
    T = json.loads(rf.read_text(encoding="utf-8"))


def norm(rows):
    return [{(k[1:-1] if k.startswith("[") else k): v for k, v in r.items()} for r in rows]  # "[yield]" -> "yield"; "Hotels[HotelID]" stays


T = [norm(t) for t in T]
moves = {(r["p"], r["s"]): r for r in T[0]}
scal = {r["s"]: r for r in T[1]}
ends = {(r["s"], int(r["y"])): r for r in T[2]}
build = {r["s"]: r for r in T[3]}
empty = T[4][0]
bars = dict(zip(SCEN, T[5:8]))
f4h, f4t, trend, f3 = T[8], T[9], T[10], T[11]

# ---------------------------------------------------------------- 3 · compare
# 3a · against the workbook (full precision)
for p in P.index:
    for s in SCEN:
        check("workbook: a year on cost per move (E9)", (p, s), W["yield", p, s], moves[p, s]["yield"], 1e-9)
        check("workbook: profit a year per move", (p, s), W["rr", p, s], moves[p, s]["rr"], 1e-9)
        check("workbook: selector row run-rate", (p, s), W["rr", p, s], moves[p, s]["move_rr"], 1e-9)
check("workbook: Hero Sort order", "order", hero_order, [p for p, _ in sorted({(p, moves[p, "Expected"]["hsort"]) for p in P.index}, key=lambda x: x[1])])
for s in SCEN:
    for n in ("Rec A Year on Cost (sel)", "Rec Run-rate (sel)", "Rec Run-rate Low", "Rec Capex", "Tranche 1 Capex", "Tranche 2 Capex", "Tranche 3 Capex", "Not Needed Capex",
              "Tranche 1 Run-rate", "Tranche 2 Run-rate", "Tranche 3 Run-rate", "Tranche 1 Year on Cost", "Tranche 2 Year on Cost", "Tranche 3 Year on Cost",
              "Dist Cost % 2025 GI", "Dist Cost % 2032 with A (sel)", "Margin after 2032 with A (sel)", "KPI Margin after GI", "Dist Cost Rise Undone % (sel)",
              "Margin Fall Recovered % (sel)", "App Commission Saving (sel)", "App Run-rate (sel)"):
        check("workbook: package A, tranches and the 2032 ledger (E9, E11)", (n, s), W[n, s], scal[s][n], 1e-9)
    check("workbook: plan segments add up to the budget", s, BUDGET, sum(scal[s][f"Tranche {k} Capex"] for k in (1, 2, 3)) + scal[s]["Not Needed Capex"], 1e-12)
    for n in ("Build Run-rate (sel)", "Build A Year on Cost (sel)", "Build Capex"):
        check("workbook: Build state with package A picked", (n, s), W[n, s], build[s][n], 1e-9)
    check("workbook: Build state with package A picked", ("Build Count", s), 3, build[s]["Build Count"])
    check("model: Build with A picked equals the recommendation", ("NPV", s), scal[s]["Rec NPV (sel)"], build[s]["Build NPV (sel)"], 1e-9)
    # the fixed domains of the hero bar cells against the data
    check("hero domain equals the spec constants", ("yield min", s), sm.HERO_YDOM[0], scal[s]["Hero Yield Domain Min"], 1e-12)
    check("hero domain equals the spec constants", ("yield max", s), sm.HERO_YDOM[1], scal[s]["Hero Yield Domain Max"], 1e-12)
    check("hero domain equals the spec constants", ("npv min", s), sm.HERO_NDOM[0], scal[s]["Hero NPV Domain Min"], 1e-12)
    check("hero domain equals the spec constants", ("npv max", s), sm.HERO_NDOM[1], scal[s]["Hero NPV Domain Max"], 1e-12)
check("workbook: hero yield domain covers the data", "min", True, sm.HERO_YDOM[0] <= min(ally) and max(ally) <= sm.HERO_YDOM[1])
for r in f4h:
    h = r["Hotels[HotelID]"] if "Hotels[HotelID]" in r else r["HotelID"]
    check("workbook: F4 Row Y per hotel (the comp's rule)", h, round(f4y[h], 6), round(float(r["y"]), 6))
    check("workbook: F4 Dot Color (Night = the seven fullest)", h, sm.INK if h in top7 else sm.SLATE, r["color"])
    check("workbook: months at or above 90 % in the last 24 (E5)", h, int(m90.get(h, 0)), int(r["m90"]))
check("workbook: F4 has 50 hotels", "count", len(ids), len(f4h))
for r in f4t:
    t = r.get("Hotels[LocationType]", r.get("LocationType"))
    check("workbook: F4 row and average per location type", (t, "row"), ROWS[t], r["y"])
    check("workbook: F4 row and average per location type", (t, "avg"), type_avg[t], r["avg"], 1e-9)
for r in trend:
    y = int(r.get("Date[Year]", r.get("Year")))
    if y in take:
        check("workbook: commission take per year (F1 band)", y, take[y], r["take"], 1e-9)
        check("workbook: OTA end labels (F2)", (y, "GI"), ota_gi.get(y), r["ota"], 1e-9 if y in ota_gi else None)
        check("workbook: OTA end labels (F2)", (y, "sisters"), ota_sis if y == 2025 else None, r["sis"], 1e-9 if y == 2025 else None)

# 3b · against the approved spec text (what the formatters print, Low / Expected / High)
name_of = {moves[p, "Expected"]["name"]: p for p in P.index}
for s in SCEN:
    rec, alts, bld = TEXT[f"P2 rec {s}"], TEXT[f"P2 alts {s}"], TEXT[f"P2 build {s}"]
    hero = rec["tbl_hero"][1:]
    check("spec: hero table row order", s, [r[0] for r in hero], [moves[p, s]["name"] for p in sorted(P.index, key=lambda p: moves[p, s]["hsort"])])
    for r in hero:
        p = name_of[r[0]]
        check("hero yield", (p, s), r[4], clean(moves[p, s]["yield_txt"]))
        check("spec: hero NPV through 2032 (E10)", (p, s), r[6], clean(moves[p, s]["npv_txt"]))
        check("spec: hero status", (p, s), r[2], moves[p, s]["status"])
        check("spec: hero answers start with the MoveDecision finding", (p, s), r[1].split(" ")[0], moves[p, s]["finding"])
    nums = rec["c_rec_nums"].split("\n")
    for want, n in ((nums[0], "Rec Capex"), (nums[2], "Rec NPV (sel)"), (nums[4], "Rec Run-rate (sel)"), (nums[6], "Rec A Year on Cost (sel)")):
        check("spec: recommendation numbers (E10)", (n, s), want, clean(scal[s][n + " | txt"]))
    line1, line2 = rec["c_rec_lines"].split("\n")
    money = lambda t: re.findall(r"[+−]?\$[\d.]+M", t)  # noqa: E731
    check("spec: worst case line (Low, always)", ("NPV", s), money(line1)[0], clean(scal[s]["Rec NPV Low | txt"]))
    check("spec: worst case line (Low, always)", ("a year", s), money(line1)[1], clean(scal[s]["Rec Run-rate Low | txt"]))
    check("spec: the app carries it", ("app", s), money(line2)[0], clean(scal[s]["App Run-rate (sel) | txt" if s == "Low" else "App NPV (sel) | txt"]))
    check("spec: the app carries it", ("leaves with the agencies", s), money(line2)[2], clean(scal[s]["App Commission Saving (sel) | txt"]))
    led = {r[0][:2]: r for r in rec["tbl_ledger"][1:]}
    check("spec: ledger (E11)", ("F2 2025", s), led["F2"][2], clean(scal[s]["Dist Cost % 2025 GI | txt"]))
    check("spec: ledger (E11)", ("F2 2032 with A", s), led["F2"][3], clean(scal[s]["Dist Cost % 2032 with A (sel) | txt"]))
    check("spec: ledger (E11)", ("F1 2025", s), led["F1"][2], clean(scal[s]["KPI Margin after GI | txt"]))
    check("spec: ledger (E11)", ("F1 2032 with A", s), led["F1"][3], clean(scal[s]["Margin after 2032 with A (sel) | txt"]))
    check("spec: plan segments", ("T1", s), rec["c_plan_t1"].split("\n")[1].split(" · ")[0], clean(scal[s]["Tranche 1 Capex | txt"]))
    check("spec: plan segments", ("T4", s), rec["c_plan_t4"].split(" · ")[1], clean(scal[s]["Not Needed Capex | txt"]))
    for k in (2, 3):
        t = rec[f"c_plan_t{k}"].split("\n")
        check("spec: plan segments", (f"T{k} capex", s), t[1].split(" · ")[0], clean(scal[s][f"Tranche {k} Capex | txt"]))
        check("spec: plan segments", (f"T{k} a year once live", s), t[2].split(" ")[0], clean(scal[s][f"Tranche {k} Run-rate | txt"]))
        check("spec: plan segments", (f"T{k} a year on cost", s), t[2].split(" · ")[1].split(" ")[0], clean(scal[s][f"Tranche {k} Year on Cost | txt"]))
    # cumulative end labels: on 2032 the literal the label prints, on 2031 nothing
    e32, e31 = ends[s, 2032], ends[s, 2031]
    lit = lambda v: None if v is None else clean(v).split(";")[0].strip('"')  # noqa: E731
    shown = sorted(lit(e32[n + " | fmt"]) for n in ENDS if n.startswith("A Cumulative End") and "Name" not in n and e32[n] is not None)
    check("spec: capital plan end labels", s, sorted(x for x in rec["ch_plan_cum"]["labels"] if x.split(" ")[0] in SCEN), shown)
    check("model: the case in view has no thin line", s, None, e32[f"A line {s}"])
    shown = sorted(lit(e32[f"Preset {k} Cumulative End (label-safe) | fmt"]) for k in "ABC")
    check("spec: comparison end labels (A, B, C)", s, sorted(x for x in alts["ch_cmp_alts"]["labels"] if x[:2] in ("A ", "B ", "C ")), shown)
    check("spec: build comparison end labels", s, sorted(x for x in bld["ch_cmp_build"]["labels"] if x in ("A", "You")),
          sorted(lit(e32[n + " | fmt"]) for n in ("A Cumulative End Name (label-safe)", "Build Cumulative End Name (label-safe)") if e32[n] is not None))
    check("model: end series are blank before the horizon year", s, [], [n for n in ENDS if e31[n] is not None])
    for part in (lit(e32[n + " | fmt"]) for n in ENDS):
        pass
    check("model: a dynamic format string repeats its literal in three sections", s, True,
          all(e32[n + " | fmt"].split(";")[0] == e32[n + " | fmt"].split(";")[1] == e32[n + " | fmt"].split(";")[2] for n in ENDS))
    # the selector table and the build bars
    rows = sorted(P.index, key=lambda p: moves[p, s]["bsort"])
    for want, p in zip(bld["tbl_moves"][1:], rows):
        check("spec: selector table", (p, s, "answers"), want[0], moves[p, s]["move_answers"])
        check("spec: selector table", (p, s, "capex"), want[1], clean(moves[p, s]["move_capex_txt"]))
        check("spec: selector table", (p, s, "NPV"), want[2], clean(moves[p, s]["move_npv_txt"]))
        check("spec: selector table", (p, s, "a year by 2032"), want[3], clean(moves[p, s]["move_rr_txt"]))
    lab = bld["ch_build_bars"]["labels"]
    got = sorted(bars[s], key=lambda r: -r["v"])
    check("spec: build bars, names and labels in NPV order", s, lab, [x for r in got for x in (r.get("BuildMove[Short Name]", r.get("Short Name")), lit(r["fmt"]))])
    check("model: build bar colours (Night adds, Tangerine costs)", s, [sm.SIGNAL_MARK if half_up(r["v"] / 1e6, 2) < 0 else sm.INK for r in got], [r["color"] for r in got])
    you = bld["c_you_nums"].split("\n")
    check("spec: your-plan numbers", ("a year by 2032", s), you[4], clean(build[s]["rr_txt"]))
    check("spec: your-plan numbers", ("a year on cost", s), you[6], clean(build[s]["yoc_txt"]))
check("model: nothing picked", "count, run-rate, a year on cost, end label, bar", [0, None, None, None, None],
      [empty["Build Count"], empty["Build Run-rate (sel)"], empty["Build A Year on Cost (sel)"], empty["end"], empty["bar"]])
p1 = TEXT["P1"]
check("spec: F3 bar labels", "bands", [x for x in p1["ch_f3_age"]["labels"] if x[0] in "+0" + MINUS],
      [clean(r["fmt"]).split(";")[0].strip('"') for r in sorted((r for r in f3 if r.get("Hotels[Renovation Age Sort]", r.get("Renovation Age Sort")) is not None),
                                                               key=lambda r: r.get("Hotels[Renovation Age Sort]", r.get("Renovation Age Sort")))])
check("spec: F2 end labels", "33%, 50%, 27%", p1["ch_f2_ota"]["labels"][:3],
      [r["ota_txt"] for r in sorted(trend, key=lambda r: r.get("Date[Year]", r.get("Year"))) if r["ota"] is not None]
      + [r["sis_txt"] for r in trend if r["sis"] is not None])
rows_txt = dict(x.rsplit(" ", 1) for x in p1["c_f4_rows"].split("\n"))
for r in f4t:
    t = r.get("Hotels[LocationType]", r.get("LocationType"))
    check("spec: F4 row averages", t, rows_txt[t], f"{half_up(r['avg'] * 100, 1):.1f}%")
names = {r.get("Hotels[HotelID]", r.get("HotelID")): r.get("Hotels[HotelName]", r.get("HotelName")) for r in f4h}
for part, n in (("Toronto", 17), ("Gatwick", 14), ("Trudeau", 13), ("Kingston", 0)):
    h = [k for k, v in names.items() if part in v][0]
    check("doc 20 E5: months at or above 90 %", part, n, int([r for r in f4h if r.get("Hotels[HotelID]", r.get("HotelID")) == h][0]["m90"]))
# the hero bar cells: one image width, the reference line at the constant x, a rect per bar
for (p, s), r in moves.items():
    for col, ref, dom, w in (("ybar", sm.HERO_YREF, sm.HERO_YDOM, sm.HERO_SPEC_COLS[3]), ("nbar", sm.HERO_NREF, sm.HERO_NDOM, sm.HERO_SPEC_COLS[5])):
        svg = r[col]
        xr = sm.bar_x(ref, dom, w) - sm.HERO_IMG_PAD - 0.5
        ok = svg.startswith("data:image/svg+xml;utf8,<svg") and f"width='{sm.HERO_IMG_W}' height='{sm.HERO_ROW_H}'" in svg and f"<rect x='{xr:.2f}' y='0' width='1'" in svg \
            and "," not in svg.split("utf8,", 1)[1] and r["color"].replace("#", "%23") in svg
        check("model: hero bar cell is a well-formed SVG with the reference line at its constant x", (p, s, col), True, ok)

# ---------------------------------------------------------------- 4 · report
fails = [r for r in results if r[4] == "FAIL"]
known = [r for r in results if r[4] == "KNOWN"]
lines = [f"number_checks: {len(results)} checks, {len(results) - len(fails) - len(known)} ok, {len(known)} known difference(s), {len(fails)} failed", ""]
groups = {}
for g, k, e, a, st in results:
    groups.setdefault(g, [0, 0, 0])[("ok", "KNOWN", "FAIL").index(st)] += 1
for g, (o, kn, f) in groups.items():
    lines.append(f"  {'FAIL' if f else 'ok  '}  {g}: {o} ok" + (f", {kn} known" if kn else "") + (f", {f} FAILED" if f else ""))
for title, rows in (("KNOWN (not failures)", known), ("FAILED", fails)):
    if rows:
        lines += ["", title]
        for g, k, e, a, st in rows:
            lines.append(f"  {g} {k}: expected {e!r}, model {a!r}" + (f"  [{KNOWN[(g,) + tuple(k if isinstance(k, tuple) else (k,))][2]}]" if st == "KNOWN" else ""))
lines += ["", "Values (model, as its formatters print them):"]
for s in SCEN:
    r = scal[s]
    lines.append(f"  {s:8s} A: capex {clean(r['Rec Capex | txt'])}, NPV {clean(r['Rec NPV (sel) | txt'])}, a year {clean(r['Rec Run-rate (sel) | txt'])}, a year on cost {clean(r['Rec A Year on Cost (sel) | txt'])}"
                 f" | ledger: distribution cost {clean(r['Dist Cost % 2025 GI | txt'])} -> {clean(r['Dist Cost % 2032 with A (sel) | txt'])}, margin after commissions {clean(r['KPI Margin after GI | txt'])} -> {clean(r['Margin after 2032 with A (sel) | txt'])}"
                 f", app saves {clean(r['App Commission Saving (sel) | txt'])} a year | tranche 2 {clean(r['Tranche 2 Year on Cost | txt'])}, tranche 3 {clean(r['Tranche 3 Year on Cost | txt'])}"
                 f" | rise undone {r['Dist Cost Rise Undone % (sel)']:.3f}, fall recovered {r['Margin Fall Recovered % (sel)']:.3f}")
lines.append("  a year on cost per move, Low / Expected / High: " + "; ".join(f"{p} " + " / ".join(clean(moves[p, s]['yield_txt']) for s in SCEN) for p in hero_order))
text = "\n".join(lines) + "\n"
print(text)
OUT.write_text(text, encoding="utf-8")
sys.exit(1 if fails else 0)
