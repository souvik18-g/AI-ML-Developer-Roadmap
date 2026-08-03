numbers = [10, 50, 20, 90, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)