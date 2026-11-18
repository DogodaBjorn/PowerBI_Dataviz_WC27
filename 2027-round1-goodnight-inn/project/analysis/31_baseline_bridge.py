import sys, json, pandas as pd
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); fa=r('FinanceAssumptions'); gi=h[h.Brand=='Goodnight Inn']; ids=set(gi.HotelID)
mp=mp[mp.HotelID.isin(ids)].copy()
for c in ['RoomsAvailable','RoomsSold','TotalRevenue','TotalOperatingExpenses']: mp[c]=mp[c].astype(float)
m25=mp[mp.Month.dt.year==2025].merge(gi[['HotelID','Region']],on='HotelID').groupby(['HotelID','Region'])[['RoomsAvailable','RoomsSold','TotalRevenue','TotalOperatingExpenses']].sum().reset_index()
cap=0.97; vol=price=costvol=costinf=0.0; rev25=m25.TotalRevenue.sum(); opex25=m25.TotalOperatingExpenses.sum()
for _,b in m25.iterrows():
    dem=adr=cost=1.0
    for y in range(2026,2033):
        a=fa[(fa.Year==y)&(fa.Region==b.Region)].iloc[0]; dem*=1+a.MarketDemandGrowthPct; adr*=1+a.ADRInflationPct; cost*=1+a.CostInflationPct
    sold=min(b.RoomsSold*dem,b.RoomsAvailable*cap); ratio=sold/b.RoomsSold
    vol+=b.TotalRevenue*(ratio-1); price+=b.TotalRevenue*ratio*(adr-1); costvol-=b.TotalOperatingExpenses*(ratio-1); costinf-=b.TotalOperatingExpenses*ratio*(cost-1)
gop25=rev25-opex25; gop32=gop25+vol+price+costvol+costinf
out=dict(gop2025=round(gop25/1e6,2),volume=round(vol/1e6,2),price=round(price/1e6,2),costVolume=round(costvol/1e6,2),costInflation=round(costinf/1e6,2),gop2032=round(gop32/1e6,2))
J=json.load(open(sys.argv[2])); J['baselineBridge']=out; json.dump(J,open(sys.argv[2],'w'),indent=0,default=str); print(out)
