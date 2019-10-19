import pandas as pd 
import numpy as np

df = pd.read_csv("Amazon Book Analysis/Data/Amazon Book Data.tsv", delimiter='\t')
print(df.size)

df.drop_duplicates(subset='Title',keep='last',inplace = True)

df = df.dropna()
df = df.set_index('Title')

df.to_csv("Filtered Data.tsv",sep='\t')