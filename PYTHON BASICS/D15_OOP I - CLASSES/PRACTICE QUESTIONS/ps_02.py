class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square of a no is {self.n*self.n}")   
    def cube(self):
        print(f"the cube of a no is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square of a no is {self.n**.5}")          
a=calculator(4)
a.square()
a.cube()
a.squareroot()