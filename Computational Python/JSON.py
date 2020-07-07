import numpy as np
import pandas as pd

dataframe1 = pd.read_json('iris.json')
print(dataframe1)

print(dataframe1.head())

print(dataframe1[:96])
print(dataframe1[5:7])

#writing the json

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],'score1':[34,54,23,52,76,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47]}

dataframe2 = pd.DataFrame(popularity)
dataframe3 = dataframe2.to_json('popularity.json')
print(dataframe2)