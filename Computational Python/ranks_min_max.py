import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

#rank method to generate ranks based on attribute
dataframe2 = dataframe1['score1'].rank(ascending=True)
print(dataframe2)

dataframe2 = dataframe1['score1'].rank(ascending=False)
print(dataframe2)

dataframe1['rank1'] = dataframe1['score1'].rank(ascending=False)
print(dataframe1)
#get the minimum value index
dataframe3 = dataframe1['score1'].idxmin()
print(dataframe3)
#get the minimum value
dataframe3 = dataframe1['score1'][2]
print(dataframe3)

dataframe3 = dataframe1['score1'][dataframe1['score1'].idxmin()]
print(dataframe3)

dataframe3 = dataframe1['score1'].min()
print(dataframe3)
#idmax use the same method for the maximum value index