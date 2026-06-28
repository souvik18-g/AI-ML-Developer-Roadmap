a=int(input("enter a no.: "))
b=int(input("enter a no.: "))

if (b==0):
    raise ZeroDivisionError("hey you cant dividedno by zero")
else:
    print(f"the divison of a/b is {a/b}")