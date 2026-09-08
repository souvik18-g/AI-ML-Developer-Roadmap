import pandas as pd

df=pd.read_csv("train.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)

