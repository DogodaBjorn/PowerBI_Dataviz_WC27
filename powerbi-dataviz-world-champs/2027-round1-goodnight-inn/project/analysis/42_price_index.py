"""Plan 09 R1 / plan 11: feasibility check of the price-power index before it lands on P1.

Pricing power as the brand KPI that reaches the P&L (Kantar BrandZ, IPA; see CREDITS.md): ADR and RevPAR per brand
and year, indexed to a base year, so a budget brand can be compared with a luxury one by movement, not by level.

Usage (repo root, data stays local):
    python -I project/analysis/42_price_index.py project/data/PillowKey_Dataset.xlsx
    python -I project/analysis/42_price_index.py <parquet folder from 02_export_tables.py>

Prints both bases (2021 = 100 as plan 09 asks, and 2023 = 100 because the footer calls 2021 a depressed base year)
and the decision rule's inputs: Goodnight Inn's rank and its gap to the sisters in 2025, and how much of the 2021
index is the shared recovery (the four brands' spread against their mean).
"""
import os
import sys

import pandas as pd

src = sys.argv[1]
if os.path.isdir(src):
    hotels = pd.read_parquet(os.path.join(src, "Hotels.parquet"))
    perf = pd.read_parquet(os.path.join(src, "MonthlyPerformance.parquet"))
else:
    hotels = pd.read_excel(src, sheet_name="Hotels")
    perf = pd.read_excel(src, sheet_name="MonthlyPerformance")

mp = perf.merge(hotels[["HotelID", "Brand"]], on="HotelID")
mp["Year"] = pd.to_datetime(mp["Month"]).dt.year
for c in ("RoomsAvailable", "RoomsSold", "RoomRevenue"):
    mp[c] = mp[c].astype("float64")
g = mp.groupby(["Brand", "Year"])[["RoomsAvailable", "RoomsSold", "RoomRevenue"]].sum()
g["ADR"] = g.RoomRevenue / g.RoomsSold
g["RevPAR"] = g.RoomRevenue / g.RoomsAvailable
g["Occ"] = g.RoomsSold / g.RoomsAvailable

pd.set_option("display.width", 200)
print("== ADR, RevPAR and occupancy by brand and year")
print(g[["ADR", "RevPAR", "Occ"]].unstack("Year").round(3).to_string())

GI = "Goodnight Inn"
for base in (2021, 2023):
    print(f"\n==================== base {base} = 100")
    for k in ("ADR", "RevPAR"):
        ix = g[k].unstack("Year")
        ix = ix.div(ix[base], axis=0) * 100
        print(f"\n-- {k} index ({base} = 100)")
        print(ix.round(1).to_string())
        y = 2025
        col = ix[y].sort_values(ascending=False)
        rank = list(col.index).index(GI) + 1
        sisters = col.drop(GI)
        spread = col.max() - col.min()
        print(f"{k} {y}: Goodnight Inn {col[GI]:.1f}, rank {rank} of {len(col)} (higher = more pricing power); "
              f"sisters {sisters.min():.1f} to {sisters.max():.1f}; gap to sister mean {col[GI] - sisters.mean():+.1f} pts; "
              f"spread of the four {spread:.1f} pts; mean of the four {col.mean():.1f}")
print("\nDecision rule (plan 11 step 3): build R1 when Goodnight Inn's 2021-based RevPAR index tells a distinct story "
      "(a clear rank or gap against the sisters). If the four move together (small spread against a large shared rise), "
      "the 2021 base measures the recovery, not pricing power: show Bjorn both bases before building.")
