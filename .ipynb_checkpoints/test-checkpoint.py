import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import quandl
import sys
import scipy.optimize as scoplt

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.figure_factory as ff

plt.style.use('fivethirtyeight')
np.random.seed(777)

data = yf.download(['BTC-USD','ETH-USD','XRP-USD','LINK-USD'],start="2019-01-01",end="2021-01-01")
#data = yf.download(['AAPL','NKE','GOOGL','AMZN'],start="2018-01-01",end="2021-01-01")

daily_returns = data
data = data['Adj Close']