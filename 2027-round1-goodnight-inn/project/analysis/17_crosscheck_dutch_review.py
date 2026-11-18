import sys, itertools, pandas as pd, numpy as np
pd.set_option('display.width', 300); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); bc=r('BookingChannels'); ge=r('GuestExperience'); gc=r('GuestComplaints'); ren=r('Renovations'); p=r('InvestmentProjects'); pp=r('InvestmentProjectProperties'); s=r('InvestmentScenarios')
num=['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']
for c in num: mp[c]=mp[c].astype(float)
mp['Year']=mp.Month.dt.year; mp=mp.merge(h[['HotelID','Brand','LocationType']],on='HotelID')
for c in ['RoomRevenue','DistributionCost']: bc[c]=bc[c].astype(float)
bc['Year']=bc.Month.dt.year; bc=bc.merge(h[['HotelID','Brand']],on='HotelID')
# 1 margin before/after distribution per brand 2025 and GI by year
g=mp.groupby(['Brand','Year'])[['TotalRevenue','TotalOperatingExpenses']].sum(); dc=bc.groupby(['Brand','Year']).DistributionCost.sum()
m=pd.DataFrame({'GOP%':1-g.TotalOperatingExpenses/g.TotalRevenue,'Dist%ofRev':dc/g.TotalRevenue,'GOP% after dist':(g.TotalRevenue-g.TotalOperatingExpenses-dc)/g.TotalRevenue,'GOP after dist M':(g.TotalRevenue-g.TotalOperatingExpenses-dc)/1e6})
print('== margin before/after distribution (assumes opex excludes distribution cost, per Contents sheet)'); print(m.loc[(slice(None),2025),:].droplevel(1).to_string()); print(m.loc['Goodnight Inn'].to_string())
gi=mp[mp.Brand=='Goodnight Inn']; ids=set(gi.HotelID)
# 2 per-hotel trends
y=gi.groupby(['HotelID','Year'])[num].sum(); gm=(1-y.TotalOperatingExpenses/y.TotalRevenue).unstack(); occ=(y.RoomsSold/y.RoomsAvailable).unstack()
geg=ge[ge.HotelID.isin(ids)].copy(); geg['Year']=geg.Month.dt.year; w=geg.SurveyResponses.astype(float)
def wavg(col): x=(geg[col].astype(float)*w).groupby([geg.HotelID,geg.Year]).sum()/w.groupby([geg.HotelID,geg.Year]).sum(); return x.unstack()
nps=wavg('NetPromoterScore'); comf=wavg('RoomComfortScore'); vfm=wavg('ValueForMoneyScore')
both=nps.dropna(subset=[2021,2025]); print(f'\n== hotels with NPS 2025 < 2021: {(both[2025]<both[2021]).sum()} of {len(both)} | NPS 2025 < 2024: {(nps[2025]<nps[2024]).sum()} of {nps[2024].notna().sum()}')
print(f'margin 2025 < 2023: {(gm[2025]<gm[2023]).sum()} of {gm[2023].notna().sum()} | margin 2025 < 2024: {(gm[2025]<gm[2024]).sum()} of {gm[2024].notna().sum()}')
dn=(nps[2025]-nps[2021]).dropna(); do=(occ[2025]-occ[2021]).dropna(); print('corr(dNPS 2021-25, dOcc 2021-25) =', round(dn.corr(do.loc[dn.index]),3), '| corr(dNPS 23-25, dOcc 23-25)=', round((nps[2025]-nps[2023]).corr(occ[2025]-occ[2023]),3))
# 3 comfort vs years since renovation
hh=h[h.Brand=='Goodnight Inn'].set_index('HotelID'); age=(2025-hh.LastRenovationDate.dt.year); c25=comf[2025]; n25=nps[2025]
sel=age.dropna().index; print(f'\n== r(years since reno, RoomComfort 2025) over {len(sel)} hotels with a date:', round(age[sel].corr(c25[sel]),3), '| r with NPS:', round(age[sel].corr(n25[sel]),3), '| all 50 with opening fallback: comfort', round(age.fillna(2025-hh.OpeningDate.dt.year).corr(c25),3))
# 4 complaints per 1k by category YoY
gcg=gc[gc.HotelID.isin(ids)].copy(); gcg['Year']=gcg.Month.dt.year; cy=gcg.groupby(['Category','Year']).Complaints.sum().astype(float).unstack(); rn=gi.groupby('Year').RoomsSold.sum(); per=cy.div(rn,axis=1)*1000
print('\n== complaints per 1k: change 2024->2025 and 2021->2025'); print(pd.DataFrame({'2025':per[2025],'yoy 24-25':per[2025]/per[2024]-1,'2021-25':per[2025]/per[2021]-1}).sort_values('yoy 24-25',ascending=False).to_string())
# 5 renovation spend per brand 2018-2025 and starts per year
rr=ren.merge(h[['HotelID','Brand']],on='HotelID'); r18=rr[rr.StartDate.dt.year>=2018]
print('\n== renovation spend 2018+ (by start year) per brand, $M, per hotel'); sp=r18.groupby('Brand').agg(n=('CostUSD','count'),spend=('CostUSD','sum')); sp['spend_M']=sp.spend/1e6; sp['hotels']=h.groupby('Brand').HotelID.count(); sp['per_hotel_M']=sp.spend_M/sp.hotels; print(sp[['n','spend_M','per_hotel_M']].to_string())
print(pd.crosstab(rr[rr.StartDate.dt.year>=2018].Brand, rr[rr.StartDate.dt.year>=2018].StartDate.dt.year).to_string())
print('GI last renovation start:', rr[rr.Brand=='Goodnight Inn'].StartDate.max().date(), '| GI 2021+ starts:', int((rr[(rr.Brand=='Goodnight Inn')&(rr.StartDate.dt.year>=2021)]).shape[0]))
# 6 event study: renovations completed 2021-2023 with >=3 months data both sides: comfort & room-condition complaints 6 months before start vs 6 months after end
gea=ge.merge(h[['HotelID','Brand']],on='HotelID'); gca=gc.merge(h[['HotelID','Brand']],on='HotelID'); mpa=mp.copy()
ev=rr[(rr.EndDate>='2021-01-01')&(rr.EndDate<='2023-12-31')]
rows=[]
for _,e in ev.iterrows():
    hid=e.HotelID; b0=e.StartDate-pd.DateOffset(months=6); a1=e.EndDate+pd.DateOffset(months=6)
    gb=gea[(gea.HotelID==hid)&(gea.Month>=b0)&(gea.Month<e.StartDate)]; ga=gea[(gea.HotelID==hid)&(gea.Month>=e.EndDate)&(gea.Month<a1)]
    if len(gb)<3 or len(ga)<3: continue
    cb=(gb.RoomComfortScore.astype(float)*gb.SurveyResponses).sum()/gb.SurveyResponses.sum(); ca=(ga.RoomComfortScore.astype(float)*ga.SurveyResponses).sum()/ga.SurveyResponses.sum()
    nb=(gb.NetPromoterScore.astype(float)*gb.SurveyResponses).sum()/gb.SurveyResponses.sum(); na=(ga.NetPromoterScore.astype(float)*ga.SurveyResponses).sum()/ga.SurveyResponses.sum()
    kb=gca[(gca.HotelID==hid)&(gca.Category=='Room condition')&(gca.Month>=b0)&(gca.Month<e.StartDate)].Complaints.sum(); ka=gca[(gca.HotelID==hid)&(gca.Category=='Room condition')&(gca.Month>=e.EndDate)&(gca.Month<a1)].Complaints.sum()
    sb=mpa[(mpa.HotelID==hid)&(mpa.Month>=b0)&(mpa.Month<e.StartDate)].RoomsSold.sum(); sa=mpa[(mpa.HotelID==hid)&(mpa.Month>=e.EndDate)&(mpa.Month<a1)].RoomsSold.sum()
    rows.append(dict(hotel=h.set_index('HotelID').HotelName[hid],brand=e.Brand,end=e.EndDate.date(),comfort_before=cb,comfort_after=ca,d_comfort=ca-cb,nps_before=nb,nps_after=na,roomcond_per1k_before=kb/sb*1000,roomcond_per1k_after=ka/sa*1000,d_roomcond_pct=(ka/sa)/(kb/sb)-1))
