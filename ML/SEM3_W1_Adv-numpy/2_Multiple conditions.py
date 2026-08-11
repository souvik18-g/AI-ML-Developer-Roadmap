import numpy as np
x = np.array([10, 20, 30, 40, 50])

result = x[(x > 20) & (x < 50)]

print(result)