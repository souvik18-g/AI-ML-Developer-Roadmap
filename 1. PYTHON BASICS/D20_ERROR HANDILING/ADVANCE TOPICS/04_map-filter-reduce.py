from functools import reduce
#map
l=[1,2,3,4,5,6]
square=lambda x:x*x
sqlist= map(square,l)
print(list(sqlist))
 
 # filter 

def even(n):
    if (n%2==0):
        return True
    return False


onlyeven=filter(even,l)
print(list(onlyeven))

# reduce

def sum(a,b):
    return(a+b)
print(reduce(sum,l))