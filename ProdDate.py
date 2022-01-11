import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('SI.xlsx', parse_dates=['SIHD_INV_DATE'])
df.to_csv('NewSI.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = df.groupby(['SILN_PROD_ID'], as_index=False,
                sort=True)['SIHD_INV_DATE'].count()
df = pd.DataFrame(df).reset_index(drop=True)
# df = df.astype({'SIHD_INV_DATE': int})
df = df.sort_values(by='SIHD_INV_DATE', ascending=False)
print(df.head(15))
# print(df.tail(10))
print(df.shape)

# df.to_csv('SI_ProdDateCount.csv')
