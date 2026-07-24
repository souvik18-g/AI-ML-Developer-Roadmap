import pandas as pd

df=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})

print(df)

print(df.sort_values(by="Age"))  #both  same if we don't write assending =True it will default so print small to large
print(df.sort_values(by="Age",ascending=True))

print(df.sort_values(by="Age",ascending=False)) #for get decending big to small we need use that use False not possible to decending=True 