import numpy as np

x = np.array([
    [[10, 20, 30, 40]],
    [[50, 60, 70, 80]],
    [[90, 100, 110, 120]]
])

print(x)
print("Shape:", x.shape)  

y = np.squeeze(x) #squeeze() only removes dimensions whose size is 1.

print(y)
print("Shape:", y.shape)   #here (1,3,4)---->(3,4)