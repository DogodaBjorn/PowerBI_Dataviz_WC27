import sys, itertools, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); bc=r('BookingChannels'); gs=r('GuestSegments'); ge=r('GuestExperience'); gc=r('GuestComplaints'); ren=r('Renovations'); p=r('InvestmentProjects'); pp=r('InvestmentProjectProperties'); s=r('InvestmentScenarios')
gi=h[h.Brand=='Goodnight Inn'].copy(); ids=set(gi.HotelID)
num=['RoomsAvailable','RoomsSold','RoomRevenue','FoodBeverageRevenue','OtherRevenue','TotalRevenue','StaffCost','EnergyCost','MaintenanceCost','FoodBeverageCost','OtherOperatingCost','TotalOperatingExpenses']
mp=mp[mp.HotelID.isin(ids)].copy(); 
for c in num: mp[c]=mp[c].astype(float)
mp['Year']=mp.Month.dt.year
print('== GI brand by year (full)'); g=mp.groupby('Year')[num].sum(); out=pd.DataFrame({'Occ':g.RoomsSold/g.RoomsAvailable,'ADR':g.RoomRevenue/g.RoomsSold,'RevPAR':g.RoomRevenue/g.RoomsAvailable,'RoomRev_M':g.RoomRevenue/1e6,'TotRev_M':g.TotalRevenue/1e6,'GOP_M':(g.TotalRevenue-g.TotalOperatingExpenses)/1e6,'GOP%':1-g.TotalOperatingExpenses/g.TotalRevenue,'Staff%':g.StaffCost/g.TotalRevenue,'Energy%':g.EnergyCost/g.TotalRevenue,'Maint%':g.MaintenanceCost/g.TotalRevenue,'Other%':g.OtherOperatingCost/g.TotalRevenue,'FBcost%':g.FoodBeverageCost/g.TotalRevenue,'CPOR':g.TotalOperatingExpenses/g.RoomsSold,'RoomsAvail':g.RoomsAvailable}); print(out.to_string())
print('\n== GI quarterly RevPAR / Occ / GOP% 2023-2025'); q=mp[mp.Year>=2023].groupby(mp.Month.dt.to_period('Q'))[num].sum(); print(pd.DataFrame({'Occ':q.RoomsSold/q.RoomsAvailable,'RevPAR':q.RoomRevenue/q.RoomsAvailable,'GOP%':1-q.TotalOperatingExpenses/q.TotalRevenue}).to_string())
# channels in $
bc=bc[bc.HotelID.isin(ids)].copy(); 
for c in ['Bookings','RoomNights','RoomRevenue','DistributionCost']: bc[c]=bc[c].astype(float)
bc['Year']=bc.Month.dt.year; t=bc.groupby(['Year','Channel'])[['Bookings','RoomNights','RoomRevenue','DistributionCost']].sum()
t['RevShare']=t.RoomRevenue/t.groupby(level=0).RoomRevenue.transform('sum'); t['Cost%']=t.DistributionCost/t.RoomRevenue; t['ADR']=t.RoomRevenue/t.RoomNights; t['Nights/booking']=t.RoomNights/t.Bookings
print('\n== GI channels by year'); print(t.to_string())
tt=t.groupby(level=0)[['RoomRevenue','DistributionCost']].sum(); tt['Dist%']=tt.DistributionCost/tt.RoomRevenue; print(tt.to_string())
# counterfactual: 2025 channel mix at 2021 shares -> distribution cost
m21=t.loc[2021,'RevShare']; c25=t.loc[2025,'Cost%']; rr25=tt.loc[2025,'RoomRevenue']; cf=(m21*c25).sum()*rr25; print(f'\n2025 dist cost actual {tt.loc[2025,"DistributionCost"]/1e6:.2f}M ; at 2021 mix {cf/1e6:.2f}M ; delta {(tt.loc[2025,"DistributionCost"]-cf)/1e6:.2f}M')
print('each 1pt of room revenue moved OTA->direct web saves', (0.18-0.04)*0.01*rr25/1e6, 'M/yr')
# segments
gs=gs[gs.HotelID.isin(ids)].copy(); gs['Year']=gs.Month.dt.year
for c in ['Bookings','RoomNights','RoomRevenue']: gs[c]=gs[c].astype(float)
sg=gs.groupby(['Year','Segment'])[['RoomNights','RoomRevenue']].sum(); sg['share']=sg.RoomNights/sg.groupby(level=0).RoomNights.transform('sum'); sg['ADR']=sg.RoomRevenue/sg.RoomNights; print('\n== GI segments'); print(sg[['share','ADR']].unstack(0).to_string())
# guest experience
ge=ge[ge.HotelID.isin(ids)].copy(); ge['Year']=ge.Month.dt.year; w=ge.SurveyResponses.astype(float)
sc=['OverallScore','CleanlinessScore','ServiceScore','RoomComfortScore','AmenitiesScore','ValueForMoneyScore','NetPromoterScore']
g=ge.groupby('Year'); print('\n== GI guest scores (weighted)'); print(pd.DataFrame({c:(ge[c].astype(float)*w).groupby(ge.Year).sum()/g.SurveyResponses.sum() for c in sc}).to_string())
gc=gc[gc.HotelID.isin(ids)].copy(); gc['Year']=gc.Month.dt.year; cy=gc.groupby(['Year','Category']).Complaints.sum().astype(float).unstack(0); rn=mp.groupby('Year').RoomsSold.sum(); print('\n== GI complaints per 1k room nights by category'); print((cy/rn*1000).round(2).to_string()); print('total per 1k', (cy.sum()/rn*1000).round(2).to_dict())
# projects -> hotels
gp=p[p.Brand=='Goodnight Inn']; k25=mp[mp.Year==2025].groupby('HotelID')[num].sum()
kh=pd.DataFrame({'Occ25':k25.RoomsSold/k25.RoomsAvailable,'RevPAR25':k25.RoomRevenue/k25.RoomsAvailable,'GOP%25':1-k25.TotalOperatingExpenses/k25.TotalRevenue,'Rev25M':k25.TotalRevenue/1e6}).join(gi.set_index('HotelID')[['HotelName','Country','LocationType','Rooms','OpeningDate','LastRenovationDate']])
w25=ge[ge.Year==2025]; ww=w25.SurveyResponses.astype(float); kh['NPS25']=(w25.NetPromoterScore.astype(float)*ww).groupby(w25.HotelID).sum()/ww.groupby(w25.HotelID).sum()
kh['YearsSinceReno']=2025-kh.LastRenovationDate.dt.year; kh['YearsOpen']=2025-kh.OpeningDate.dt.year
for pid in ['GI-02','GI-07']:
    hs=pp[pp.ProjectID==pid].HotelID; print(f'\n== {pid} properties ({len(hs)})'); print(kh.loc[kh.index.isin(hs)].sort_values('YearsSinceReno',ascending=False)[['HotelName','Country','LocationType','Rooms','YearsOpen','YearsSinceReno','Occ25','RevPAR25','GOP%25','NPS25']].to_string())
