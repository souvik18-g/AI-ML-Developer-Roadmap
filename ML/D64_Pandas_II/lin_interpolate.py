import pandas as pd

data={
    'Age':[20, None, 19, 18, 22, 23, 24, 25, 26, 27],
    'performance_score':[80, None , 70, 60, 85, 95, 75, 65, 88, 92],
    'salary':[1000, None, 1500, 1200, 2500, 3000, 1800, 2200, 2700, 3200]
}

df=pd.DataFrame(data)
print(df)

#interpolate() is another way to fill missing (NaN) values. Instead of using a fixed value like 0
#or the mean, it tries to guess the missing value based on neighboring values.
# Linear_interpolate=df.interpolate(method='linear', axis=0, inplace=True) #filling missing values with linear interpolation
#
Linear_interpolate=df.interpolate(method='linear', axis=0, inplace=True) #filling missing values with linear interpolation
print(Linear_interpolate) #NOT support strings # for all column

# we can write this like 
df['Age'] = df['Age'].interpolate(method='linear') #filling missing values with linear interpolation
print(df) # only one column