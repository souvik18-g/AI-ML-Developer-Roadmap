numbers = [10, 20, 40, 30, 50]

largest = second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print(second)