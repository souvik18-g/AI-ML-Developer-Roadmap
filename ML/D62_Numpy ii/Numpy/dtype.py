import numpy as np

array=np.array([1,2.3,3,4.3,5])  
print(array.dtype)  # Output: float64

array=np.array([1,2,3,4,5])  
print(array.dtype)  # Output: int64

array=np.array([1,2,"hello",4,5]) 
print(array.dtype)  # Output: <U11  #This NumPy array stores Unicode strings, and each element can have up to 21 characters

array=np.array([1,2,True,4,5])    # True is treated as 1 and False as 0, so the array will be of integer type
print(array.dtype)  # Output: int64

array=np.array([True,False,True])
print(array.dtype)  # Output: bool