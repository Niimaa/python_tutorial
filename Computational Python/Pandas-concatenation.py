import numpy as np
import pandas as pd

#Contatenation of data frames

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                           'B':['B0','B1','B2','B3'],
                           'C':['C0','C1','C2','C3'],
                           'D':['D0','D1','D2','D3']},
                          index= [0,1,2,3])

print(df1)

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                           'B':['B4','B5','B6','B7'],
                           'C':['C4','C5','C6','C7'],
                           'D':['D4','D5','D6','D7']},
                          index= [4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                           'B':['B8','B9','B10','B11'],
                           'C':['C8','C9','C10','C11'],
                           'D':['D8','D9','D10','D11']},
                          index= [8,9,10,11])

#do a concatnation with rows
result = pd.concat([df1,df2,df3])
print(result)
#do a concatnation with columns
result1 = pd.concat([df1,df2,df3], axis=1)
print(result1)

#merging
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']
                     })
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']
                      })
print(left)
#on='key' is the similar key that we want to merge in those two dataframes
result2= pd.merge(left,right, on= 'key')
print(result2)

#Joining

left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                    index=['K0','K1','K2'])

right = pd.DataFrame({'C':['C0','C2','C3'],
                      'D':['D0','D2','D3']},
                     index=['K0','K2','K3'])
print(right)
result3 = left.join(right)
print(result3)