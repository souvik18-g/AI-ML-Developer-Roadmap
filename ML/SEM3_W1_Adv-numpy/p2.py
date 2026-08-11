import numpy as np

x = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1 Total sum
print(np.sum(x))

#2  Mean of each row
print("Mean of each row:", np.mean(x, axis=1))

# 3. Mean of each column
print("Mean of each column:", np.mean(x, axis=0))

# 4. Maximum of each row
print("Maximum of each row:", np.max(x, axis=1))

# 5. Minimum of each column
print("Minimum of each column:", np.min(x, axis=0))

# 6. Standard deviation of each row
print("Standard deviation of each row:", np.std(x, axis=1))

# 7. Index of the maximum value
print("Index of maximum value:", np.unravel_index(np.argmax(x), x.shape)) #(np.int64(2), np.int64(2))
print("Index of maximum value:",tuple(map(int, np.unravel_index(x.argmax(), x.shape))))