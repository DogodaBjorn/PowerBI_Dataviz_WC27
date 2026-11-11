"""Compare the Desktop measure values (DAX via the Modeling MCP, 7 Nov) with packages.csv from the offline analysis."""
import csv

CSV = r"E:\PowerBI_Dataviz_WC27\project\analysis\output\packages.csv"
rows = {r["PackageID"]: r for r in csv.DictReader(open(CSV, encoding="utf-8"))}

# (focus package, scenario): capex, NPV(sel), cum2032 low/exp/high, rooms added, hotels rated  -- from the DAX run
dax = {
    ("01+02+03+05+08+09+10", "Expected"): (60000000, -31826359.09449216, -43552488.43, -25992655.096666664, -9031071.76333333, 190, 50),
    ("01+02+03+05+08+09+10", "High"): (60000000, -18960932.14992307, None, None, None, 190, 50),
    ("01+02+03+05+08+09+10", "Low"): (60000000, -45117049.65448993, None, None, None, 190, 50),
    ("01+02+10", "Expected"): (9400000, 3276891.3994296286, -4642100, 6819900.000000002, 19186350, 0, 20),
    ("01+02+10", "High"): (9400000, 12719998.036994074, None, None, None, 0, 20),
    ("01+02+10", "Low"): (9400000, -5470003.915693456, None, None, None, 0, 20),
    ("01+09+10", "Expected"): (11650000, 2739352.2498829435, -5765016.666666668, 6832850, 19670716.666666668, 0, 50),
    ("01+02+09+10", "High"): (13650000, 12591028.052768536, -6920416.666666668, 6517950, 20200416.666666664, 0, 50),
    ("01+07+10", "Expected"): (36900000, -23437568.0299526, -34084648.51666668, -19191965.183333345, -3331998.516666673, 0, 10),
    ("01+02+07+10", "High"): (38900000, -11339066.29265529, -35240048.51666668, -19506865.183333345, -2802298.5166666657, 0, 27),
    ("01+02+07", "Low"): (36500000, -34498150.892228514, -33974948.51666668, -20831665.183333345, -7585148.516666673, 0, 27),
}
rec_runrate = {"Low": 1044000, "Expected": 3529000, "High": 6201000}

bad = 0
for (pid, sc), (cap, npv, cl, ce, ch, rooms, hotels) in dax.items():
    r = rows[pid]
    checks = [("capex", cap, float(r["CapexUSD"])), (f"NPV_{sc}", npv, float(r[f"NPV_{sc}"])),
              ("RoomsAdded", rooms, float(r["RoomsAdded"])), ("HotelsRated", hotels, float(r["HotelsRated"]))]
    if cl is not None:
        checks += [("Net_Low", cl, float(r["Net_Low"])), ("Net_Expected", ce, float(r["Net_Expected"])), ("Net_High", ch, float(r["Net_High"]))]
    for name, got, want in checks:
        ok = abs(got - want) <= max(1.0, abs(want) * 1e-9)
        bad += not ok
        if not ok:
            print(f"MISMATCH {pid} {sc} {name}: desktop {got} csv {want}")
for sc, v in rec_runrate.items():
    want = float(rows["01+02+10"][f"RunRate_{sc}"])
    if abs(v - want) > 1:
        bad += 1
        print(f"MISMATCH A run-rate {sc}: desktop {v} csv {want}")
# which packages do the B and C rules pick per scenario, offline? (Shortlist_Expected is the only flag in the csv)
print("shortlist flags in csv:", sorted({r["Shortlist_Expected"] for r in rows.values()}))
print("B Low candidates (HotelsRated max, NPV_Low >= 0):",
      sorted(((int(float(r["HotelsRated"])), pid) for pid, r in rows.items() if float(r["NPV_Low"]) >= 0), reverse=True)[:3])
print("checks done,", bad, "mismatches")
