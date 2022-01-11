import sys
import pandas as pd
import numpy as np
from impyute.imputation.cs import fast_knn

sys.setrecursionlimit(100000)
# Increase the recursion limit of the OS

df = pd.read_csv('KPL_FGAS_660A_16_00087.csv')
# train = np.array(df['QTY_NAN']).reshape(-1, 1)
# start the KNN training
df = df.astype({'QTY_NAN': float})
data = df['QTY_NAN']
# train = float(train)
# data = data.values

data = np.array(data).reshape(142, 6)
print(data)

np.seterr(divide='ignore',  invalid='ignore')
knn = fast_knn(data, k=2)

# we got an error is bool is not callable so we dont know how to call the bool value so dont try this method until review this boolean value
print(knn)
knn = knn.reshape(852, 1)

knn = pd.DataFrame(knn)
print("reshaped ", knn)
knn.to_excel('knn2.xlsx')
