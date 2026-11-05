import sys, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
s=r('InvestmentScenarios'); p=r('InvestmentProjects'); pp=r('InvestmentProjectProperties'); h=r('Hotels'); mp=r('MonthlyPerformance')
print('== scenario inputs (Expected)'); print(s[s.Scenario=='Expected'].drop(columns=['Scenario']).to_string(index=False))
# reconcile: 2025 actuals of the project's properties
mp25=mp[mp.Month.dt.year==2025].copy()
for c in ['RoomsAvailable','RoomsSold','RoomRevenue','FoodBeverageRevenue','OtherRevenue','TotalRevenue','TotalOperatingExpenses']: mp25[c]=mp25[c].astype(float)
base=mp25.groupby('HotelID')[['RoomsAvailable','RoomsSold','RoomRevenue','FoodBeverageRevenue','OtherRevenue','TotalRevenue','TotalOperatingExpenses']].sum()
bc=r('BookingChannels'); bc=bc[bc.Month.dt.year==2025].groupby('HotelID')[['RoomRevenue','DistributionCost']].sum().astype(float); base['DistCost']=bc.DistributionCost
rows=[]
for _,pr in p.iterrows():
    hs=pp[pp.ProjectID==pr.ProjectID].HotelID.tolist()
    b=base.loc[base.index.isin(hs)].sum() if hs else None
    e=s[(s.ProjectID==pr.ProjectID)&(s.Scenario=='Expected')].iloc[0]
    if b is not None and len(hs):
        occ=b.RoomsSold/b.RoomsAvailable; adr=b.RoomRevenue/b.RoomsSold
        # model guess: room rev impact = RoomsAvailable*(occ+dOcc)*(adr*(1+dADR)) - RoomRevenue ; added rooms: AddedRooms*365*AddedRoomsOccupancy*adr(1+dADR)
        newrr=b.RoomsAvailable*(occ+e.OccupancyChangePts)*adr*(1+e.ADRChangePct)-b.RoomRevenue
        addrr=pr.AddedRooms*365*(e.AddedRoomsOccupancy if pd.notna(e.AddedRoomsOccupancy) else 0)*adr*(1+e.ADRChangePct)
        fb=b.FoodBeverageRevenue*e.FoodBeverageRevenueChangePct; oth=b.OtherRevenue*e.OtherRevenueChangePct
        guess=newrr+addrr+fb+oth
        rows.append(dict(ProjectID=pr.ProjectID,nH=len(hs),occ25=occ,adr25=adr,TotRev25=b.TotalRevenue,Opex25=b.TotalOperatingExpenses,DistC25=b.DistCost,dOcc=e.OccupancyChangePts,dADR=e.ADRChangePct,roomRevΔ=newrr,addedRoomsΔ=addrr,fbΔ=fb,othΔ=oth,guessRev=guess,givenRev=e.AnnualRevenueImpactUSD,ratio=guess/e.AnnualRevenueImpactUSD if e.AnnualRevenueImpactUSD else np.nan,givenOP=e.AnnualOperatingProfitImpactUSD,opexΔ=e.OperatingExpenseChangePct,distΔ=e.DistributionCostChangePts,runCost=pr.AnnualRunningCostUSD))
    else:
        rows.append(dict(ProjectID=pr.ProjectID,nH=0,givenRev=e.AnnualRevenueImpactUSD,givenOP=e.AnnualOperatingProfitImpactUSD,newOcc=e.NewPropertyOccupancy,newADR=e.NewPropertyADR,addedRooms=pr.AddedRooms,guessRev=pr.AddedRooms*365*e.NewPropertyOccupancy*e.NewPropertyADR if pd.notna(e.NewPropertyOccupancy) else np.nan))
df=pd.DataFrame(rows); print('== reconciliation'); print(df.to_string(index=False))
