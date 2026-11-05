import sys, json, pandas as pd, numpy as np
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); bc=r('BookingChannels'); ge=r('GuestExperience'); gc=r('GuestComplaints'); ren=r('Renovations'); p=r('InvestmentProjects'); pp=r('InvestmentProjectProperties'); s=r('InvestmentScenarios'); fa=r('FinanceAssumptions'); gs=r('GuestSegments'); b=r('Brands')
gi=h[h.Brand=='Goodnight Inn'].copy(); ids=set(gi.HotelID); out={}
num=['RoomsAvailable','RoomsSold','RoomRevenue','FoodBeverageRevenue','OtherRevenue','TotalRevenue','StaffCost','EnergyCost','MaintenanceCost','FoodBeverageCost','OtherOperatingCost','TotalOperatingExpenses']
mpa=mp.copy()
for c in num: mpa[c]=mpa[c].astype(float)
mpa['Year']=mpa.Month.dt.year; mpa=mpa.merge(h[['HotelID','Brand']],on='HotelID')
# brand benchmarks 2025 + GI yearly
def kp(g): s_=g[num].sum(); return dict(occ=round(s_.RoomsSold/s_.RoomsAvailable,4),adr=round(s_.RoomRevenue/s_.RoomsSold,2),revpar=round(s_.RoomRevenue/s_.RoomsAvailable,2),rev=round(s_.TotalRevenue/1e6,2),gop=round((s_.TotalRevenue-s_.TotalOperatingExpenses)/1e6,2),gopm=round(1-s_.TotalOperatingExpenses/s_.TotalRevenue,4),cpor=round(s_.TotalOperatingExpenses/s_.RoomsSold,2),revpor=round(s_.TotalRevenue/s_.RoomsSold,2),staff=round(s_.StaffCost/s_.TotalRevenue,4),energy=round(s_.EnergyCost/s_.TotalRevenue,4),maint=round(s_.MaintenanceCost/s_.TotalRevenue,4),other=round(s_.OtherOperatingCost/s_.TotalRevenue,4),fbcost=round(s_.FoodBeverageCost/s_.TotalRevenue,4),roomrev=round(s_.RoomRevenue/1e6,2))
m=mpa[mpa.Brand=='Goodnight Inn']; out['giYears']={int(y):kp(g) for y,g in m.groupby('Year')}
out['brands2025']={br:kp(g) for br,g in mpa[mpa.Year==2025].groupby('Brand')}
# brand yearly margin for all brands
out['brandMargin']={br:{int(y):round(1-g.TotalOperatingExpenses.sum()/g.TotalRevenue.sum(),4) for y,g in gg.groupby('Year')} for br,gg in mpa.groupby('Brand')}
# GOP bridge 2024->2025 GI
y24=m[m.Year==2024][num].sum(); y25=m[m.Year==2025][num].sum()
out['bridge']={'rev2024':round(y24.TotalRevenue/1e6,2),'gop2024':round((y24.TotalRevenue-y24.TotalOperatingExpenses)/1e6,2),'gop2025':round((y25.TotalRevenue-y25.TotalOperatingExpenses)/1e6,2),'revenue':round((y25.TotalRevenue-y24.TotalRevenue)/1e6,2),'staff':round(-(y25.StaffCost-y24.StaffCost)/1e6,2),'energy':round(-(y25.EnergyCost-y24.EnergyCost)/1e6,2),'maintenance':round(-(y25.MaintenanceCost-y24.MaintenanceCost)/1e6,2),'fbcost':round(-(y25.FoodBeverageCost-y24.FoodBeverageCost)/1e6,2),'other':round(-(y25.OtherOperatingCost-y24.OtherOperatingCost)/1e6,2)}
# channels
bcg=bc[bc.HotelID.isin(ids)].copy(); bcg['Year']=bcg.Month.dt.year
for c in ['Bookings','RoomNights','RoomRevenue','DistributionCost']: bcg[c]=bcg[c].astype(float)
t=bcg.groupby(['Year','Channel'])[['RoomNights','RoomRevenue','DistributionCost']].sum().reset_index()
tot=t.groupby('Year').RoomRevenue.transform('sum'); t['share']=t.RoomRevenue/tot; t['adr']=t.RoomRevenue/t.RoomNights; t['rate']=t.DistributionCost/t.RoomRevenue
out['channels']=[dict(year=int(x.Year),channel=x.Channel,share=round(x.share,4),nights=int(x.RoomNights),rev=round(x.RoomRevenue/1e6,3),cost=round(x.DistributionCost/1e6,3),adr=round(x.adr,2),rate=round(x.rate,3)) for x in t.itertuples()]
tt=t.groupby('Year')[['RoomRevenue','DistributionCost']].sum(); out['distCost']={int(y):dict(rev=round(v.RoomRevenue/1e6,2),cost=round(v.DistributionCost/1e6,2),pct=round(v.DistributionCost/v.RoomRevenue,4)) for y,v in tt.iterrows()}
sh21=t[t.Year==2021].set_index('Channel').share; rate25=t[t.Year==2025].set_index('Channel').rate; rr25=tt.loc[2025,'RoomRevenue']; out['distAt2021Mix']=round(float((sh21*rate25).sum()*rr25/1e6),2)
# brand distribution pct 2025
bca=bc.merge(h[['HotelID','Brand']],on='HotelID'); bca=bca[bca.Month.dt.year==2025].groupby('Brand')[['RoomRevenue','DistributionCost']].sum().astype(float); out['brandDist2025']={k:round(v.DistributionCost/v.RoomRevenue,4) for k,v in bca.iterrows()}
# OTA share per GI hotel 2025
oh=bcg[bcg.Year==2025].groupby(['HotelID','Channel']).RoomRevenue.sum().unstack(); out['otaShareHotels']={k:round(v,4) for k,v in (oh['Online Travel Agencies']/oh.sum(axis=1)).items()}
# segments GI
gsg=gs[gs.HotelID.isin(ids)].copy(); gsg['Year']=gsg.Month.dt.year
for c in ['RoomNights','RoomRevenue']: gsg[c]=gsg[c].astype(float)
sg=gsg.groupby(['Year','Segment'])[['RoomNights','RoomRevenue']].sum().reset_index(); sg['share']=sg.RoomNights/sg.groupby('Year').RoomNights.transform('sum'); sg['adr']=sg.RoomRevenue/sg.RoomNights
out['segments']=[dict(year=int(x.Year),segment=x.Segment,share=round(x.share,4),adr=round(x.adr,2)) for x in sg.itertuples()]
# guest experience GI
geg=ge[ge.HotelID.isin(ids)].copy(); geg['Year']=geg.Month.dt.year; w=geg.SurveyResponses.astype(float)
sc=['OverallScore','CleanlinessScore','ServiceScore','RoomComfortScore','AmenitiesScore','ValueForMoneyScore','NetPromoterScore']
out['scores']={int(y):{c:round(float((g[c].astype(float)*g.SurveyResponses.astype(float)).sum()/g.SurveyResponses.astype(float).sum()),3) for c in sc} for y,g in geg.groupby('Year')}
# brand NPS yearly
gea=ge.merge(h[['HotelID','Brand']],on='HotelID'); gea['Year']=gea.Month.dt.year
out['brandNPS']={br:{int(y):round(float((g.NetPromoterScore.astype(float)*g.SurveyResponses.astype(float)).sum()/g.SurveyResponses.astype(float).sum()),2) for y,g in gg.groupby('Year')} for br,gg in gea.groupby('Brand')}
# complaints per 1k GI
gcg=gc[gc.HotelID.isin(ids)].copy(); gcg['Year']=gcg.Month.dt.year; cy=gcg.groupby(['Year','Category']).Complaints.sum().astype(float).unstack(0); rn=m.groupby('Year').RoomsSold.sum()
out['complaints']={cat:{int(y):round(float(cy.loc[cat,y]/rn[y]*1000),3) for y in cy.columns} for cat in cy.index}
# hotels GI
k25=m[m.Year==2025].groupby('HotelID')[num].sum(); g25=geg[geg.Year==2025]; ww=g25.SurveyResponses.astype(float)
nps=(g25.NetPromoterScore.astype(float)*ww).groupby(g25.HotelID).sum()/ww.groupby(g25.HotelID).sum(); ov=(g25.OverallScore.astype(float)*ww).groupby(g25.HotelID).sum()/ww.groupby(g25.HotelID).sum()
c25=gcg[gcg.Year==2025].groupby('HotelID').Complaints.sum().astype(float)
monthly=m[m.Year>=2024].sort_values('Month').groupby('HotelID').apply(lambda g:[round(a/b,3) for a,b in zip(g.RoomsSold,g.RoomsAvailable)])
projmap=pp.merge(p[['ProjectID','Brand']],on='ProjectID'); projmap=projmap[projmap.Brand=='Goodnight Inn']
multi=pp.ProjectID.value_counts(); projmap=projmap[projmap.ProjectID.map(multi)<=20]
pm=projmap.groupby('HotelID').ProjectID.apply(list)
hot=[]
for _,x in gi.iterrows():
    hid=x.HotelID; kk=k25.loc[hid]
    yr=2025-(x.LastRenovationDate.year if pd.notna(x.LastRenovationDate) else x.OpeningDate.year)
    hot.append(dict(id=hid,name=x.HotelName.replace('Goodnight Inn ',''),type=x.LocationType,region=x.Region,country=x.Country,rooms=int(x.Rooms),opened=int(x.OpeningDate.year),renoYear=(int(x.LastRenovationDate.year) if pd.notna(x.LastRenovationDate) else None),age=int(yr),occ=round(kk.RoomsSold/kk.RoomsAvailable,4),revpar=round(kk.RoomRevenue/kk.RoomsAvailable,2),adr=round(kk.RoomRevenue/kk.RoomsSold,2),gopm=round(1-kk.TotalOperatingExpenses/kk.TotalRevenue,4),rev=round(kk.TotalRevenue/1e6,3),nps=round(float(nps[hid]),2),overall=round(float(ov[hid]),3),compl=round(float(c25[hid]/kk.RoomsSold*1000),2),ota=out['otaShareHotels'][hid],monthly=monthly[hid],projects=pm.get(hid,[]),lat=round(x.Latitude,3),lon=round(x.Longitude,3)))
