import numpy as np
from statistics import mode

data = [10, 20, 20, 30, 40, 50]

print("NumPy Calculations")

# Mean
print("Mean:", np.mean(data))

# Median
print("Median:", np.median(data))

# Mode
print("Mode:", mode(data)) #for mode we need "from statistics import mode"

# Variance
print("Variance:", np.var(data))

# Standard Deviation
print("Std Dev:", np.std(data))

# Percentiles
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

print("25th Percentile:", q1)
print("75th Percentile:", q3)

# IQR
print("IQR:", q3 - q1)