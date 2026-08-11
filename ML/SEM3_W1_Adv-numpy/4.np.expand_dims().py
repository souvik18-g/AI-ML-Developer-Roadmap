import numpy as np

x = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])


print("Shape:", x.shape) #gives(3,4)
y = np.expand_dims(x, axis=0)

print(y)
print("Shape:", y.shape) # here use axis=0 makes whole 2d in a single 3d (1,3,4)

y = np.expand_dims(x, axis=1)

print(y)
print("Shape:", y.shape) #here use axis=1 makes whole 2d in 3 row based 3d array (3,1,4)


y = np.expand_dims(x, axis=2)

print(y)
print("Shape:", y.shape) #here whole array 2d row to 3 3d array (3, 4, 1)