out['hotels']=hot
# 2021 cohort vs peers NPS yearly
rc=ren[ren.HotelID.isin(ids)&(ren.EndDate>='2021-01-01')].HotelID.tolist(); out['cohort2021']=[h.set_index('HotelID').HotelName[i].replace('Goodnight Inn ','') for i in rc]
for lbl,sel in [('cohort',geg.HotelID.isin(rc)),('peers',~geg.HotelID.isin(rc))]:
    x=geg[sel]; out['npsCohort_'+lbl]={int(y):round(float((g.NetPromoterScore.astype(float)*g.SurveyResponses.astype(float)).sum()/g.SurveyResponses.astype(float).sum()),2) for y,g in x.groupby('Year')}
# projects GI + scenarios + econ
mp25=m[m.Year==2025].groupby('HotelID').TotalRevenue.sum(); MONTHS=pd.period_range('2027-01','2032-12',freq='M')
def econ(pr,scen):
    e=s[(s.ProjectID==pr.ProjectID)&(s.Scenario==scen)].iloc[0]; op=float(e.AnnualOperatingProfitImpactUSD)
    start=pd.Period(pr.EarliestStart,freq='M'); D=int(pr.DurationMonths); comp=start+D; hs=pp[pp.ProjectID==pr.ProjectID].HotelID.tolist(); prm=mp25[mp25.index.isin(hs)].sum()/12 if hs else 0.0
    cap=pd.Series(0.0,index=MONTHS); dis=pd.Series(0.0,index=MONTHS); ben=pd.Series(0.0,index=MONTHS)
    for mm in MONTHS:
        if start<=mm<comp: cap[mm]-=float(pr.CapexUSD)/D; dis[mm]-=float(pr.RoomsOutOfServicePct)*prm
        elif mm>=comp: kq=(mm-comp).n; ben[mm]+=op/12*(0.5 if kq<12 else 0.85 if kq<24 else 1.0)
    tot=cap+dis+ben; cum=tot.cumsum(); pb=next((int(str(mm)[:4]) for mm,v in cum.items() if v>=0 and mm>=comp), None)
    by=tot.groupby(tot.index.year).sum(); npv=sum(v/1.08**(y-2026) for y,v in by.items())
    return dict(complete=str(comp),capex=round(cap.sum()/1e6,2),disruption=round(dis.sum()/1e6,2),benefit=round(ben.sum()/1e6,2),net=round(tot.sum()/1e6,2),npv=round(npv/1e6,2),run2032=round(ben[ben.index.year==2032].sum()/1e6,2),payback=pb,yearly={int(y):round(v/1e6,3) for y,v in by.items()},yearlyBen={int(y):round(v/1e6,3) for y,v in ben.groupby(ben.index.year).sum().items()},yearlyCapex={int(y):round(v/1e6,3) for y,v in cap.groupby(cap.index.year).sum().items()},yearlyDis={int(y):round(v/1e6,3) for y,v in dis.groupby(dis.index.year).sum().items()})
