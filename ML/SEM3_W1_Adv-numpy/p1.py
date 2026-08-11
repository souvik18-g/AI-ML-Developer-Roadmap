import numpy as np

x=np.array([10,20,-3,0,-7,50,90,60,20,-2])

#1.Find all values greater than 50.

print(x[x>50])

#2.Find values between 20 and 80.

print(x[(x>20) & (x<80)])

#3.Replace all negative values with

y=np.where(x<0,0,x)
print(y)

# 4.Find indices of values greater than the mean.


index=np.where(x>np.mean(x))[0] #without[0] here output (array([5, 6, 7]),)
print(index)                    #with[0] here output [5 6 7]

# 5.Extract elements at indices [1, 3, 5].

print(x[[1, 3, 5]])