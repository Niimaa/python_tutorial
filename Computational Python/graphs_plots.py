import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
popularity = {'character':['spiderman','spiderman','superman','superman','batman','batman','tom','tom','jerry','jerry'], 'popularity':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'],
              'score1':[35,54,23,52,60,60,57,44,59,45], 'score2':[34,58,29,43,70,60,57,45,63,45], 'gender':['male','male','male','male', 'male','male','male','male','female', 'female']}

dataframe1 = pd.DataFrame(popularity, columns=pd.Index(['character','popularity','score1','score2','gender'], name= 'Attributes'))
print(dataframe1)

#it automatically find the numeric columns
graph1 = dataframe1.plot('character')
plt.show()

graph2 = dataframe1.plot('character', kind= 'bar')
plt.show()
# for the next two axis has to be numeric
graph3 = dataframe1.plot('score1','score2', kind= 'scatter')
plt.show()

graph4 = dataframe1.plot('score1','score2', kind= 'pie')
plt.show()

graph1 = dataframe1.plot('character')
graph1.set_xlabel("super_hero")
graph1.set_ylabel("scores")
graph1.set_title("scores of super heros")
plt.show()
#using stacked to put to results on top of each others
graph2 = dataframe1.plot('character', kind= 'bar', stacked= True)
graph2.set_xlabel("super_hero")
graph2.set_ylabel("scores")
graph2.set_title("scores of super heros")
plt.show()