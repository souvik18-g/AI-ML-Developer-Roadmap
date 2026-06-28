import numpy as np

#1D
a=np.array([1,3,4])
print(a)
print(a.shape)

#2D
b=np.array([
    [1,2],
    [5,6]
])
print(b)
print(b.shape)

#Transpose
print(b.T)

# Dot product
x = np.array([1, 2])
y = np.array([3, 4])

print(np.dot(x, y))