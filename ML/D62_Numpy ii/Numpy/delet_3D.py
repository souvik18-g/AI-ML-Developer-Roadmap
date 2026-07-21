import numpy as np

arr = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

new_arr = np.delete(arr, 0, axis=0) # Deleting the first 2D array (index 0) from the 3D array
print(new_arr)

new_arr = np.delete(arr, 0, axis=1) # Deleting the first row (index 0) from each 2D array in the 3D array
print(new_arr)

new_arr = np.delete(arr, 0, axis=2) # Deleting the first column (index 0) from each 2D array in the 3D array
print(new_arr)