import pandas as pd

df=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 28, 20, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})

#for one column

print(df.groupby("Age")["salary"].sum()) #age assending order & according this sum of that age salary

# for multiple column

print(df.groupby(["Age","Name"])[["salary","performance_score"]].sum())