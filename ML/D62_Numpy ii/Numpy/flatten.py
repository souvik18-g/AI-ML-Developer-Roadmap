import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

x = arr.flatten()  # Flattening the 2D array to a 1D array

print(arr.flatten())  # Output: [1 2 3 4]  # Flattening the 2D array to a 1D array

#its makes a "copy" of the original array and returns a new 1D array. The original array remains unchanged.
x[0] = 100

print(x)  # Output: [100   2   3   4]  # The original array remains unchanged
print(arr)
# [[1 2]
#  [3 4]]