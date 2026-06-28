data = [1, 2, 2, 3, 4, 5, 100]
# Mean Formula:
# mean = Σx / n
def mean(arr):
    return sum(arr) / len(arr)


# Median Formula:
# Odd n  -> middle value
# Even n -> (middle1 + middle2) / 2
def median(arr):
    arr = sorted(arr)
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Mode Formula:
# Mode = value with highest frequency
def mode(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())

    for key, value in freq.items():
        if value == max_freq:
            return key


# Variance Formula:
# variance = Σ(x - mean)² / N
def variance(arr):
    m = mean(arr)

    return sum((x - m) ** 2 for x in arr) / len(arr)


# Standard Deviation Formula:
# std_dev = √variance
def std_dev(arr):
    return variance(arr) ** 0.5


# Percentile Position Formula:
# index = (p/100) * (n - 1)
#
# Interpolation Formula:
# P = lower*(1-weight) + upper*weight
def percentile(arr, p):
    arr = sorted(arr)

    index = (p / 100) * (len(arr) - 1)

    lower = int(index)
    upper = lower + 1

    if upper >= len(arr):
        return arr[lower]

    weight = index - lower

    return arr[lower] * (1 - weight) + arr[upper] * weight


# IQR Formula:
# IQR = Q3 - Q1
# Q1 = 25th percentile
# Q3 = 75th percentile
def iqr(arr):
    q1 = percentile(arr, 25)
    q3 = percentile(arr, 75)

    return q3 - q1

arr = [1, 2, 2, 3, 4, 5, 100]

print("Mean Formula: Σx / n")
print("Mean:", mean(data))

print("\nMedian Formula:")
print("Odd n  -> middle value")
print("Even n -> (middle1 + middle2) / 2")
print("Median:", median(data))

print("\nMode Formula:")
print("Value with highest frequency")
print("Mode:", mode(data))

print("\nVariance Formula:")
print("Σ(x - mean)² / N")
print("Variance:", variance(data))

print("\nStandard Deviation Formula:")
print("√variance")
print("Std Dev:", std_dev(data))

print("\nPercentile Position Formula:")
print("index = (p/100) * (n - 1)")
print("25th Percentile:", percentile(data, 25))
print("75th Percentile:", percentile(data, 75))

print("\nIQR Formula:")
print("IQR = Q3 - Q1")
print("IQR:", iqr(data))