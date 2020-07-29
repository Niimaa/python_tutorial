import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,30,60,60,57,44,43,45], 'score2':[34,30,29,43,70,60,57,45,63,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

graph2 = dataframe1.plot('character', kind= 'bar', stacked= True)
graph2.set_xlabel("super_hero")
graph2.set_ylabel("scores")
graph2.set_title("scores of super heros")
plt.show()

histo1 = dataframe1['score1'].hist()
plt.show()

