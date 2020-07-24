import numpy as np
import pandas as pd

popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,78,60,57,44,59,45], 'score2':[34,54,23,52,76,60,57,44,59,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity)
print(dataframe1)

buckets = [0,45,50,55,60]
bucket_labels = ['poor','average','good','excellent']
#add a new column
dataframe1['ratings']  = pd.cut(dataframe1['score1'], buckets, labels= bucket_labels)

print(dataframe1)