pr_=[]
for _,x in p[p.Brand=='Goodnight Inn'].iterrows():
    sc_={scn:dict(revenue=int(e.AnnualRevenueImpactUSD),op=int(e.AnnualOperatingProfitImpactUSD),occ=float(e.OccupancyChangePts),adr=float(e.ADRChangePct),addedOcc=(None if pd.isna(e.AddedRoomsOccupancy) else float(e.AddedRoomsOccupancy)),fb=float(e.FoodBeverageRevenueChangePct),opex=float(e.OperatingExpenseChangePct),dist=float(e.DistributionCostChangePts),sat=float(e.SatisfactionChangePts),econ=econ(x,scn)) for scn,e in ((scn,s[(s.ProjectID==x.ProjectID)&(s.Scenario==scn)].iloc[0]) for scn in ['Low','Expected','High'])}
    pr_.append(dict(id=x.ProjectID,name=x.ProjectName,category=x.Category,scope=x.Scope,growth=x.GrowthInitiative=='Yes',capex=int(x.CapexUSD),start=str(x.EarliestStart.date()),months=int(x.DurationMonths),oos=float(x.RoomsOutOfServicePct),addedRooms=int(x.AddedRooms),running=int(x.AnnualRunningCostUSD),dependsOn=(None if pd.isna(x.DependsOn) else x.DependsOn),description=x.Description,hotels=pp[pp.ProjectID==x.ProjectID].HotelID.tolist(),scenarios=sc_))
