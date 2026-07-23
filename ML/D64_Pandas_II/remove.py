import pandas as pd

data={
    'Name':['Tom', 'nick', 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 21, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 90, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000, 2000, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
}

df=pd.DataFrame(data)
print(df)

df.drop(columns=['performance_score'], inplace=True) #here we are removing the performance_score column from the existing dataframe
print("new_dataframe after removing the performance_score column\n")
print(df) # here we change the main df dataframe use True means here original change 

new=df.drop(columns=['Age'], inplace=False) #here we are removing the age column from the existing dataframe and creating a new dataframe without modifying the existing dataframe
print("new_dataframe after removing the age column without modifying the existing dataframe\n")
print(new)
print(df) # here original df not change