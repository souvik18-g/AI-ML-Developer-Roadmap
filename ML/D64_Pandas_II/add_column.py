import pandas as pd

data={
    'Name':['Tom', 'nick', 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 21, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 90, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000, 2000, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
}


df=pd.DataFrame(data)

df['bonus'] = df['salary'] * 0.1 #here we are add a new column to the existing dataframe at the end of the dataframe
print(df)

df.insert(2, 'city', ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']) #here we are add a new column to the existing dataframe at the 2nd index of the dataframe
print("new_dataframe after adding new column at 2nd index") #(index, column_name, column_value)
print(df)