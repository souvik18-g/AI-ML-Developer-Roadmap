import pandas as pd

df=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})


 # here we perform aggregation  (sum,max,min,count,median,std,var,mean)
mean =df['Age'].mean()
print(mean)

max =df['Age'].max()
print(max)
                                      # for get single data
min =df['Age'].min()
print(min)

sum =df['Age'].sum()
print(sum)


print(df["Age"].agg(["mean","max","std","var"])) # for get multiple data

