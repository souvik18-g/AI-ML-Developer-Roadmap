import numpy as np


x = np.array([10, 25, 40, 15])

result = np.where(x >= 20, "Pass", "Fail") #if condision satisfy  print 1st option otherwise 2nd option

print(result)

x = np.array([10, 25, 40, 15])

print(np.where(x > 20)) # here output is the index of those which are satisfy condition