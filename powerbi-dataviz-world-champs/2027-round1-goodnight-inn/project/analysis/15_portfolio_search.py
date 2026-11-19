import sys, itertools, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.2f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
p=r('InvestmentProjects'); s=r('InvestmentScenarios'); pp=r('InvestmentProjectProperties'); h=r('Hotels'); b=r('Brands'); mp=r('MonthlyPerformance')
mp25=mp[mp.Month.dt.year==2025].groupby('HotelID').TotalRevenue.sum().astype(float)
DR=0.08; MONTHS=pd.period_range('2027-01','2032-12',freq='M')
def cashflows(pr, scen):
    e=s[(s.ProjectID==pr.ProjectID)&(s.Scenario==scen)].iloc[0]; op=float(e.AnnualOperatingProfitImpactUSD)
    start=pd.Period(pr.EarliestStart,freq='M'); D=int(pr.DurationMonths); comp=start+D
    hs=pp[pp.ProjectID==pr.ProjectID].HotelID.tolist(); prop_rev_m=mp25[mp25.index.isin(hs)].sum()/12 if hs else 0.0
    cf=pd.Series(0.0,index=MONTHS); capex=pd.Series(0.0,index=MONTHS); disr=pd.Series(0.0,index=MONTHS); ben=pd.Series(0.0,index=MONTHS)
    for m in MONTHS:
        if start<=m<comp:
            capex[m]-=float(pr.CapexUSD)/D; disr[m]-=float(pr.RoomsOutOfServicePct)*prop_rev_m
        elif m>=comp:
            k=(m-comp).n; ramp=0.5 if k<12 else 0.85 if k<24 else 1.0; ben[m]+=op/12*ramp
    tot=capex+disr+ben
    byyear=tot.groupby(tot.index.year).sum(); disc=sum(v/(1+DR)**(y-2026) for y,v in byyear.items())
    return dict(npv=disc, cum=tot.sum(), capex=capex.sum(), disr=disr.sum(), ben=ben.sum(), comp=str(comp), ben2032=ben[ben.index.year==2032].sum())
rows=[]
for _,pr in p.iterrows():
    for sc in ['Low','Expected','High']:
        c=cashflows(pr,sc); c.update(ProjectID=pr.ProjectID,Brand=pr.Brand,Scenario=sc,CapexUSD=pr.CapexUSD,Growth=pr.GrowthInitiative); rows.append(c)
cf=pd.DataFrame(rows); ex=cf[cf.Scenario=='Expected'].set_index('ProjectID')
print('== per-project NPV (Expected), 2027-2032, 8%, 2025 dollars, earliest start, full-revenue disruption, no terminal value')
print(ex[['Brand','CapexUSD','Growth','comp','capex','disr','ben','cum','npv','ben2032']].assign(NPVperCapex=lambda x:x.npv/x.CapexUSD).sort_values(['Brand','npv'],ascending=[True,False]).to_string())
excl={('MO-04','MO-05'),('PS-08','PS-10'),('PP-02','PP-03')}; dep={'GI-02':'GI-01','PS-01':'PS-03'}
for brand,g in p.groupby('Brand'):
    budget=float(b.set_index('Brand').InvestmentBudgetUSD[brand]); ids=g.ProjectID.tolist(); best=[]
    for k in range(1,len(ids)+1):
        for combo in itertools.combinations(ids,k):
            cs=set(combo)
            if any(a in cs and c in cs for a,c in excl): continue
            if any(x in cs and y not in cs for x,y in dep.items()): continue
            capex=g[g.ProjectID.isin(cs)].CapexUSD.sum()
            if capex>budget: continue
            growth=(g[g.ProjectID.isin(cs)].GrowthInitiative=='Yes').sum()
            npv=ex.loc[list(cs)].npv.sum(); npvlo=cf[(cf.Scenario=='Low')&cf.ProjectID.isin(cs)].npv.sum(); npvhi=cf[(cf.Scenario=='High')&cf.ProjectID.isin(cs)].npv.sum()
            best.append((npv,npvlo,npvhi,capex,len(cs),growth,','.join(sorted(cs))))
    best.sort(reverse=True)
    print(f'\n===== {brand}: budget {budget/1e6:.0f}M, all-projects capex {g.CapexUSD.sum()/1e6:.1f}M, feasible combos {len(best)}')
    print('top by NPV (Expected):')
    for row in best[:8]: print(f'  NPV {row[0]/1e6:7.1f}M  [low {row[1]/1e6:6.1f} / high {row[2]/1e6:6.1f}]  capex {row[3]/1e6:6.1f}M  n={row[4]} growth={row[5]}  {row[6]}')
    unconstrained=ex[ex.Brand==brand].npv.clip(lower=0).sum(); print(f'  unconstrained (all NPV>0 projects): {unconstrained/1e6:.1f}M ; best within budget: {best[0][0]/1e6:.1f}M ; budget bites: {(1-best[0][0]/unconstrained)*100:.0f}%')
    # worst-case robust: maximize Low
    bl=max(best,key=lambda x:x[1]); print(f'  most robust (max Low NPV): low {bl[1]/1e6:.1f} / exp {bl[0]/1e6:.1f} capex {bl[3]/1e6:.1f}M  {bl[6]}')
