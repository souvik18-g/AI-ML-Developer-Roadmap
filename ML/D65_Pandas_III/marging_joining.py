import pandas as pd

df_1=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jakem', 'josh'],
    'Age':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})

df_2=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'syam', 'joseph', 'jordan', 'oliv', 'josh'],
    'takes leaves':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'Attendence':[82, 69, 75, 60, 85, 98, 80, 65, 88, 92],
    'bonus':[100,150, 150, 120, 250, 300, 180, 220, 270, 320]
})

merged_inner=pd.merge(df_1,df_2,on='Name',how="inner") #here all common(intersection) name both dataframe printed & according them all valus are came
print("inner join\n")
print(merged_inner)

merged_outer=pd.merge(df_1,df_2,on='Name',how="outer") #here all value (union) name both dataframe printed & according them all valus are came
print("outer join\n")
print(merged_outer)

merged_left=pd.merge(df_1,df_2,on='Name',how="left") #here all left datafreme name came both dataframe colums are printed but which have not in datafreame 1 that show NaN
print("left join\n")
print(merged_left)

merged_right=pd.merge(df_1,df_2,on='Name',how="right") #here all right datafreme name came both dataframe colums are printed but which have not in datafreame 1 that show NaN
print("right join\n")
print(merged_right)