import time

#recursive Fibonacci

def fib_r(n):
    if n<=1:
        return n
    return fib_r(n-1)+fib_r(n-2)

# Memoization Fibonacci

memo={}
def fib_m(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_m(n - 1) + fib_m(n - 2)
    return memo[n]

# Tabulation Fibonacci

def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 40

start = time.time()
print("Recursive:", fib_r(n))
print("Time:", time.time() - start)

start = time.time()
print("\nMemoization:", fib_m(n))
print("Time:", time.time() - start)

start = time.time()
print("\nTabulation:", fib_tab(n))
print("Time:", time.time() - start)