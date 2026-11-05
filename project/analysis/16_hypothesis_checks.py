import sys, pandas as pd, numpy as np
pd.set_option('display.width', 320); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels'); mp=r('MonthlyPerformance'); ren=r('Renovations'); ge=r('GuestExperience')
for c in ['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']: mp[c]=mp[c].astype(float)
mp['Year']=mp.Month.dt.year; mp=mp.merge(h[['HotelID','HotelName','Brand','LocationType','Rooms']],on='HotelID')
print('== renovations overlapping the data window (2021+)'); rr=ren[ren.EndDate>='2021-01-01'].merge(h[['HotelID','HotelName','Brand']],on='HotelID'); print(rr.to_string(index=False))
# natural experiment: hotels with renovation ending 2022-2024 vs brand peers; RevPAR + GOP% by year
ids=rr[(rr.EndDate.dt.year>=2022)&(rr.EndDate.dt.year<=2024)].HotelID.tolist()
y=mp.groupby(['HotelID','HotelName','Brand','Year'])[['RoomsAvailable','RoomsSold','RoomRevenue','TotalRevenue','TotalOperatingExpenses']].sum()
k=pd.DataFrame({'RevPAR':y.RoomRevenue/y.RoomsAvailable,'Occ':y.RoomsSold/y.RoomsAvailable,'ADR':y.RoomRevenue/y.RoomsSold,'GOP%':1-y.TotalOperatingExpenses/y.TotalRevenue,'RoomsAvail':y.RoomsAvailable}).reset_index()
print('\n== renovated hotels trajectory'); print(k[k.HotelID.isin(ids)].pivot_table(index=['Brand','HotelName'],columns='Year',values=['RevPAR','GOP%','RoomsAvail']).to_string())
bb=mp.groupby(['Brand','Year'])[['RoomsAvailable','RoomRevenue','TotalRevenue','TotalOperatingExpenses']].sum(); print('\n== brand RevPAR by year'); print((bb.RoomRevenue/bb.RoomsAvailable).unstack().to_string())
# peers excluding renovated: RevPAR growth 2021->2025 by brand
pe=k[~k.HotelID.isin(ids)].groupby(['Brand','Year']).RevPAR.mean().unstack(); print('\n== peer mean RevPAR growth 2021->2025'); print((pe[2025]/pe[2021]-1).to_string())
rv=k[k.HotelID.isin(ids)].pivot_table(index='HotelName',columns='Year',values='RevPAR'); print('renovated RevPAR growth 2021->2025'); print((rv[2025]/rv[2021]-1).to_string())
# Pebble & Pine seasonality by location type 2025
pp=mp[(mp.Brand=="Pebble & Pine")&(mp.Year==2025)].groupby(['LocationType',mp.Month.dt.month])[['RoomsSold','RoomsAvailable']].sum(); print('\n== P&P occupancy by location type x month 2025'); print((pp.RoomsSold/pp.RoomsAvailable).unstack().round(2).to_string())
pp=mp[(mp.Brand=="Pebble & Pine")&(mp.Year==2025)]; pp=pp.groupby(['HotelName',pp.Month.dt.month])[['RoomsSold','RoomsAvailable']].sum(); occ=(pp.RoomsSold/pp.RoomsAvailable).unstack()
print('P&P hotels: months <50% occupancy count and min month'); x=pd.DataFrame({'m<50':(occ<0.5).sum(axis=1),'min':occ.min(axis=1).round(2),'max':occ.max(axis=1).round(2)}).sort_values('m<50',ascending=False); print(x.head(12).to_string())
# Maison d'Or ADR monthly plateau; MO NY occupancy by month (capacity constrained?)
mo=mp[(mp.Brand=="Maison d'Or")].groupby(['Year'])[['RoomsSold','RoomRevenue']].sum(); print("\n== MO ADR by year", (mo.RoomRevenue/mo.RoomsSold).round(1).to_dict())
ny=mp[(mp.HotelName=="Maison d'Or New York")&(mp.Year==2025)]; print('MO NY 2025 monthly occ', (ny.RoomsSold/ny.RoomsAvailable).round(2).tolist())
# Goodnight: OTA dependence per hotel 2025 vs NPS
bc=r('BookingChannels'); bc=bc[bc.Month.dt.year==2025].merge(h[['HotelID','Brand']],on='HotelID'); t=bc.groupby(['Brand','HotelID','Channel'])[['RoomRevenue','DistributionCost']].sum().astype(float)
ota=(t.xs('Online Travel Agencies',level='Channel').RoomRevenue/t.groupby(level=[0,1]).RoomRevenue.sum()); print('\n== OTA share per hotel 2025: brand min/median/max'); print(ota.groupby(level=0).agg(['min','median','max']).round(3).to_string())
# P&K: Wi-Fi complaints per 1k roomnights by hotel top
gc=r('GuestComplaints'); gc=gc[gc.Month.dt.year==2025].merge(h[['HotelID','HotelName','Brand']],on='HotelID'); w=gc[gc.Category=='Wi-Fi & technology'].groupby(['Brand','HotelName']).Complaints.sum().astype(float); rs=mp[mp.Year==2025].groupby(['Brand','HotelName']).RoomsSold.sum(); print('\n== Wi-Fi complaints per 1k roomnights by brand (mean)'); print((w/rs*1000).groupby(level=0).mean().round(2).to_string())
# brand totals 2025 for sizing
print('\n== brand 2025 totals'); print(bb.loc[(slice(None),2025),:].droplevel(1).assign(GOP=lambda x:x.TotalRevenue-x.TotalOperatingExpenses)[['TotalRevenue','GOP']].div(1e6).round(1).to_string())
