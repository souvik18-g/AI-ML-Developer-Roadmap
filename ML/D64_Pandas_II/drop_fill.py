import pandas as pd

data={
    'Name':['Tom', 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, None, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, None , 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000, None, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
}

df=pd.DataFrame(data)
print(df)

# print(df.dropna()) #here we are removing the rows which have missing values in any of the columns and it will return a new dataframe without modifying the existing dataframe
df.fillna(0, inplace=True)
print(df)
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df) #here we are filling the missing values with the mean of the column and it will modify the existing dataframe
