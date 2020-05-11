import pandas as pd

csv_path = 'C:/Users/nafs080/work/codes/python_packages/python_tutorial/Python for Data Science/file1.csv'
df = pd.read_csv(csv_path)

df.head()

songs = {"Album":["Thriller","Back in Black"],"Released":["1982","1980"]}

songs_frame = pd.DataFrame(songs)
print(songs_frame)

x = songs_frame[['Released']]
print(x)

#loc is primarily label based; when two arguments are used, you use column headers and row indexes to select the data you want. loc can also take an integer as a row or column number.

print(songs_frame.loc[0,"Album"])

#iloc is integer-based. You use column numbers and row numbers to get rows or columns at particular positions in the data frame.
print(songs_frame.iloc[0,0])
#By default, ix looks for a label. If ix doesn't find a label, it will use an integer. This means you can select data by using either column numbers and row numbers or column headers and row names using ix.

#make slice with loc and iloc
slice = songs_frame.iloc[0:2,0:2]
print(slice)
slice = songs_frame.loc[0:2,'Album':'Released']
print(slice)

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe

print(df.head())

# Access to the column "Length"

x = df[['Length']]
print(x)

# Get the column as a series

x = df['Length']
print(x)

# Get the column as a dataframe

x = type(df[['Artist']])
print(x)


# # Access to multiple columns

y = df[['Artist','Length','Genre']]
print(y)

