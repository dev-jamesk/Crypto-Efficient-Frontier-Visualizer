import  requests
import json
import numpy as np 
import  datetime as dt 
from pandas_datareader import data as pdr 

url = 'https://api.binance.com/api/v3/klines'
symbol = 'ETHUSDT'
interval ='1d'
startTime = str(int(dt.datetime(2020,1,1).timestamp()*1000))
endTime = str(int(dt.datetime(2021,1,1).timestamp()*1000))

limit = '1000'
req_para = {"symbol" :symbol, "interval":interval,"startTime":startTime,"endTime":endTime,"limit":limit}

