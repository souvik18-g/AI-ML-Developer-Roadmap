import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dot product
result = np.dot(a, b)

print(result)

#output
#32


import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication using np.dot()
result = np.dot(a, b)

print(result)


#output
#[[19 22]
#[43 50]]