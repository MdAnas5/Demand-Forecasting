import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel('SI.xlsx')
pd.set_option('display.max_columns', None)

df = df.groupby(['SILN_PROD_ID'], as_index=False,
                sort=True)['QTY'].sum().sort_values(by='QTY', ascending=False)
df = pd.DataFrame(df).reset_index(drop=True)
df = df.astype({'QTY': int})
# df = df.reset_index()
# df['Duration'] = df.groupby(['SILN_PROD_ID'])['SIHD_INV_DATE'].diff()/np.timedelta64(1, 'D')
# df['Duration'] = df['Duration'].fillna(0)
# print(df.head(15))
print(df.shape)
print(df.head(10))
df.to_csv('SI_PredQty.csv')