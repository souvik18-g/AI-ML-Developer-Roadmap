row = int(input("enter row no :"))

for i in range(1,row+1):
    print(" "*(row-i)+(2*i-1)*"*")
for j in range(row,0,-1):
    print(" "*(row-j)+(2*j-1)*"*")