E=pd.DataFrame(rows); print(f'\n== event study, {len(E)} renovations completed 2021-2023 with >=3 months each side'); print(E.to_string(index=False)); print('mean d_comfort', round(E.d_comfort.mean(),2), '| mean d_nps', round((E.nps_after-E.nps_before).mean(),1), '| mean room-condition complaints change', f"{E.d_roomcond_pct.mean()*100:.0f}% (range {E.d_roomcond_pct.min()*100:.0f}..{E.d_roomcond_pct.max()*100:.0f})")
# 7 value for money + ADR growth by brand
gw=gea.copy(); gw['Year']=gw.Month.dt.year; W=gw.SurveyResponses.astype(float); vf=(gw.ValueForMoneyScore.astype(float)*W).groupby([gw.Brand,gw.Year]).sum()/W.groupby([gw.Brand,gw.Year]).sum(); print('\n== value for money 2025 by brand'); print(vf.unstack()[[2021,2025]].to_string())
a=mp.groupby(['Brand','Year'])[['RoomRevenue','RoomsSold']].sum(); adr=(a.RoomRevenue/a.RoomsSold).unstack(); print('ADR growth 2021->2025'); print((adr[2025]/adr[2021]-1).round(3).to_string())
# 8 everything-except-refresh sum
gp=p[p.Brand=='Goodnight Inn'].set_index('ProjectID'); alt=['GI-01','GI-02','GI-03','GI-05','GI-08','GI-09','GI-10']; print('\n== alt B sum', gp.loc[alt].CapexUSD.sum()/1e6)
# 9 NPV variants for GI-07 with disruption = lost revenue x 45% margin ; feasible combos count with >=3 projects & >=1 growth
mp25=gi[gi.Year==2025].groupby('HotelID').TotalRevenue.sum(); MONTHS=pd.period_range('2027-01','2032-12',freq='M')
def npv(pid,scen,disr_share):
    pr=gp.loc[pid]; e=s[(s.ProjectID==pid)&(s.Scenario==scen)].iloc[0]; op=float(e.AnnualOperatingProfitImpactUSD); start=pd.Period(pr.EarliestStart,freq='M'); D=int(pr.DurationMonths); comp=start+D; hs=pp[pp.ProjectID==pid].HotelID.tolist(); prm=mp25[mp25.index.isin(hs)].sum()/12 if hs else 0
    tot=pd.Series(0.0,index=MONTHS)
    for mm in MONTHS:
        if start<=mm<comp: tot[mm]-=float(pr.CapexUSD)/D+float(pr.RoomsOutOfServicePct)*prm*disr_share
        elif mm>=comp: k=(mm-comp).n; tot[mm]+=op/12*(0.5 if k<12 else 0.85 if k<24 else 1.0)
    by=tot.groupby(tot.index.year).sum(); return sum(v/1.08**(yy-2026) for yy,v in by.items())/1e6
print('== NPV Expected with disruption at 45% margin vs 100%:'); print({pid:(round(npv(pid,'Expected',0.45),1),round(npv(pid,'Expected',1.0),1)) for pid in gp.index})
ids_=list(gp.index); cnt=0; best=None
for k in range(3,11):
    for combo in itertools.combinations(ids_,k):
        cs=set(combo)
        if 'GI-02' in cs and 'GI-01' not in cs: continue
        if gp.loc[list(cs)].CapexUSD.sum()>60e6: continue
        if (gp.loc[list(cs)].GrowthInitiative=='Yes').sum()<1: continue
        cnt+=1
print('feasible combos (>=3, >=1 growth, budget, dependency):', cnt)
