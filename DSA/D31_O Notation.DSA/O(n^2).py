n = 3
for i in range(n):
    for j in range(n):
        print(i, j)



a = [1,2,3]
b = [4,5,6]
for i in a:
    for j in b:
        print(i, j) 



n = 3
for i in range(n):
    for j in range(i):
        print(i, j) 



n = 3
for i in range(n):
    for j in range(n, i, -1):
        print(i, j)                      #O(n²) = work grows like “n times n”,Loop inside loop (both depend on n) → O(n²)