import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], name= 'Alphabet Index'), columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)
#reindex(rename the rows)
dataframe2 = dataframe1.reindex(['E','B','C','D','A','F','G','I','H','J'])
print(dataframe2)

dataframe3 = dataframe1.reindex(columns= ['score1','popularity','character','score2','gender'])
print(dataframe3)

#rename the rows and columns
dataframe3.rename(columns={'character':'super hero'}, inplace=True)
dataframe3.rename(index={'A':'a','B':'b'}, inplace=True)
print(dataframe3)
