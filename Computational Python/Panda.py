import pandas as pd
import numpy as np

series1 = pd.Series([10,20,'apple',5.2,-34])
print(series1)

print(type(series1))

#put a lable for index
series1 = pd.Series([10,20,'apple',5.2,-34], index=['ten','twenty','fruit','float','signed'])
print(series1)
print(series1[2])
print(series1['fruit'])

month1 = pd.Series({'april':4, 'may':5, 'june':6, 'july':7})
print(month1)
print(month1[2])
print(month1['june'])
print(month1[month1>4 ])