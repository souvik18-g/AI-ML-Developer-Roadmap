import numpy as np

arr=np.array([1, 2, np.nan, 4, np.nan, 6])
print(arr) # [ 1.  2. nan  4. nan  6.]

print(np.isnan(arr)) # [False False  True False  True False]

print(np.nan_to_num(arr)) # [1. 2. 0. 4. 0. 6.]
print(np.nan_to_num(arr, nan=-1)) # [ 1.  2. -1.  4. -1.  6.] nun= custom value to replace nan