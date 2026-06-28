# n:int=3
# name:str="souvik"
def sum(a: int, b: int):
    return a + b

print(sum(6, 2))

#or here we can use ->int 

def sum(a: int, b: int)->int:
    return a + b

print(sum(6, 2))