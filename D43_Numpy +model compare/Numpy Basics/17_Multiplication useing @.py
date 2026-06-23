import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication using @
result = a @ b

print(result)

#output
#[[19 22]
#[43 50]]