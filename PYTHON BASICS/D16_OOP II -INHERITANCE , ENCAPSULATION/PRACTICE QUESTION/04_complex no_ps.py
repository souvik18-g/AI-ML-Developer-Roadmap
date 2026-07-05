class Complex:
   
    def __init__(self,r,i):

        self.r=r
        self.i=i

    def __add__(self, c1):
        return  Complex(self.r+c1.r,self.i+c1.i)
    
    def __str__(self):
        return f"the complex no is { self.r} +{self.i}i "
    
a =Complex(1,2)  
c1=Complex(2,4)
print(a+c1)
        