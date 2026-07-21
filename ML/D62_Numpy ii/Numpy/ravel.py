import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

x = arr.ravel()  

print(arr.ravel())  # Output: [1 2 3 4]  # Flattening the 2D array to a 1D array

#its makes a "VIEW" of the original array and returns a new 1D array. The original array remains changed.
x[0] = 100

print(x)  # Output: [100   2   3   4]  # The original array remains changed
print(arr)
# [[100 2]
#  [3 4]]