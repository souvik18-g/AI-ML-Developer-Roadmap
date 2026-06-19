def insertion_sort(arr):

    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key


arr = [5, 3, 4,7,1]

print("Before Insertion Sort:")
print(arr)

insertion_sort(arr)

print("After Insertion Sort:")
print(arr)