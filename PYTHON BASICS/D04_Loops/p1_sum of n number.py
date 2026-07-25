# Practice 1 - Sum from 1 to n

n = int(input("Enter n: "))


sum = 0

for i in range(1, n + 1):
   sum += i

print(f"sum is {sum}")