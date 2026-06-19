for i in range(n):
    j=n
    while j > 1:
        print(i, j) #Outer loop runs n times, and for each iteration the inner loop runs 
                     # log n times (due to halving), so total complexity is O(n log n).”
        j = j // 2