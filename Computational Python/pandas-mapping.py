import numpy as np
import pandas as pd

#adding a new column using mapping

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[34,54,23,52,76,60,57,46,59,47], 'score2':[34,54,23,52,76,60,57,46,59,47]}
dataframe1 = pd.DataFrame(popularity)
print(dataframe1)

gender = {'spiderman':'male', 'superman':'male','batman': 'male', 'jerry':'female', 'tom':'male'}
dataframe1['gender'] = dataframe1['character'].map(gender)
print(dataframe1)


