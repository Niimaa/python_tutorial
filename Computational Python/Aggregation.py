import numpy as np
import pandas as pd


popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity)
print(dataframe1)

char_popularity = dataframe1.groupby(['character', 'popularity'])

print(list(char_popularity))

dataframe2 = char_popularity.agg('min')
print(dataframe2)

dataframe3 = char_popularity.agg(['mean','max'])
print(dataframe3)

def get_mean(value):
    return(np.mean(value))

dataframe4 = char_popularity.agg([get_mean])
print(dataframe4)