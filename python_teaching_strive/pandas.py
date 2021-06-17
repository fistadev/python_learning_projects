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


filterrrrr = df['ARTIST CLEAN'] == 'ZZ Top'
df_zz = df[filterrrrr][['ARTIST CLEAN', 'Release Year']]
df_zz
