import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], name= 'Alphabet Index'), columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

dataframe1['character'].replace('superman','superwoman', inplace= True)
print(dataframe1)

#rename the value with the specific location
dataframe1.iat[2,4]='female'
print(dataframe1)

dataframe1.at['D','gender']='female'
print(dataframe1)
