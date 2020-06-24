import numpy as np
import pandas as pd

series1 = pd.Series(np.random.randn(5), index= ['one','two','three','four','five'])
dataframe1 = series1.to_frame()
print(series1)
print(dataframe1)

dataframe2 = pd.DataFrame(np.random.randn(25).reshape(5,5), index = ['one','two','three','four','five'], columns=['1st','2nd','3rd','4th','5th'])
print(dataframe2)

#dataframe summary method
print(dataframe2.describe())
#sum of the values in each column
print(dataframe2.sum())
#if we want sum of the values in each row
print(dataframe2.sum(axis=1))
#accumulative sum
print(dataframe2.cumsum())
print(dataframe2.cumsum(axis=1))
print(dataframe2.min())
print(dataframe2.min(axis=1))
print(dataframe2.max())
print(dataframe2.max(axis=1))
print(dataframe2.idxmax())
print(dataframe2.idxmin(axis=1))
#Creating dataframe from dictionary and select elements
popularity = {'character':['spiderman','superman','batman','tom','jerry'], 'popularity':['1st','2nd','3rd','4th','5th'],'score':[60,57,46,59,47]}
print(popularity)
dataframe3 = pd.DataFrame(popularity, index=['A','B','C','D','E'])
print(dataframe3)
#accessing the elements
print(dataframe3.iloc[2][0])
print(dataframe3.loc['C','character'])
print(dataframe3.at['C','character'])
print(dataframe3.iat[2,0])
print(dataframe3)
print(dataframe3['score']['C'])
print(dataframe3['score'][2])
print(dataframe3[1:3])