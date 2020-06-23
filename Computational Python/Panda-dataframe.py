import pandas as pd
import numpy as np

array1 = np.array([[1,2,3,4],[5,6,7,8]])
dataframe1 = pd.DataFrame(array1)
print(array1)
print(dataframe1)

print(dataframe1[3])
print(dataframe1.columns)
#lable the index
array1 = np.array([[1,2,3,4],[5,6,7,8]])
dataframe1 = pd.DataFrame(array1,columns=['one','two','three','four'])
print(dataframe1)
print(dataframe1['two'])
