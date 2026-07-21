import numpy as np


#1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack((a, b))) # Output: [1 2 3 4 5 6]  # Stacking arrays in sequence horizontally (column wise)
print(np.vstack((a, b))) # Output: [[1 2 3]
                         #          [4 5 6]] # Stacking arrays in sequence vertically (row wise)


 #2D arrays
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.hstack((a, b)))   # Output: [[1 2 5 6]
                            #          [3 4 7 8]] # Stacking arrays in sequence horizontally (column wise)
print(np.vstack((a, b)))   # Output: [[1 2]
                            #          [3 4]
                            #          [5 6]
                            #          [7 8]] # Stacking arrays in sequence vertically (row wise)