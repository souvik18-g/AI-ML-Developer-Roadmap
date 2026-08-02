def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n-1) + n 

n = int(input("Enter a positive integer: "))
result = sum(n)
print(f"The sum of the first {n} natural numbers is {result}.")