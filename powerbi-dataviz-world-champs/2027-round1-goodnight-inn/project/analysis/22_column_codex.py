import sys, pandas as pd, numpy as np, glob, os
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 60); pd.set_option('display.max_rows', 500); pd.set_option('display.max_colwidth', 160)
d=sys.argv[1]
for f in sorted(glob.glob(f"{d}/*.parquet")):
    t=os.path.basename(f)[:-8]; df=pd.read_parquet(f); print(f"\n#### {t}  rows={len(df)}")
    for c in df.columns:
        s=df[c]; n=s.nunique(); kind=str(s.dtype)
        if kind.startswith('datetime'): info=f"{s.min().date()} .. {s.max().date()}"
        elif kind in ('string','str','object') or n<=12:
            vals=s.dropna().unique()[:12]; info=('values: '+' | '.join(map(str,vals))) if n<=12 else f"e.g. {' | '.join(map(str,vals[:5]))}"
        else:
            x=pd.to_numeric(s,errors='coerce'); info=f"min {x.min():,.4g}  median {x.median():,.4g}  max {x.max():,.4g}  sum {x.sum():,.4g}"
        print(f"  {c:<32} {kind:<16} distinct={n:<6} nulls={int(s.isna().sum()):<5} {info}")
h=pd.read_parquet(f"{d}/Hotels.parquet"); print('\n#### Hotels extras'); print('countries:', h.Country.nunique(), sorted(h.Country.unique())); print('opening years:', h.OpeningDate.dt.year.min(), '-', h.OpeningDate.dt.year.max()); print('rooms per hotel min/median/max', h.Rooms.min(), h.Rooms.median(), h.Rooms.max())
r=pd.read_parquet(f"{d}/Renovations.parquet").merge(h[['HotelID','Brand']],on='HotelID'); print('renovations per hotel:', r.groupby('HotelID').size().describe()[['min','mean','max']].round(2).to_dict()); print('by decade/type'); print(pd.crosstab(r.EndDate.dt.year//10*10, r.RenovationType))
print('hotels with 0 renovations:', len(set(h.HotelID)-set(r.HotelID)))
p=pd.read_parquet(f"{d}/InvestmentProjects.parquet"); print('\n#### Projects categories x scope'); print(pd.crosstab(p.Category,p.Scope)); print(pd.crosstab(p.Brand,p.GrowthInitiative)); print('EarliestStart values', p.EarliestStart.dt.date.unique())
