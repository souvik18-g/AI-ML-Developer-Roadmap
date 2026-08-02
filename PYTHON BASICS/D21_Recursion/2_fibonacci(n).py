def fibonacci(n):
    if n < 0:
        print("Fibonacci is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n=int(input("Enter a integer value: "))
result = fibonacci(n)
for i in range(n):
    print(fibonacci(i), end=" ")