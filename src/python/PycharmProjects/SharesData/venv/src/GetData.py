#https://github.com/RomelTorres/alpha_vantage
#https://www.alphavantage.co/documentation/#intraday

from alpha_vantage.timeseries import TimeSeries

import pandas as pd
import datetime

# check account.yaml for keys (ansible-vault)

def getLatest(ticker):
    ts1 = TimeSeries(key='', output_format='pandas')
    data, meta_data = ts1.get_intraday(symbol=ticker,interval='5min', outputsize='compact')
    data.reset_index(level=0, inplace=True) # move date from index to column
    data['date']=pd.to_datetime(data['date'])
    data['date']=data['date'] + datetime.timedelta(hours=10,minutes=30)
    data['date']=data['date'].dt.strftime('%Y-%m-%d %H:%M')
    data[['date', 'time']] = data['date'].str.split(' ', expand=True) # split date into date and time
    data['ticker']=ticker

    data.drop(columns=['3. low', '1. open',  '2. high'], axis=1, inplace=True)
    f = {'5. volume':['sum'], '4. close':['last'], 'time':['last']}
    data=data.groupby(['date', 'ticker']).agg(f).tail(1)

    return data

def printListData(mylist):
    appended_data = []
    for x in mylist:
        u = getLatest(x)
        appended_data.append(u)
    data = pd.concat(appended_data, axis=0)
    print(data)


myAlist = ['SHILPAMED', '530549', 'APCOTEXIND', '523694', 'ASIANPAINT', '500820']
printListData(myAlist)

# 500298 -> National Peroxide
myBlist = ['500298']
printListData(myBlist)

#print(data.describe())
