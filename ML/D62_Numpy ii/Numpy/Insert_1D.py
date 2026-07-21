import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]  # Original array

result = np.insert(arr, 2, 100) #(array, index, value)  # Inserting 100 at index 2
print(result)  # Output: [  1   2 100   4   5]