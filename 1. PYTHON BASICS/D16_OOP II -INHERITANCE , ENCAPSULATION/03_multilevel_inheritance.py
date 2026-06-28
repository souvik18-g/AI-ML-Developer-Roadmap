class employee:
    a=1

class manager(employee):
    b=2   

class company(manager):
    c=3

o=employee() 
 
o=manager()

o=company()  

print(o.a,o.b,o.c)