print('\n== hotels with no renovation record'); print(kh[kh.LastRenovationDate.isna()][['HotelName','YearsOpen','Occ25','NPS25']].to_string())
# extension candidates monthly occupancy 2025 + 2024
for hid,nm in [('GI027','Gatwick'),('GI002','Toronto'),('GI009','Kingston'),('GI001','Montreal')]:
    x=mp[(mp.HotelID==hid)&(mp.Year>=2024)]; occ=(x.RoomsSold/x.RoomsAvailable); print(nm,'2024-25 monthly occ:', occ.round(2).tolist(), '| months>=90%:', int((occ>=0.9).sum()), '/24')
# 2021 renovation cohort natural experiment within GI
rc=ren[ren.HotelID.isin(ids)&(ren.EndDate>='2021-01-01')].HotelID.tolist(); print('\n== 2021 renovation cohort', [kh.loc[i,'HotelName'] for i in rc])
yk=mp.groupby(['HotelID','Year'])[num].sum(); yk=pd.DataFrame({'RevPAR':yk.RoomRevenue/yk.RoomsAvailable,'GOP%':1-yk.TotalOperatingExpenses/yk.TotalRevenue}).reset_index()
coh=yk[yk.HotelID.isin(rc)].groupby('Year')[['RevPAR','GOP%']].mean(); peers=yk[~yk.HotelID.isin(rc)].groupby('Year')[['RevPAR','GOP%']].mean(); print(pd.concat({'renovated2021':coh,'peers':peers},axis=1).to_string())
gw=ge.copy(); gw['w']=gw.SurveyResponses.astype(float)
for lbl,sel in [('renovated2021',gw.HotelID.isin(rc)),('peers',~gw.HotelID.isin(rc))]:
    x=gw[sel]; print(lbl,'NPS by year', ((x.NetPromoterScore.astype(float)*x.w).groupby(x.Year).sum()/x.w.groupby(x.Year).sum()).round(1).to_dict())
