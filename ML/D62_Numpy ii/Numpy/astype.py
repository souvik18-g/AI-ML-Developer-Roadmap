import numpy as np

array = np.array([1, 2, 3, 4, 5])  
print(array.astype(float))  # Output: [1. 2. 3. 4. 5.]  # Converting integer array to float

array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(array.astype(int))  # Output: [1 2 3 4 5]  # Converting float array to integer

array = np.array([1, 2, 3, 4, 5])
print(array.astype(str))  # Output: ['1' '2' '3' '4' '5']  # Converting integer array to string