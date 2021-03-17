import pandas as pd
import csv

df = pd.read_csv('allStars.csv')

print(df.shape)

del df['Luminosity']
del df['Star_Names']
del df['Distance1']
del df['Mass1']
del df['Radius1']
del df['Unnamed: 0']
del df['Unnamed: 6']

print(df.shape)
print(list(df))

df.to_csv('final.csv')