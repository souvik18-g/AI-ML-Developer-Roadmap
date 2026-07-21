import numpy as np

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

new_arr = np.delete(arr, 1, axis=0) # Deleting the second row (index 1) from the 2D array
print(new_arr)

new_arr = np.delete(arr, 0, axis=1) # Deleting the first column (index 0) from the 2D array
print(new_arr)