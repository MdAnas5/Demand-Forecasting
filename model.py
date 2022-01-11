import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
# df = pd.read_csv('DayWiseResampleZero.csv')

# df = pd.read_csv('WeekWiseResampleZero.csv')
df = pd.read_csv('SemiMonthResampleZero.csv')
# df = pd.read_excel('SM.xlsx')
# df1 = pd.read_excel('Outcome.xlsx')
# df = pd.read_csv('MonthResampleZero.csv')

# 1 Simple linear regression fit and prediction on time series data with visualization in python

print(df.head())
print(df.shape)
x = np.arange(df['SIHD_INV_DATE'].size)
# print(x)
fit = np.polyfit(x, df['QTY'], deg=4)
print(fit)
print("Slope : " + str(fit[0]))
print("Intercept : " + str(fit[1]))

# Fit function : y = mx + c [linear regression ]
fit_function = np.poly1d(fit)
y = np.arange(df['SIHD_INV_DATE'].size+6)
prediction = fit_function(y)
prediction = pd.DataFrame(prediction)
# prediction.to_csv('prediction.csv')
print("Prediction", prediction)

# plt.plot(prediction, 'r-', label='prediction')
# plt.ylim(bottom=0, top=6500)
# plt.xlim(left='30/03/2019', right='15/12/2021')
# df = df.astype({'SIHD_INV_DATE': np.datetime64})
# plt.plot(df['SIHD_INV_DATE'], df['QTY'], label='actual')
# plt.xticks(rotation=90)

# plt.ylim(bottom=0, top=6500)
# plt.subplots_adjust(left=0.06, bottom=0.17, right=0.9, top=0.9)
# plt.grid()

# # plt.xlim(left='30/03/2019', right='15/12/2021')
# plt.ylim(bottom=0, top=6500)
# plt.grid(True)
# plt.show()

# df = df.astype({'SIHD_INV_DATE': np.datetime64})
plt.plot(df['SIHD_INV_DATE'], df['QTY'], label='actual')
plt.ylim(bottom=0, top=6500)
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.06, bottom=0.17, right=0.9, top=0.9)
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.plot(prediction, label='predict')
# plt.plot(df['SIHD_INV_DATE'], df['prediction'], label='predict')
plt.ylim(bottom=0, top=6500)
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.06, bottom=0.17, right=0.9, top=0.9)
plt.grid(color='cyan', linestyle='--', linewidth=0.5)
plt.show()

