import numpy as np

arr = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(arr) 


result = np.insert(
    arr,
    1,
    [[[9, 10],
      [11, 12]]],
    axis=0
)

print(result) # go into 1st index of 3d array means 2nd 2d array & paste the new 2d array at that index
print(result.shape) #(3, 2, 2)  # The shape of the resulting array is (3, 2, 2) because we inserted a new 2D array in the first dimension

result = np.insert(
    arr,
    1,
    [[9, 10],
     [11, 12]],
    axis=1
)

print(result) # go into each 2D array and insert the new values into the 2nd dimension (rows) at index 1
print(result.shape)#(2, 3, 2)  # The shape of the resulting array is (2, 3, 2) because we inserted a new row in the 2nd dimension


result = np.insert(
    arr,
    1,
    [[9, 10],
     [11, 12]],
    axis=2
)

print(result) # go into each 2D array and insert the new values into the 3rd dimension (depth) at index 1 
print(result.shape)#(2, 2, 3)  # The shape of the resulting array is (2, 2, 3) because we inserted a new column in the depth dimension