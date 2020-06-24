import numpy as np
import pandas as pd

popularity = {"Exam1": [50,47,44,53,42],
              "Exam2": [60,57,46,59,47],
              "Exam3": [80,77,65,72,63],
              "Exam4": [81,83,75,79,87]}
dataframe1 = pd.DataFrame(popularity, index = ['school A', 'school B', 'school C', 'school D', 'school E'])

print(dataframe1)
dataframe2 = dataframe1[dataframe1<70]
print(dataframe2)
#remove all the "NaN"
print(dataframe2.dropna())
print(dataframe2.dropna(axis=1))
print(dataframe2.dropna(axis=1, how='all'))
print(dataframe2.dropna(axis=1, how='any'))
#put a threshold for removing the "NaN"
print(dataframe2.dropna(axis=1, how='all', thresh=3))
print(dataframe2.dropna(axis=1, how='all', thresh=2))
#just to change the dataframe2 and remove those Nan completely
dataframe2.dropna(axis=1, how='any', thresh=3, inplace= True)
print(dataframe2)
#sort methods
dataframe1 = pd.DataFrame(popularity, index = ['school A', 'school B', 'school C', 'school D', 'school E'])
print(dataframe1)
print(dataframe1.sort_values('Exam1'))
print(dataframe1.sort_values('school A', axis=1))
print(dataframe1.sort_values('school A', axis=1, ascending= False))







