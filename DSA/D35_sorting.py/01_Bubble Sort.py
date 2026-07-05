arr = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if not swapped:
            break

print("Before Bubble Sort:")
print(arr)

bubble_sort(arr)

print("After Bubble Sort:")
print(arr)                # here big no contineiusly compare small no & go right 
                           # so bubble sort is small to big arrangement