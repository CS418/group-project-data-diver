import pandas as pd

df: pd.DataFrame = pd.read_csv('Crime.csv')
df = df[df['Year'] >= 2019]
df = df[['Primary Type', 'Description', 'Location Description', 'Domestic', 'Year', 'Date', 'ID']]
print(df.columns)
print(df)
df = df.set_index('ID')

df.to_csv('crime_reduced.csv')

df: pd.DataFrame = pd.read_csv('crime_reduced.csv')


def describe(df):
    # check data types and size
    print('\n*** Size and data type')
    print(df.size)
    print(df.dtypes)
    # count percent NaN values of each column
    print('\n*** NaN percent each column')
    print(df.isna().sum() / df.size)


def inspect_values(df):
    for col in df:
        # count percent of each value showing up in the data
        print('\n', df[col].value_counts() / df.size)


describe(df)
# column Location Description has 0.056294% NaN value
# we can drop that
df1 = df[~df['Location Description'].isna()]
describe(df1)
inspect_values(df1)

