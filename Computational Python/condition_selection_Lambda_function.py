import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

dataframe2 = dataframe1[dataframe1['character'] =='batman']
print(dataframe2)

dataframe3 = dataframe1[dataframe1['character'] != 'batman']
print(dataframe3)

#select with two characteristic
dataframe4 = dataframe1[(dataframe1['character'] == 'batman') & (dataframe1['popularity'] == '5th')]
print(dataframe4)
#using or istead of &
dataframe5 = dataframe1[(dataframe1['character'] == 'batman') | (dataframe1['popularity'] == '5th')]
print(dataframe5)

#using isin method
dataframe6 = dataframe1[dataframe1['character'].isin(['superman', 'jerry'])]
print(dataframe6)
#using lambda function
#syntax lambda [argument] : [expression]
x = lambda a: a+5
print(x(2))

dataframe7 = dataframe1[dataframe1['character'].map(lambda superhero:'batman' in superhero)]
print(dataframe7)
