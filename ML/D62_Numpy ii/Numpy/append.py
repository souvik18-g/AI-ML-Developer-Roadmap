import numpy as np

arr = np.array([1, 2, 3])

new_arr = np.append(arr, 4) #Appending 4 to the original array

print(new_arr) 

#for 2d,3d arrays, we can append along a specific axis using the axis parameter like axis=0 for rows and axis=1 for columns. If axis is not specified, the input arrays are flattened before use.