print('NPS 2025 by years-since-reno bucket'); print(kh.assign(b=pd.cut(kh.YearsSinceReno,[0,5,9,15])).groupby('b',observed=True).agg(n=('NPS25','count'),NPS=('NPS25','mean'),Occ=('Occ25','mean'),GOP=('GOP%25','mean')).round(2).to_string())
print('corr YearsSinceReno vs NPS25', kh.YearsSinceReno.corr(kh.NPS25).round(2), '| YearsOpen vs NPS25 (no-reno hotels use open date)', kh.YearsSinceReno.fillna(kh.YearsOpen).corr(kh.NPS25).round(2))
# seasonality GI 2025 by location type
m=mp[mp.Year==2025].merge(gi[['HotelID','LocationType']],on='HotelID').groupby(['LocationType',mp[mp.Year==2025].Month.dt.month])[['RoomsSold','RoomsAvailable']].sum(); print('\n== GI occupancy by location type x month 2025'); print((m.RoomsSold/m.RoomsAvailable).unstack().round(2).to_string())
# region / location type KPI 2025
m=mp[mp.Year==2025].merge(gi[['HotelID','LocationType','Region']],on='HotelID')
for col in ['LocationType','Region']:
    g=m.groupby(col)[num].sum(); print(f'\n== GI 2025 by {col}'); print(pd.DataFrame({'hotels':m.groupby(col).HotelID.nunique(),'Occ':g.RoomsSold/g.RoomsAvailable,'ADR':g.RoomRevenue/g.RoomsSold,'RevPAR':g.RoomRevenue/g.RoomsAvailable,'GOP%':1-g.TotalOperatingExpenses/g.TotalRevenue,'Rev_M':g.TotalRevenue/1e6}).to_string())
# scenarios full for GI + through-2032 economics per scenario
print('\n== GI scenario table'); print(s[s.ProjectID.str.startswith('GI')].sort_values(['ProjectID','Scenario']).to_string(index=False))
mp25=mp[mp.Year==2025].groupby('HotelID').TotalRevenue.sum(); MONTHS=pd.period_range('2027-01','2032-12',freq='M')
def econ(pr,scen,start=None):
    e=s[(s.ProjectID==pr.ProjectID)&(s.Scenario==scen)].iloc[0]; op=float(e.AnnualOperatingProfitImpactUSD)
    start=pd.Period(start or pr.EarliestStart,freq='M'); D=int(pr.DurationMonths); comp=start+D; hs=pp[pp.ProjectID==pr.ProjectID].HotelID.tolist(); prm=mp25[mp25.index.isin(hs)].sum()/12 if hs else 0.0
    cap=pd.Series(0.0,index=MONTHS); dis=pd.Series(0.0,index=MONTHS); ben=pd.Series(0.0,index=MONTHS)
    for m in MONTHS:
        if start<=m<comp: cap[m]-=float(pr.CapexUSD)/D; dis[m]-=float(pr.RoomsOutOfServicePct)*prm
        elif m>=comp: k=(m-comp).n; ben[m]+=op/12*(0.5 if k<12 else 0.85 if k<24 else 1.0)
    tot=cap+dis+ben; cum=tot.cumsum(); pb=next((str(m) for m,v in cum.items() if v>=0 and m>=comp), None)
    by=tot.groupby(tot.index.year).sum(); npv=sum(v/1.08**(y-2026) for y,v in by.items())
    return dict(comp=str(comp),capex=cap.sum()/1e6,disrupt=dis.sum()/1e6,ben=ben.sum()/1e6,net=tot.sum()/1e6,npv=npv/1e6,run2032=ben[ben.index.year==2032].sum()/1e6,payback=pb, simple_pb_years=(float(pr.CapexUSD)/op if op>0 else np.nan))
rows=[]
for _,pr in gp.iterrows():
    for sc in ['Low','Expected','High']: c=econ(pr,sc); c.update(ProjectID=pr.ProjectID,Scenario=sc,Capex_M=pr.CapexUSD/1e6,Growth=pr.GrowthInitiative); rows.append(c)
E=pd.DataFrame(rows); print('\n== GI per-project economics through 2032 (2025 $, earliest start, OOS = full revenue loss)'); print(E.set_index(['ProjectID','Scenario']).to_string())
# candidate portfolios
cands={'A app+rms+kiosk+Gatwick+Toronto+refresh':['GI-01','GI-10','GI-02','GI-05','GI-04','GI-07'],'A+breakfast':['GI-01','GI-10','GI-02','GI-05','GI-04','GI-07','GI-09'],'B energy instead of refresh':['GI-01','GI-10','GI-02','GI-05','GI-04','GI-03','GI-09'],'C digital+extensions+energy+breakfast (no refresh)':['GI-01','GI-10','GI-02','GI-05','GI-04','GI-06','GI-03','GI-09'],'D Boston new hotel + digital + Gatwick':['GI-01','GI-10','GI-02','GI-05','GI-08','GI-09']}
print('\n== candidate portfolios'); 
for nm,ids_ in cands.items():
    x=E[E.ProjectID.isin(ids_)].groupby('Scenario')[['capex','disrupt','ben','net','npv','run2032']].sum(); print(f'{nm}: capex {-x.loc["Expected","capex"]:.1f}M growth={ (gp[gp.ProjectID.isin(ids_)].GrowthInitiative=="Yes").sum()} n={len(ids_)}'); print(x.round(1).to_string())
