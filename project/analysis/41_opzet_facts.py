"""Facts for the new report set-up (opzet) of 6 Nov: P1 four-brand comparison, Goodnight Inn
geography, P2 package scatter. Feeds the HTML comp; the model re-derives every figure.

Usage:  python -I project/analysis/41_opzet_facts.py <parquet dir> <packages.csv> <project_economics.csv> <out.json>
        (project_yearly.csv is read from beside project_economics.csv)
Conventions: 2025 = latest full year; trends 2023 -> 2025 (2021 is a depressed base year);
guest scores weighted by SurveyResponses; complaints per 1,000 room nights sold;
margin after distribution = (TotalRevenue - TotalOperatingExpenses - DistributionCost) /
TotalRevenue (the workbook's Contents sheet: MonthlyPerformance excludes distribution costs).
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

d = Path(sys.argv[1]); packs = pd.read_csv(sys.argv[2]); econ = pd.read_csv(sys.argv[3]); out = Path(sys.argv[4])
yearly = pd.read_csv(Path(sys.argv[3]).with_name("project_yearly.csv"))
r = lambda t: pd.read_parquet(d / f"{t}.parquet")
H = r("Hotels"); MP = r("MonthlyPerformance"); BC = r("BookingChannels"); GE = r("GuestExperience"); GC = r("GuestComplaints"); RN = r("Renovations")
P = r("InvestmentProjects"); PP = r("InvestmentProjectProperties"); B = r("Brands")
BR = ["Goodnight Inn", "P&K Select", "Maison d'Or", "Pebble & Pine"]
hb = H.set_index("HotelID").Brand
for t in (MP, BC, GE, GC):
    t["Brand"] = t.HotelID.map(hb); t["Year"] = t.Month.dt.year


def wavg(df, col):
    return float((df[col] * df.SurveyResponses).sum() / df.SurveyResponses.sum())


def brand_year(brand, y):
    m = MP[(MP.Brand == brand) & (MP.Year == y)]; c = BC[(BC.Brand == brand) & (BC.Year == y)]
    g = GE[(GE.Brand == brand) & (GE.Year == y)]; k = GC[(GC.Brand == brand) & (GC.Year == y)]
    rev, opex, dist = m.TotalRevenue.sum(), m.TotalOperatingExpenses.sum(), c.DistributionCost.sum()
    sold, avail, rrev = m.RoomsSold.sum(), m.RoomsAvailable.sum(), m.RoomRevenue.sum()
    ch = c.groupby("Channel").RoomRevenue.sum() / c.RoomRevenue.sum()
    return dict(
        occupancy=sold / avail, adr=rrev / sold, revpar=rrev / avail, revenue=rev, gop=rev - opex,
        gop_margin=(rev - opex) / rev, gop_margin_after=(rev - opex - dist) / rev, dist_cost=dist,
        dist_pct_room=dist / c.RoomRevenue.sum(), dist_pct_rev=dist / rev,
        ota_share=float(ch.get("Online Travel Agencies", 0)),
        direct_share=float(ch.get("Direct Website & App", 0) + ch.get("Direct Phone & Walk-in", 0)),
        nps=wavg(g, "NetPromoterScore"), comfort=wavg(g, "RoomComfortScore"), value=wavg(g, "ValueForMoneyScore"),
        overall=wavg(g, "OverallScore"), complaints_1k=k.Complaints.sum() / sold * 1000,
        room_cond_1k=k[k.Category == "Room condition"].Complaints.sum() / sold * 1000,
    )


def refresh_age(brand):
    h = H[H.Brand == brand]
    yrs = 2025 - h.LastRenovationDate.fillna(h.OpeningDate).dt.year
    return dict(median_years=float(yrs.median()), share_10plus=float((yrs >= 10).mean()), never=int(h.LastRenovationDate.isna().sum()))


brands = {}
for b in BR:
    h = H[H.Brand == b]
    brands[b] = dict(hotels=int(len(h)), rooms=int(h.Rooms.sum()), budget=float(B.set_index("Brand").InvestmentBudgetUSD[b]),
                     y2025=brand_year(b, 2025), y2023=brand_year(b, 2023), y2021=brand_year(b, 2021),
                     trend={y: brand_year(b, y) for y in range(2021, 2026)}, refresh=refresh_age(b),
                     reno_spend_2018=float(RN[(RN.HotelID.map(hb) == b) & (RN.StartDate >= "2018-01-01")].CostUSD.sum()),
                     last_reno_start=str(RN[RN.HotelID.map(hb) == b].StartDate.max().date()))

# ranks across the four brands (1 = best in the direction stated)
better_high = ["occupancy", "adr", "revpar", "gop_margin", "gop_margin_after", "direct_share", "nps", "comfort", "value", "overall"]
better_low = ["dist_pct_room", "dist_pct_rev", "ota_share", "complaints_1k", "room_cond_1k"]
ranks = {}
for k in better_high + better_low:
    vals = {b: brands[b]["y2025"][k] for b in BR}
    order = sorted(vals, key=lambda b: vals[b], reverse=k in better_high)
    ranks[k] = order.index("Goodnight Inn") + 1

# Goodnight Inn geography
gi = H[H.Brand == "Goodnight Inn"].copy()
m25 = MP[(MP.Brand == "Goodnight Inn") & (MP.Year == 2025)].groupby("HotelID")[["RoomsSold", "RoomsAvailable", "RoomRevenue"]].sum()
g25 = GE[(GE.Brand == "Goodnight Inn") & (GE.Year == 2025)].groupby("HotelID").apply(lambda x: pd.Series({"nps": wavg(x, "NetPromoterScore"), "comfort": wavg(x, "RoomComfortScore")}), include_groups=False)
gi = gi.set_index("HotelID").join(m25).join(g25)
gi["occ"] = gi.RoomsSold / gi.RoomsAvailable; gi["revpar"] = gi.RoomRevenue / gi.RoomsAvailable
gi["years"] = 2025 - gi.LastRenovationDate.fillna(gi.OpeningDate).dt.year
proj_of = PP[PP.ProjectID.str.startswith("GI-")].groupby("HotelID").ProjectID.apply(lambda s: sorted(set(s)))
gi["projects"] = proj_of.reindex(gi.index).apply(lambda v: v if isinstance(v, list) else [])
gi["single"] = gi.projects.apply(lambda v: [p for p in v if p in ("GI-04", "GI-05", "GI-06", "GI-07", "GI-02")])
hotels = [dict(id=i, name=x.HotelName.replace("Goodnight Inn ", ""), city=x.City, country=x.Country, region=x.Region, type=x.LocationType,
               lat=float(x.Latitude), lon=float(x.Longitude), rooms=int(x.Rooms), occ=float(x.occ), revpar=float(x.revpar),
               nps=float(x.nps), comfort=float(x.comfort), years=int(x.years), projects=x.single) for i, x in gi.iterrows()]
loc = gi.groupby("LocationType").agg(hotels=("Rooms", "size"), rooms=("Rooms", "sum"), sold=("RoomsSold", "sum"), avail=("RoomsAvailable", "sum"), rrev=("RoomRevenue", "sum"))
loc = {t: dict(hotels=int(x.hotels), rooms=int(x.rooms), occ=float(x.sold / x.avail), revpar=float(x.rrev / x.avail)) for t, x in loc.iterrows()}
reg = gi.groupby("Region").agg(hotels=("Rooms", "size"), sold=("RoomsSold", "sum"), avail=("RoomsAvailable", "sum"))
reg = {t: dict(hotels=int(x.hotels), occ=float(x.sold / x.avail)) for t, x in reg.iterrows()}
ref = gi[gi.projects.apply(lambda v: "GI-07" in v)]
comfort_corr = float(np.corrcoef(gi.dropna(subset=["LastRenovationDate"]).years, gi.dropna(subset=["LastRenovationDate"]).comfort)[0, 1])

# P2
proj = []
for _, x in P[P.Brand == "Goodnight Inn"].sort_values("ProjectID").iterrows():
    e = econ[(econ.ProjectID == x.ProjectID)].set_index("Scenario")
    proj.append(dict(id=x.ProjectID, name=x.ProjectName, category=x.Category, growth=x.GrowthInitiative, capex=float(x.CapexUSD),
                     duration=int(x.DurationMonths), oos=float(x.RoomsOutOfServicePct), added=int(x.AddedRooms),
                     depends=x.DependsOn if isinstance(x.DependsOn, str) else None,
                     start=e.Start["Expected"], live=e.Live["Expected"], hotels=int(e.Hotels["Expected"]),
                     npv={s: float(e.NPV[s]) for s in e.index}, runrate={s: float(e.RunRate2032[s]) for s in e.index},
                     sat={s: float(e.SatPts[s]) for s in e.index},
                     net_by_year={s: {int(y): float(v) for y, v in yearly[(yearly.ProjectID == x.ProjectID) & (yearly.Scenario == s)].set_index("Year").Net.items()} for s in e.index}, payback={s: (None if pd.isna(e.Payback[s]) else int(e.Payback[s])) for s in e.index}))
scatter = [dict(id=x.PackageID, capex=float(x.CapexUSD), refresh=x.ContainsRefresh == "Yes", n=int(x.Projects),
                npv={"Low": float(x.NPV_Low), "Expected": float(x.NPV_Expected), "High": float(x.NPV_High)},
                rr={"Low": float(x.RunRate_Low), "Expected": float(x.RunRate_Expected), "High": float(x.RunRate_High)},
                rated=int(x.HotelsRated), added=int(x.RoomsAdded)) for _, x in packs.iterrows()]

facts = dict(brands=brands, ranks=ranks, hotels=hotels, location=loc, region=reg,
             refresh10=dict(n=int(len(ref)), rooms=int(ref.Rooms.sum()), comfort=float(ref.comfort.mean()), comfort_rest=float(gi[~gi.index.isin(ref.index)].comfort.mean()),
                            neg_nps=int((ref.nps < 0).sum()), neg_nps_all=int((gi.nps < 0).sum())),
             comfort_years_r=comfort_corr, projects=proj, packages=scatter)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(facts, indent=1, default=float), encoding="utf-8")
g = brands["Goodnight Inn"]["y2025"]
print("GI 2025:", {k: round(v, 4) for k, v in g.items()})
print("ranks (1 = best of four):", ranks)
for b in BR:
    y = brands[b]["y2025"]
    print(f"{b:14} occ {y['occupancy']:.1%} ADR {y['adr']:.0f} RevPAR {y['revpar']:.0f} GOP% {y['gop_margin']:.1%} after {y['gop_margin_after']:.1%} dist/room {y['dist_pct_room']:.1%} OTA {y['ota_share']:.1%} direct {y['direct_share']:.1%} NPS {y['nps']:+.1f} comfort {y['comfort']:.2f} value {y['value']:.2f} compl {y['complaints_1k']:.2f} roomcond {y['room_cond_1k']:.2f} refresh {brands[b]['refresh']}")
print("location:", loc); print("region:", reg); print("refresh10:", facts["refresh10"], "r(years, comfort) dated:", round(comfort_corr, 3))
print("written", out)
