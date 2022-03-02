import pandas as pd
import pandas_datareader as web
from datetime import datetime
import pandas_datareader.wb as wb
import numpy as np


gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)
print(nasdaq_data)

sap_data = web.DataReader('SP500', 'fred', start, end)
print(sap_data)

gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
print(gdp_data)

export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
print(export_data)

def log_return(prices):
    series = prices / prices.shift(1)
    return np.log(series)

gold_returns = log_return(gold_prices['Gold_Price'])
print(gold_returns)

crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])

nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])

sap_returns = log_return(sap_data['SP500'])

gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])

export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

gold_variance = gold_returns.var()
print(gold_variance)
print(crude_oil_variance := crude_oil_returns.var())
print(nasdaq_variance := nasdaq_returns.var())
print(sap_variance := sap_returns.var())
print(gdp_variance := gdp_returns.var())
print(export_variance := export_returns.var())


