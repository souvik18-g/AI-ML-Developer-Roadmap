import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr)

result = np.insert(arr, 1, [5, 6], axis=0) #(array, index, value, axis)  # Inserting [5, 6] as a new row at index 1 
                                           #axis=0 means we are inserting along the rows (vertically)
print(result)

result = np.insert(arr, 1, [5, 6], axis=1) #(array, index, value, axis)  # Inserting [5, 6] as a new column at index 1 
                                           #axis=1 means we are inserting along the columns (horizontally)
print(result)

result = np.insert(arr, 1, [5, 6], axis=None) #(array, index, value, axis)  # Inserting [5, 6] into the flattened array at index 1
                                           #axis=None means we are inserting along the flattened array
print(result)
result = np.insert(arr, 1, [5, 6])  # axis=None is the default value, so this is equivalent to the previous line
print(result)  #(array, index, value)  # Inserting [5, 6] into the flattened array at index 1