import numpy as np

arr1 = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(arr1) # [ 1.  2. inf  4. -inf  6.]

print(np.isinf(arr1)) # [False False  True False  True False]

print(np.nan_to_num(arr1,posinf=1000,neginf= -1000)) # [ 1.  2. 1000.  4. -1000.  6.]