out['projects']=pr_; out['budget']=int(b.set_index('Brand').InvestmentBudgetUSD['Goodnight Inn'])
out['planA']=['GI-01','GI-10','GI-02','GI-05','GI-04','GI-07']
# baseline projection
cap_=0.97; base=m[m.Year==2025].merge(gi[['HotelID','HotelName','Region']],on='HotelID').groupby(['HotelID','HotelName','Region'])[['RoomsAvailable','RoomsSold','TotalRevenue','TotalOperatingExpenses']].sum().reset_index()
base['RevPOR']=base.TotalRevenue/base.RoomsSold; base['CPOR']=base.TotalOperatingExpenses/base.RoomsSold
rows=[]
for _,bb in base.iterrows():
    dem=adr=cost=1.0
    for y in range(2026,2033):
        a=fa[(fa.Year==y)&(fa.Region==bb.Region)].iloc[0]; dem*=1+a.MarketDemandGrowthPct; adr*=1+a.ADRInflationPct; cost*=1+a.CostInflationPct
        want=bb.RoomsSold*dem; sold=min(want,bb.RoomsAvailable*cap_)
        rows.append(dict(HotelID=bb.HotelID,HotelName=bb.HotelName.replace('Goodnight Inn ',''),Year=y,avail=bb.RoomsAvailable,demand=want,sold=sold,rev=sold*bb.RevPOR*adr,opex=sold*bb.CPOR*cost))
P=pd.DataFrame(rows); g=P.groupby('Year')[['avail','demand','sold','rev','opex']].sum()
out['baseline']={int(y):dict(occ=round(v.sold/v.avail,4),demandOcc=round(v.demand/v.avail,4),rev=round(v.rev/1e6,2),gop=round((v.rev-v.opex)/1e6,2),gopm=round(1-v.opex/v.rev,4),unmet=int(v.demand-v.sold)) for y,v in g.iterrows()}
capped=P[P.demand>P.avail*cap_].groupby('HotelName').Year.min(); out['capacityWall']=[dict(name=n,first=int(y),demandOcc={int(yy):round(dd,3) for yy,dd in P[P.HotelName==n].set_index('Year').apply(lambda r_: r_.demand/r_.avail,axis=1).items()}) for n,y in capped.sort_values().items()]
out['assumptions']=[dict(year=int(x.Year),region=x.Region,demand=float(x.MarketDemandGrowthPct),adr=float(x.ADRInflationPct),cost=float(x.CostInflationPct)) for x in fa.itertuples()]
# location type seasonality 2025
lt=m[m.Year==2025].merge(gi[['HotelID','LocationType']],on='HotelID').groupby(['LocationType',m[m.Year==2025].Month.dt.month])[['RoomsSold','RoomsAvailable']].sum(); out['seasonType']={t_:[round(v,3) for v in (grp.RoomsSold/grp.RoomsAvailable).tolist()] for t_,grp in lt.groupby(level=0)}
out['typeKpi']={t_:kp(grp) for t_,grp in m[m.Year==2025].merge(gi[['HotelID','LocationType']],on='HotelID').groupby('LocationType')}
json.dump(out,open(sys.argv[2],'w'),indent=0,default=str); print('ok', {k:(len(v) if hasattr(v,'__len__') else v) for k,v in out.items()})
