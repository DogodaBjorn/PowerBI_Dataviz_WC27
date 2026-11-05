import sys, pandas as pd
pd.set_option('display.width', 300); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.max_colwidth', 400)
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
p=r('InvestmentProjects'); pp=r('InvestmentProjectProperties'); s=r('InvestmentScenarios'); h=r('Hotels')
n=pp.groupby('ProjectID').HotelID.nunique().rename('nHotels'); rooms=pp.merge(h[['HotelID','Rooms']],on='HotelID').groupby('ProjectID').Rooms.sum().rename('PropRooms')
p=p.merge(n,on='ProjectID',how='left').merge(rooms,on='ProjectID',how='left')
ex=s[s.Scenario=='Expected'].set_index('ProjectID')[['AnnualRevenueImpactUSD','AnnualOperatingProfitImpactUSD']]
lo=s[s.Scenario=='Low'].set_index('ProjectID').AnnualOperatingProfitImpactUSD.rename('LowOP'); hi=s[s.Scenario=='High'].set_index('ProjectID').AnnualOperatingProfitImpactUSD.rename('HighOP')
p=p.join(ex,on='ProjectID').join(lo,on='ProjectID').join(hi,on='ProjectID')
p['ExpOP/Capex']=p.AnnualOperatingProfitImpactUSD/p.CapexUSD
for b,g in p.groupby('Brand'):
    print('\n=====',b)
    print(g[['ProjectID','ProjectName','Category','Scope','GrowthInitiative','CapexUSD','EarliestStart','DurationMonths','RoomsOutOfServicePct','AddedRooms','AnnualRunningCostUSD','DependsOn','ExclusiveWith','nHotels','PropRooms','AnnualRevenueImpactUSD','AnnualOperatingProfitImpactUSD','LowOP','HighOP','ExpOP/Capex']].to_string(index=False))
    print('sum capex', g.CapexUSD.sum())
print('\n== descriptions'); print(p[['ProjectID','Brand','Description']].to_string(index=False))
print('\n== scenarios full'); print(s.to_string(index=False))
print('unassigned project properties', set(p.ProjectID)-set(pp.ProjectID))
