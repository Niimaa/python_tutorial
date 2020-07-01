import numpy as np
import pandas as pd
#reading the CSV file
dataframe1 = pd.read_csv('iris.data.csv')
print(dataframe1)
#to print only 5 rows of the data set we can use head()
print(dataframe1.head())

dataframe1 = pd.read_csv('iris.data.csv', header=None)
print(dataframe1.head())
#If the data are separated by space
dataframe1 = pd.read_csv('iris.data.csv', header=None, sep=',')
#specify the nubmer of rows
dataframe1 = pd.read_csv('iris.data.csv', header=None, sep=',', nrows=100)
print(dataframe1)
print(dataframe1[96:])

#writing the CSV file
popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],'score1':[34,54,23,52,76,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47]}
dataframe2 = pd.DataFrame(popularity)
print(dataframe2)
dataframe3 = dataframe2.to_csv('popularity.csv', index=False, sep=' ')
print(dataframe3)


