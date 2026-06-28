import random
n= random.randint(1,10)
a=-1
guesses=0
while (a!=n):
    a=int(input("enter a no pls: "))
    if(a>n):
        print("enter a low value than your present value")
        guesses+=1
    else:
        print("enter a higher value than your present value")
        guesses+=1    
print(f"you are guess the no {n} at {guesses} no attempt")        