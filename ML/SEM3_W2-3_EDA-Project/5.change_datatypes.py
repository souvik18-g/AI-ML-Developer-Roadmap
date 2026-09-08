import pandas as pd

df=pd.read_csv("train.csv")

df["Age"] = df["Age"].fillna(df["Age"].median())
print(df["Age"])

# 3. Convert to integer
df["Age"] = df["Age"].astype(int)

# 4. Check datatype
print(df.dtypes)