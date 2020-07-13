import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','1st','3rd','4th','5th','6th','7th','8th','9th','10th'],'score1':[34,34,23,52,76,60,57,46,59,47], 'score2':[34,34,23,52,76,60,57,46,59,47]}
dataframe1 = pd.DataFrame(popularity)
print(dataframe1)

dataframe2 = dataframe1.duplicated()

print(dataframe2)
dataframe3 = dataframe1.duplicated(['character'])
print(dataframe3)

#Remove the dupplciated value
dataframe4 = dataframe1.drop_duplicates(['character'])
print(dataframe4)

#remove the dupplicated value but keep the last value instead of the first one
dataframe5 = dataframe1.drop_duplicates(['character'], keep='last')
print(dataframe5)
