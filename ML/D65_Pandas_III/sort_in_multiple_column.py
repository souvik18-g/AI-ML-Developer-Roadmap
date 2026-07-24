import pandas as pd

df=pd.DataFrame({
    'Name':['Tom',"amit", 'krish', 'jack', 'john', 'james', 'joseph', 'jordan', 'jake', 'josh'],
    'Age':[20, 28, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, 67, 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000,1500, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
})

print(df)

df.sort_values(by=["Age","salary"],ascending=[True,False],inplace=True) #remember here at 1st pandas sort wrt to Age due to
                                                                       # here its write 1st place if there are any repeat vaalue in age then 
                                                                       #those salaary are deceending (high to low) sorting otherwise if all age 
                                                                       #are uniqe then not sort in salary 

print (df)
