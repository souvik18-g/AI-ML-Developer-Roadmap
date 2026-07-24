import pandas as pd

df_1=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jakem', 'josh'],
    'Age':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})

df_2=pd.DataFrame({
    'Name':['jerry',"amrit", 'krishna', 'jackline', 'johnny', 'syamol', 'josua', 'jason', 'oliv', 'jonty'],
    'takes leaves':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'Attendence':[82, 69, 75, 60, 85, 98, 80, 65, 88, 92],
    'bonus':[100,150, 150, 120, 250, 300, 180, 220, 270, 320]
})

df_3=pd.concat([df_1,df_2],ignore_index=True) #row wise where axis=0
print(df_3)

df_4=pd.concat([df_1,df_2],axis=1,ignore_index=True) #column wise where axis=1
print(df_4)