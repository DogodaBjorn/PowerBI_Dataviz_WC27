import sys, pandas as pd
pd.set_option('display.width', 260); pd.set_option('display.max_columns', 40); pd.set_option('display.max_colwidth', 200); pd.set_option('display.max_rows', 400)
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
for t in ['Brands','FinanceParameters','FinanceAssumptions','Scenario','Region']: print('==',t); print(r(t).to_string())
h=r('Hotels'); print('== Hotels by brand/region'); print(pd.crosstab(h.Brand,h.Region,margins=True)); print(h.groupby('Brand').agg(hotels=('HotelID','count'),rooms=('Rooms','sum'),avgrooms=('Rooms','mean'),open_min=('OpeningDate','min'),open_max=('OpeningDate','max'),reno_min=('LastRenovationDate','min'),reno_max=('LastRenovationDate','max')))
print(pd.crosstab(h.Brand,h.LocationType))
dt=r('Date'); print('== Date', dt.Date.min(), dt.Date.max(), dt.Period.unique()[:10])
mp=r('MonthlyPerformance'); print('== MP months', mp.Month.min(), mp.Month.max(), mp.Month.nunique())
