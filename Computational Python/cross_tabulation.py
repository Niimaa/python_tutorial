import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,60,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)
#frequecy distribution
dataframe2 = pd.crosstab(dataframe1['character'],dataframe1['score1'])
print(dataframe2)
#have the total value of all rows and columns
dataframe3 = pd.crosstab(dataframe1['character'],dataframe1['score1'], margins=True)
print(dataframe3)