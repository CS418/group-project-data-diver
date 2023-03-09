import pandas as pd

df = pd.read_csv('Crime.csv')
df = df[df['Year'] >= 2016]
df = df[['Primary Type', 'Description', 'Location Description', 'Domestic', 'Year', 'Date', 'ID']]
print(df.columns)
print(df)
df.to_pickle('crime_reduced.pkl')
