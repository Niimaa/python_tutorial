import numpy as np
import pandas as pd


popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],'score1':[34,54,23,52,76,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47]}

dataframe1 = pd.DataFrame(popularity)
print(dataframe1)
#stack
dataframe2 = dataframe1.stack()
print(dataframe2)
#unstack back to normal
dataframe3 = dataframe2.unstack()
print(dataframe3)
#creat transpose
dataframe3 = dataframe2.unstack(0)
print(dataframe3)
#pivoting, index has to be defined
dataframe4 = dataframe1.pivot_table(index=['character', 'popularity'])
print(dataframe4)
