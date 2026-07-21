import numpy as np

D1_array = np.array([1, 2, 3, 4, 5])  # Creating a 1D array

D2_array = np.array([[1, 2, 3], [4, 5, 6]])  # Creating a 2D array
D3_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Creating a 3D array


print(D1_array.ndim)  # Output: 1
print(D2_array.ndim)  # Output: 2
print(D3_array.ndim)  # Output: 3
    