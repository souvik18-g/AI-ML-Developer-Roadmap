import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Row slicing and column slicing
print(matrix[0:2, 1:3])    # Rows -> 0 to 1
                           # Columns -> 1 to 2

#output

# [[2 3]
#  [5 6]]