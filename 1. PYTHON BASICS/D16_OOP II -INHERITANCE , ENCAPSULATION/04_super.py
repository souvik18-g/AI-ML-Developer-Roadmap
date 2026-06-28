class employee:
    def __init__(self):
        print("its a emplyoee part")
    a=1

class manager(employee):
    def __init__(self):
        super().__init__()
        print("its a manager part")
    b=2   

class company(manager):
    def __init__(self):
        super().__init__()
        print("its a company part")
    c=3

# o=employee()
# print(o.a) 
# o=manager()
# print(o.a,o.b)


o=company()  
print(o.a,o.b)
