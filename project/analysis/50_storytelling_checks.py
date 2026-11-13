"""Storytelling checks for doc 19/20 (13 Nov 2026): the facts the requirements in
project-state/active/20-requirements-storytelling-2026-11-13.md rest on.

Usage: python 50_storytelling_checks.py <PillowKey_Dataset.xlsx> > output/storytelling_checks.txt
Reads the organisers' workbook directly (one sheet at a time). Evidence only; the semantic
model re-derives every number before it reaches a visual.
"""
import sys
import warnings

import pandas as pd

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
F = sys.argv[1]
BRAND = "Goodnight Inn"


def sheet(name):
    return pd.read_excel(F, sheet_name=name)


def year(df):
    df = df.copy()
    df["Year"] = pd.to_datetime(df.Month).dt.year
    return df


H = sheet("Hotels")
H = H[H.Brand == BRAND]
ids = set(H.HotelID)
PP = sheet("InvestmentProjectProperties")
kiosk = set(PP[PP.ProjectID == "GI-02"].HotelID)
refresh = set(PP[PP.ProjectID == "GI-07"].HotelID)
M = year(sheet("MonthlyPerformance"))
M = M[M.HotelID.isin(ids)]
B = year(sheet("BookingChannels"))
B = B[B.HotelID.isin(ids)]
C = year(sheet("GuestComplaints"))
C = C[C.HotelID.isin(ids)]
S = sheet("InvestmentScenarios")
P = sheet("InvestmentProjects")
P = P[P.Brand == BRAND].set_index("ProjectID")

print("== 1 kiosk hotels (GI-02) against the occupancy ranking, 2025")
m25 = M[M.Year == 2025]
occ = (m25.groupby("HotelID").RoomsSold.sum() / m25.groupby("HotelID").RoomsAvailable.sum()).sort_values(ascending=False)
top20 = set(occ.index[:20])
print("kiosk set == 20 fullest:", kiosk == top20, "| min kiosk occ", round(occ[list(kiosk)].min(), 4),
      "| 21st", occ.index[20], round(occ.iloc[20], 4))

print("\n== 2 complaints per 1,000 room nights sold: kiosk hotels vs the other 30")
M["K"] = M.HotelID.isin(kiosk)
C["K"] = C.HotelID.isin(kiosk)
rn = M.groupby(["K", "Year"]).RoomsSold.sum()
for cat in ["Check-in & waiting times", "Room condition"]:
    c = C[C.Category == cat].groupby(["K", "Year"]).Complaints.sum()
    print(cat)
    print((c / rn * 1000).round(2).unstack().rename(index={True: "kiosk 20", False: "other 30"}).to_string())

print("\n== 3 ADR growth: kiosk (fullest 20) vs other 30 (tests the 'full but not pricing' idea)")
adr = M.groupby(["K", "Year"]).apply(lambda g: g.RoomRevenue.sum() / g.RoomsSold.sum()).unstack()
print("2023-25", (adr[2025] / adr[2023] - 1).round(4).to_dict(), "| 2021-25", (adr[2025] / adr[2021] - 1).round(4).to_dict())

print("\n== 4 months at or above 90 % occupancy, 2024-2025 (24 months)")
m2 = M[M.Year >= 2024].copy()
m2["occ"] = m2.RoomsSold / m2.RoomsAvailable
cnt = m2[m2.occ >= 0.9].groupby("HotelID").size().reindex(sorted(ids)).fillna(0).astype(int)
names = H.set_index("HotelID").HotelName
for hid in ["GI002", "GI027", "GI001", "GI009"]:
    print(f"  {names[hid]}: {cnt[hid]} of 24 | occupancy 2025 {occ[hid]:.3f}")

print("\n== 5 margin after commissions: split of the fall since 2023")
rows = []
for y in range(2021, 2026):
    my, by = M[M.Year == y], B[B.Year == y]
    tot, opex, dist, rr = my.TotalRevenue.sum(), my.TotalOperatingExpenses.sum(), by.DistributionCost.sum(), by.RoomRevenue.sum()
    rows.append(dict(Year=y, GOP=(tot - opex) / tot, Dist_rev=dist / tot, After=(tot - opex - dist) / tot,
                     Dist_room=dist / rr, Staff=my.StaffCost.sum() / tot))
T = pd.DataFrame(rows).set_index("Year")
print(T.round(4).to_string())
d = T.loc[2025] - T.loc[2023]
print(f"since 2023: after {d.After*100:+.1f} pt = operations {d.GOP*100:+.1f} pt, commissions {-d.Dist_rev*100:+.1f} pt; staff {d.Staff*100:+.1f} pt")

print("\n== 6 the 2032 ledger: 2025 brand plus package A at full effect (2025 dollars)")
m25, b25 = M[M.Year == 2025], B[B.Year == 2025]
tot, opex, dist, rr = m25.TotalRevenue.sum(), m25.TotalOperatingExpenses.sum(), b25.DistributionCost.sum(), b25.RoomRevenue.sum()
A = ["GI-01", "GI-02", "GI-10"]
for sc in ["Low", "Expected", "High"]:
    s = S[(S.ProjectID.isin(A)) & (S.Scenario == sc)]
    prof, rev = s.AnnualOperatingProfitImpactUSD.sum(), s.AnnualRevenueImpactUSD.sum()
    dpts = s.DistributionCostChangePts.sum()
    after = (tot - opex - dist + prof) / (tot + rev)
    print(f"  {sc:8s} profit a year {prof/1e6:5.2f}M | margin after commissions {(tot-opex-dist)/tot:.4f} -> {after:.4f}"
          f" | distribution cost % room revenue {dist/rr:.4f} -> {dist/rr + dpts:.4f}"
          f" | app's yearly commission saving {-S[(S.ProjectID=='GI-01')&(S.Scenario==sc)].DistributionCostChangePts.iloc[0]*rr/1e6:.2f}M")

print("\n== 7 running costs are netted in AnnualOperatingProfitImpactUSD (GI-10 reconciliation)")
s10 = S[(S.ProjectID == "GI-10") & (S.Scenario == "Expected")].iloc[0]
calc = s10.AnnualRevenueImpactUSD * (1 - dist / rr) - P.loc["GI-10", "AnnualRunningCostUSD"]
print(f"  revenue x (1 - distribution %) - running cost = {calc:,.0f} vs dataset {s10.AnnualOperatingProfitImpactUSD:,.0f}")

print("\n== 8 profit a year by 2032 / capex, per move (Expected)")
se = S[(S.Scenario == "Expected") & (S.ProjectID.isin(P.index))].set_index("ProjectID")
y = (se.AnnualOperatingProfitImpactUSD / P.CapexUSD).sort_values(ascending=False)
for pid, v in y.items():
    print(f"  {pid} {P.loc[pid,'ProjectName'][:48]:48s} capex {P.loc[pid,'CapexUSD']/1e6:6.2f}M  a year {se.loc[pid,'AnnualOperatingProfitImpactUSD']/1e6:5.2f}M  {v*100:5.1f} %")
pa = se.loc[A].AnnualOperatingProfitImpactUSD.sum() / P.loc[A].CapexUSD.sum()
t2 = ["GI-04", "GI-05"]
pt2 = se.loc[t2].AnnualOperatingProfitImpactUSD.sum() / P.loc[t2].CapexUSD.sum()
print(f"  package A {pa*100:.1f} % | tranche 2 (GI-04 + GI-05) {pt2*100:.1f} % on {P.loc[t2].CapexUSD.sum()/1e6:.1f}M")
