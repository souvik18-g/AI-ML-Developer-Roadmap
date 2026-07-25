# Practice 3 - Count Digits

number = int(input("Enter a number: "))

count = 0

temp = abs(number)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print(f"total number in this number: {count}")
