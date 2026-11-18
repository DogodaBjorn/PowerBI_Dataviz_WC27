import sys, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); ge=r('GuestExperience'); gc=r('GuestComplaints'); pp=r('InvestmentProjectProperties'); p=r('InvestmentProjects'); ren=r('Renovations')
for c in ['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']: mp[c]=mp[c].astype(float)
mp['Year']=mp.Month.dt.year
def hk(y):
    g=mp[mp.Year==y].groupby('HotelID')[['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']].sum()
    return pd.DataFrame({f'Occ{y}':g.RoomsSold/g.RoomsAvailable,f'RevPAR{y}':g.RoomRevenue/g.RoomsAvailable,f'GOP%{y}':1-g.TotalOperatingExpenses/g.TotalRevenue,f'Rev{y}M':g.TotalRevenue/1e6})
k=hk(2025).join(hk(2022)[['RevPAR2022','GOP%2022']])
ge['Year']=ge.Month.dt.year; g25=ge[ge.Year==2025]; w=g25.SurveyResponses.astype(float)
nps=(g25.NetPromoterScore.astype(float)*w).groupby(g25.HotelID).sum()/w.groupby(g25.HotelID).sum(); ov=(g25.OverallScore.astype(float)*w).groupby(g25.HotelID).sum()/w.groupby(g25.HotelID).sum()
gc['Year']=gc.Month.dt.year; c25=gc[gc.Year==2025].groupby('HotelID').Complaints.sum().astype(float)
rs=mp[mp.Year==2025].groupby('HotelID').RoomsSold.sum()
k['NPS25']=nps; k['Overall25']=ov; k['Compl/1kRN']=c25/rs*1000
k=k.join(h.set_index('HotelID')[['HotelName','Brand','Region','Country','LocationType','Rooms','OpeningDate','LastRenovationDate']])
k['RenoAge']=2025-k.LastRenovationDate.dt.year
proj=pp.merge(p[['ProjectID','ProjectName']],on='ProjectID'); proj=proj[~proj.ProjectID.isin(pp.ProjectID.value_counts()[lambda s:s>3].index)]
k['Projects']=proj.groupby('HotelID').ProjectID.apply(lambda s:','.join(s))
for b,g in k.groupby('Brand'):
    print('\n=====',b); print(g.sort_values('RevPAR2025',ascending=False)[['HotelName','Country','LocationType','Rooms','RenoAge','Occ2025','RevPAR2025','RevPAR2022','GOP%2025','GOP%2022','Rev2025M','NPS25','Overall25','Compl/1kRN','Projects']].to_string())
    print('corr RenoAge vs Overall25', g.RenoAge.corr(g.Overall25).round(2), '| RenoAge vs Compl', g.RenoAge.corr(g['Compl/1kRN']).round(2), '| RenoAge vs GOP%', g.RenoAge.corr(g['GOP%2025']).round(2))
print('\n== renovations table sample'); print(ren.head(10).to_string()); print(ren.RenovationType.value_counts()); print(ren.StartDate.min(), ren.EndDate.max())
# renovation effect: hotels renovated 2021-2024: RevPAR before vs after
ren2=ren[(ren.EndDate.dt.year>=2022)&(ren.EndDate.dt.year<=2024)].merge(h[['HotelID','Brand']],on='HotelID')
print('renovations finishing 2022-2024 by brand/type'); print(pd.crosstab(ren2.Brand,ren2.RenovationType))
print('cost by type', ren.groupby('RenovationType').agg(n=('CostUSD','count'),cost=('CostUSD','mean'),oos=('RoomsOutOfServicePct','mean'),months=('StartDate',lambda s: ((ren.loc[s.index,'EndDate']-s).dt.days/30.4).mean())))
# seasonality amplitude per brand (2025 monthly occ max/min)
m=mp[mp.Year==2025].merge(h[['HotelID','Brand']],on='HotelID').groupby(['Brand','Month'])[['RoomsSold','RoomsAvailable']].sum(); occ=(m.RoomsSold/m.RoomsAvailable).unstack(0)
print('\nseasonality 2025 min/max/ratio'); print(pd.DataFrame({'min':occ.min(),'max':occ.max(),'ratio':occ.min()/occ.max(),'months<60%':(occ<0.6).sum()}))
