import pandas as pd


# dataset = 'classic-rock-song-list.csv'
# df = pd.read_csv(dateset)
df = pd.read_csv('classic-rock-song-list.csv')
df

df.head()

df.describe()

df.info()

df.isna().sum()


df.loc[:, ['ARTIST CLEAN', 'Release Year']]

df["ARTIST CLEAN"].value_counts()
