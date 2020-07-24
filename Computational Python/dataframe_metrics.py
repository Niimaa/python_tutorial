import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], name= 'Alphabet Index'), columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

#find the shape of the dataframe
print(dataframe1.shape)
#just number of rows
print(dataframe1.shape[0])
#just number of columns
print(dataframe1.shape[1])
#count thte number of occurences of value in a column
print(pd.value_counts(dataframe1['character']))
#we can apply it to all the values in dataframe
print(dataframe1.apply(pd.value_counts))
print(dataframe1.apply(pd.value_counts).fillna(0))

#count the nubmer of unique values in a column
dataframe2 = dataframe1['character'].unique()
print(dataframe2)

