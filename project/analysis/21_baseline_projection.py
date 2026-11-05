import sys, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); fa=r('FinanceAssumptions'); bc=r('BookingChannels')
gi=h[h.Brand=='Goodnight Inn']; ids=set(gi.HotelID)
mp=mp[mp.HotelID.isin(ids)].copy()
for c in ['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']: mp[c]=mp[c].astype(float)
mp['Year']=mp.Month.dt.year; m25=mp[mp.Year==2025].merge(gi[['HotelID','HotelName','Region','Rooms','LocationType']],on='HotelID')
# do-nothing baseline per hotel: nights grow with regional demand growth (capped at 97% occupancy = max observed), ADR with ADR inflation, CPOR with cost inflation
cap=0.97; base=m25.groupby(['HotelID','HotelName','Region','LocationType'])[['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']].sum().reset_index()
base['RevPOR']=base.TotalRevenue/base.RoomsSold; base['CPOR']=base.TotalOperatingExpenses/base.RoomsSold; base['Occ']=base.RoomsSold/base.RoomsAvailable
rows=[]
for _,b in base.iterrows():
    dem=1.0; adr=1.0; cost=1.0
    for y in range(2026,2033):
        a=fa[(fa.Year==y)&(fa.Region==b.Region)].iloc[0]; dem*=1+a.MarketDemandGrowthPct; adr*=1+a.ADRInflationPct; cost*=1+a.CostInflationPct
        want=b.RoomsSold*dem; sold=min(want,b.RoomsAvailable*cap); unmet=want-sold
        rows.append(dict(HotelID=b.HotelID,HotelName=b.HotelName,Region=b.Region,LocationType=b.LocationType,Year=y,RoomsAvailable=b.RoomsAvailable,Demand=want,Sold=sold,Unmet=unmet,Rev=sold*b.RevPOR*adr,Opex=sold*b.CPOR*cost,RevPOR=b.RevPOR*adr,CPOR=b.CPOR*cost,UnmetRev=unmet*b.RevPOR*adr))
P=pd.DataFrame(rows); P['GOP']=P.Rev-P.Opex
g=P.groupby('Year')[['RoomsAvailable','Demand','Sold','Unmet','Rev','Opex','GOP','UnmetRev']].sum(); g['Occ']=g.Sold/g.RoomsAvailable; g['DemandOcc']=g.Demand/g.RoomsAvailable; g['GOP%']=g.GOP/g.Rev
print('== GI do-nothing baseline (2025 unit economics x FinanceAssumptions; capacity cap 97%)'); print(g[['Occ','DemandOcc','Unmet','UnmetRev','Rev','GOP','GOP%']].assign(Rev=lambda x:x.Rev/1e6,GOP=lambda x:x.GOP/1e6,UnmetRev=lambda x:x.UnmetRev/1e6).to_string())
print('2025 actual: Rev 212.8M GOP 94.4M GOP% 44.4% Occ 79.4%')
print('\n== hotels hitting the cap by 2032 (unmet room nights 2032)'); x=P[P.Year==2032].sort_values('Unmet',ascending=False); print(x[x.Unmet>0][['HotelName','LocationType','Region','RoomsAvailable','Demand','Sold','Unmet','UnmetRev']].assign(UnmetRev=lambda v:v.UnmetRev/1e6).head(20).to_string(index=False)); print('hotels capped 2032:', int((x.Unmet>0).sum()), 'of 50; unmet nights', int(x.Unmet.sum()), 'unmet revenue M', round(x.UnmetRev.sum()/1e6,1))
# first year each extension candidate hits the cap
for nm in ['Goodnight Inn London Gatwick Airport','Goodnight Inn Toronto Pearson Airport','Goodnight Inn Montréal-Trudeau Airport','Goodnight Inn Kingston']:
    y=P[(P.HotelName==nm)&(P.Unmet>0)].Year.min(); print(nm, 'first capped year:', y, '| 2032 demand occ', round(P[(P.HotelName==nm)&(P.Year==2032)].Demand.iloc[0]/P[(P.HotelName==nm)&(P.Year==2032)].RoomsAvailable.iloc[0],3))
# margin erosion decomposition: ADR inflation vs cost inflation only (no volume), NA
print('\nNA ADR inflation 2026-32 cumulative', round(np.prod(1+fa[fa.Region=='North America'].ADRInflationPct)-1,4), 'cost inflation', round(np.prod(1+fa[fa.Region=='North America'].CostInflationPct)-1,4), 'demand', round(np.prod(1+fa[fa.Region=='North America'].MarketDemandGrowthPct)-1,4))
# OTA drift continuation: linear trend of OTA share +4.25pts/yr -> 2032? and cost
bc=bc[bc.HotelID.isin(ids)].copy(); bc['Year']=bc.Month.dt.year
for c in ['RoomRevenue','DistributionCost']: bc[c]=bc[c].astype(float)
t=bc.groupby(['Year','Channel']).RoomRevenue.sum().unstack(); sh=t.div(t.sum(axis=1),axis=0); print('\nOTA share by year', sh['Online Travel Agencies'].round(3).to_dict()); slope=(sh.loc[2025,'Online Travel Agencies']-sh.loc[2021,'Online Travel Agencies'])/4; print('slope pts/yr', round(slope,4), '-> naive 2032 share', round(sh.loc[2025,'Online Travel Agencies']+7*slope,3), '(trend extrapolation, label as scenario; realistic cap ~?)')
