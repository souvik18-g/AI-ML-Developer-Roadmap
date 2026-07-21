import numpy as np

# ===================== 1D =====================

arr1 = np.array([1, 2, 3, 4, 5, 6])

print(np.split(arr1, 3))
# Split 1D array into 3 equal parts

print(np.split(arr1, [2, 4]))
# Split at index 2 and index 4


# ===================== 2D =====================

arr2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print(np.split(arr2, 2, axis=0))
# Split rows (axis=0)

print(np.split(arr2, 2, axis=1))
# Split columns (axis=1)


# ===================== 3D =====================

arr3 = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(np.split(arr3, 2, axis=0))
# Split 3D array into two 2D blocks

print(np.split(arr3, 2, axis=1))
# Split rows inside each 2D block

print(np.split(arr3, 2, axis=2))
# Split columns/elements inside each row


# ===================== SPECIAL SPLITS =====================

arr4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(np.hsplit(arr4, 2))
# Horizontal split (columns)

print(np.vsplit(arr2, 2))
# Vertical split (rows)

arr5 = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(np.dsplit(arr5, 2))
# Depth split (3rd dimension)