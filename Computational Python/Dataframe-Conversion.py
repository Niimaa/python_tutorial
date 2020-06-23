import numpy as np
import pandas as pd

#Creating series
series1 = pd.Series(np.random.randn(5), index= ['one','two','three','four','five'])
print(series1)

series1= series1.to_frame()
print(series1)

series2 = pd.Series(np.random.randn(5), index= ['one','two','three','four','five'])
print(series2)

series2= series2.to_frame()
print(series2)

#join together two series as a single dataframe
dataframe1 = pd.concat([series1,series2],axis=1)
print(dataframe1)

dataframe1 = pd.concat([series1,series2],axis=1).reset_index()
print(dataframe1)

#[0] is the row index
print(dataframe1.iloc[0])
#we can add column index next to row
print(dataframe1.iloc[3][0])
#drop rows and coloumns
dataframe3 = pd.DataFrame(np.random.randn(25).reshape(5,5), index=['one','two','three','four','five'], columns = ['1st','2nd','3rd','4th','5th'])
print(dataframe3)

dataframe4 = dataframe3.drop('two')
print(dataframe4)
#to drop the coloumn we need to mention the axis
dataframe5 = dataframe3.drop('2nd',axis=1)
print(dataframe5)
print(dataframe3)
#if we want to change the dataframe3 without saving it in a new dataframe
dataframe3.drop('3rd', axis=1, inplace= True)
print(dataframe3)