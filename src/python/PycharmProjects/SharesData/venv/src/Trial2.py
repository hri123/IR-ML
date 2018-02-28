#https://github.com/RomelTorres/alpha_vantage
#https://www.alphavantage.co/documentation/#intraday

from alpha_vantage.timeseries import TimeSeries

import pandas as pd


ts1 = TimeSeries(key='', output_format='pandas')
data, meta_data = ts1.get_daily(symbol='NSE:SHILPAMED', outputsize='compact')

data.sort_index(axis=1, inplace=True)

print(data.tail(5))

'''
data, meta_data = ts1.get_daily_adjusted(symbol='NSE:SHILPAMED', outputsize='compact')

print(data.tail(1))

data, meta_data = ts1.get_weekly(symbol='NSE:SHILPAMED')

print(data.tail(3))
'''
