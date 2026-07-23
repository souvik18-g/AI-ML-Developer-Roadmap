import pandas as pd

data={
    'Name':['Tom', 'nick', 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 21, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 90, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000, 2000, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
}

df=pd.DataFrame(data)
print(df)

#df.loc[index, column_name] = new_value #here we are updating the value of a specific column at a specific index
df.loc[0,"salary"] = 1100 #here we are updating the value of salary column at index 0 
df.loc[1,"performance_score"] = 95 #here we are updating the value of performance_score column at index 1
print("new_dataframe after updating the values of salary and performance_score columns")
print(df)

print("update whole column values")
df['salary'] = df['salary'] * 1.1 #here we are updating the whole column values of salary by 10%
print("new_dataframe after updating the whole salary column")
print(df)