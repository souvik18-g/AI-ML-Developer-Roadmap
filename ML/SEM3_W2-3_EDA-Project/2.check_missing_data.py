import pandas as pd

df=pd.read_csv("train.csv")

print(df.isnull().sum())
print(df.isnull().mean()* 100)

