import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[34,54,23,52,76,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47]}
dataframe1 = pd.DataFrame(popularity)
print(dataframe1)

#creat a grouping object
dataframe2 = dataframe1.groupby(['character'])
print(dataframe2)
#convert into list
dataframe2 = list(dataframe1.groupby(['character']))
print(dataframe2)
#convert into ictionary
dict1 = dict(list(dataframe1.groupby(['character'])))
print(dict1)
#based on indexing do the filter
dict2 = dict1['jerry']
print(dict2)
dataframe3 = dataframe1.groupby(['character']).describe()
print(dataframe3)
