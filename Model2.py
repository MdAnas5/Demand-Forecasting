import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import train_test_split

# df = pd.read_csv('DayWiseResampleZero.csv', parse_dates=['SIHD_INV_DATE'])

# df = pd.read_csv('WeekWiseResampleZero.csv', parse_dates=['SIHD_INV_DATE'])
df = pd.read_csv('SemiMonthResampleZero.csv', parse_dates=['SIHD_INV_DATE'])
# df = pd.read_csv('MonthResampleZero.csv', parse_dates=['SIHD_INV_DATE'])

# train, test = np.split(df, [int(.67 * len(df))])

train, test = train_test_split(df, test_size=0.2, shuffle=False)
print(train, "\n", test)

# Build Model
model = ARIMA(train, order=(3, 2, 1))
fitted = model.fit(disp=-1)
print(fitted.summary())

# Forecast
fc, se, conf = fitted.forecast(15, alpha=0.05)  # 95% conf

# Make as pandas series
fc_series = pd.Series(fc, index=test.index)
lower_series = pd.Series(conf[:, 0], index=test.index)
upper_series = pd.Series(conf[:, 1], index=test.index)

# Plot
plt.figure(figsize=(12,5), dpi=100)
plt.plot(train, label='training')
plt.plot(test, label='actual')
plt.plot(fc_series, label='forecast')
plt.fill_between(lower_series.index, lower_series, upper_series,
                 color='k', alpha=.15)
plt.title('Forecast vs Actuals')
plt.legend(loc='upper left', fontsize=8)
plt.show()

