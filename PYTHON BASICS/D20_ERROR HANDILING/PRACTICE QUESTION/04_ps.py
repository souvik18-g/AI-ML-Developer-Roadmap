 
try:

    a=int(input("enter a valid no:"))
    b=int(input("enter a valid no:"))
    print(a/b)
except ZeroDivisionError as v:
    print("infinte")
