import pandas as pd

df=pd.read_csv("train.csv")


# check the age column number which null
print(df["Age"].isnull().sum())
#in nan part fill median
df["Age"] = df["Age"].fillna(df["Age"].median())
print(df["Age"])
# check the age column number which null
print(df["Age"].isnull().sum())

#fill here max number s/c part where null
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
print(df["Embarked"])
print(df["Embarked"].isnull().sum())

#delete Cabin column
df.drop(columns=["Cabin"], inplace=True)
print(df.columns)


df["Age"] = df["Age"].astype(int)
print(df.dtypes)

