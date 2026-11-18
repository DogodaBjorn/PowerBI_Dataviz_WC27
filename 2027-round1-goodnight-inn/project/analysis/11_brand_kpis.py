import sys, pandas as pd, numpy as np
pd.set_option('display.width', 260); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 400); pd.set_option('display.float_format', lambda x: f'{x:,.3f}')
d=sys.argv[1]; r=lambda t: pd.read_parquet(f"{d}/{t}.parquet")
h=r('Hotels')[['HotelID','Brand','Region','Rooms','LocationType','LastRenovationDate','OpeningDate']]
mp=r('MonthlyPerformance').merge(h,on='HotelID'); mp['Year']=mp.Month.dt.year
num=['RoomsAvailable','RoomsSold','RoomRevenue','FoodBeverageRevenue','OtherRevenue','TotalRevenue','StaffCost','EnergyCost','MaintenanceCost','FoodBeverageCost','OtherOperatingCost','TotalOperatingExpenses']
for c in num: mp[c]=mp[c].astype('float64')
def kpis(g):
    s=g[num].sum()
    return pd.Series({'Occ':s.RoomsSold/s.RoomsAvailable,'ADR':s.RoomRevenue/s.RoomsSold,'RevPAR':s.RoomRevenue/s.RoomsAvailable,'TotRev_M':s.TotalRevenue/1e6,'GOP_M':(s.TotalRevenue-s.TotalOperatingExpenses)/1e6,'GOP%':1-s.TotalOperatingExpenses/s.TotalRevenue,'CPOR':s.TotalOperatingExpenses/s.RoomsSold,'Energy%':s.EnergyCost/s.TotalRevenue,'Maint%':s.MaintenanceCost/s.TotalRevenue,'Staff%':s.StaffCost/s.TotalRevenue,'FB%rev':s.FoodBeverageRevenue/s.TotalRevenue})
print('== Brand x Year'); print(mp.groupby(['Brand','Year']).apply(kpis).to_string())
print('== Brand x Region 2025'); print(mp[mp.Year==2025].groupby(['Brand','Region']).apply(kpis).to_string())
# seasonality occupancy by month 2025
print('== Occ by month-of-year 2025'); x=mp[mp.Year==2025].groupby(['Brand',mp.Month.dt.month])[['RoomsSold','RoomsAvailable']].sum(); print((x.RoomsSold/x.RoomsAvailable).unstack().round(3).to_string())
ge=r('GuestExperience').merge(h,on='HotelID'); ge['Year']=ge.Month.dt.year
sc=['OverallScore','CleanlinessScore','ServiceScore','RoomComfortScore','AmenitiesScore','ValueForMoneyScore','NetPromoterScore']
w=ge.SurveyResponses.astype(float)
for c in sc: ge[c+'_w']=ge[c].astype(float)*w
g=ge.groupby(['Brand','Year']); out=pd.DataFrame({c:g[c+'_w'].sum()/g.SurveyResponses.sum() for c in sc}); out['Resp']=g.SurveyResponses.sum(); print('== Guest exp (response-weighted)'); print(out.to_string())
print('score ranges', ge[sc].describe().loc[['min','max']].to_string())
gc=r('GuestComplaints').merge(h,on='HotelID'); gc['Year']=gc.Month.dt.year
print('== Complaints by brand/year/category'); print(gc.groupby(['Brand','Category','Year']).Complaints.sum().unstack().to_string())
bc=r('BookingChannels').merge(h,on='HotelID'); bc['Year']=bc.Month.dt.year
for c in ['Bookings','RoomNights','RoomRevenue','DistributionCost']: bc[c]=bc[c].astype(float)
t=bc.groupby(['Brand','Year','Channel'])[['RoomRevenue','DistributionCost']].sum()
t['share']=t.RoomRevenue/t.groupby(level=[0,1]).RoomRevenue.transform('sum'); t['cost%']=t.DistributionCost/t.RoomRevenue
print('== Channels'); print(t[['share','cost%']].unstack('Year').round(3).to_string())
tt=bc.groupby(['Brand','Year'])[['RoomRevenue','DistributionCost']].sum(); print((tt.DistributionCost/tt.RoomRevenue).unstack().to_string())
gs=r('GuestSegments').merge(h,on='HotelID'); gs['Year']=gs.Month.dt.year
for c in ['RoomNights','RoomRevenue']: gs[c]=gs[c].astype(float)
t=gs.groupby(['Brand','Year','Segment'])[['RoomNights','RoomRevenue']].sum(); t['share']=t.RoomNights/t.groupby(level=[0,1]).RoomNights.transform('sum'); t['ADR']=t.RoomRevenue/t.RoomNights
print('== Segments'); print(t[['share','ADR']].unstack('Year').round(3).to_string())
# consistency checks
mpc=r('MonthlyPerformance'); print('== checks: TotalRev==sum', (mpc.TotalRevenue-(mpc.RoomRevenue+mpc.FoodBeverageRevenue+mpc.OtherRevenue)).abs().max(), 'Opex==sum', (mpc.TotalOperatingExpenses-(mpc.StaffCost+mpc.EnergyCost+mpc.MaintenanceCost+mpc.FoodBeverageCost+mpc.OtherOperatingCost)).abs().max())
bcs=bc.groupby(['HotelID','Month']).RoomRevenue.sum(); mps=mpc.set_index(['HotelID','Month']).RoomRevenue.astype(float); print('channel roomrev vs MP roomrev max diff', (bcs-mps).abs().max())
print('rooms sold vs channel roomnights', (bc.groupby(['HotelID','Month']).RoomNights.sum()-mpc.set_index(['HotelID','Month']).RoomsSold.astype(float)).abs().max())
print('null counts MP', mpc.isna().sum().sum(), 'GE', r('GuestExperience').isna().sum().sum())
print('hotels per month MP min/max', mpc.groupby('Month').HotelID.nunique().agg(['min','max']))
