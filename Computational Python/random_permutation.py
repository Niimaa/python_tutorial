import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

#random permutation
no_of_rows = dataframe1.shape[0]
print(no_of_rows)

random_rows= np.random.permutation(no_of_rows)
print(random_rows)

dataframe2 = dataframe1.reindex(random_rows)
print(dataframe2)

#method2
dataframe3=dataframe1.take(random_rows)
print(dataframe3)

