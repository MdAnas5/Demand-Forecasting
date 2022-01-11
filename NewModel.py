import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

df = pd.read_csv('SemiMonthResampleZero.csv')
df['SIHD_INV_DATE'].min(), df['SIHD_INV_DATE'].max()

df = df.sort_values('SIHD_INV_DATE')
df.isnull().sum()

df = df.groupby('SIHD_INV_DATE')['QTY'].sum().reset_index()
# df = df.set_index('SIHD_INV_DATE'.asfreq('SM'))
# print(df.index)

# y = df['QTY']
# print(y['2019':])

# y.plot(figsize=(15, 6))
# plt.show()

from pylab import rcParams
rcParams['figure.figsize'] = 18, 8

# y['SIHD_INV_DATE'] = pd.to_datetime(y['SIHD_INV_DATE'])
# df = df.set_index('SIHD_INV_DATE')

decomposition = sm.tsa.seasonal_decompose(df, model='additive')
fig = decomposition.plot()
plt.show()

