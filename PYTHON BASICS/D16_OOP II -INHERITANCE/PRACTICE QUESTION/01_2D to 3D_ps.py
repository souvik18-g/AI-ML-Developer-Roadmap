class TwoD:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print (f"TwoD is {self.i}i+{self.j}j" )  

class ThreeD(TwoD):
    def __init__(self,i,j,k):
     super().__init__(i,j)
     self.k=k
    def show(self):
        print (f"ThreeeD is {self.i}i+{self.j}j+{self.k}k" )  


a=TwoD(1,2)
b=ThreeD(5,6,3)

b.show()



        