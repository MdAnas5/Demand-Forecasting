import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('SI1.xlsx', parse_dates=['SIHD_INV_DATE'], index_col='SIHD_INV_DATE')
# pd.set_option('display.max_columns', None)
# print(df.columns)
# df = df.astype({'SIHD_INV_DATE': np.datetime64})
# print(df['SILN_PROD_ID'].unique()).tolist()
# values_df2 = df['SILN_PROD_ID'].unique('FGAS-VW271-01-00099')
l = ['FGAS-660A-16-00087']
filtered = df[df['SILN_PROD_ID'].isin(l)]
filtered = filtered.drop('SILN_PROD_ID', axis=1)
# print(filtered.head(10))
# filtered = filtered.astype({'SIHD_INV_DATE': np.datetime64})
# filtered = filtered.QTY.resample('W').mean().fillna(pd.rolling_mean(filtered.QTY, 6, min_periods=1))
# filtered = filtered.QTY.resample('D').sum().fillna(filtered.QTY.rolling(6, min_periods=1)).mean().plot()
filtered = filtered.QTY.resample('M').min()
print(filtered.head(10))
filtered.to_csv('MonthlyMin.csv')
# filtered1 = filtered.fillna(filtered.QTY.rolling(6, min_periods=1).mean())
# print(filtered1.head(10))
# filtered = filtered.QTY.resample('M').sum().plot(kind='line', figsize=(10, 5))
# plt.show()
# filtered = filtered.QTY.resample('M').sum()
# filtered.to_csv('MonthWiseResample.csv')
# print(filtered.head())
# x = filtered.SIHD_INV_DATE
# y = filtered.QTY
# plt.bar(x, y)



# print(filtered.head())
# filtered['QTY'].plot()
# print('resampled \n', filtered.head(10))
# filtered = filtered.SIHD_INV_DATE.sort_values(ascending=True)
# df = df.astype({'SIHD_INV_DATE': np.datetime64})
# df = df.SIHD_INV_DATE.sort_values()
# x = filtered.SIHD_INV_DATE
# y = filtered.QTY
# plt.figure(figsize=(10,5))
# plt.bar(x, y, label='FGAS-VW271-01-00099' )
# plt.xlabel('year')
# plt.ylabel('quantity')
# plt.title('product of FGAS-VW271-01-00099')
# plt.xticks(rotation=90)
# plt.subplots_adjust(bottom=0.18)
# plt.show()

# print(filtered)
# df = df.groupby(['FGAS-VW271-01-00099', 'SIHD_INV_DATE'], as_index=False,
#                 sort=True)['QTY'].sum().sort_values(by='QTY', ascending=False)
# df = pd.DataFrame(df).reset_index(drop=True)
# df = df.astype({'QTY': int})
# df = df.reset_index()
# df['Duration'] = df.groupby(['SILN_PROD_ID'])['SIHD_INV_DATE'].diff()/np.timedelta64(1, 'D')
# df['Duration'] = df['Duration'].fillna(0)
# print(df.head(15))
# print(df.shape)
# print(df.head(10))
#plot
# df.to_csv('SI_PredYearMonth.csv')
