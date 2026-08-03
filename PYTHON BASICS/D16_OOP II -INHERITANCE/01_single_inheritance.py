class employee:
    company="ITC"
    name="default"
    
    def show(self):
        print(f"the employee name was {self.name} & his company was {self.company}")

class programmer(employee):
    company="TCS"
    def language(self):
        print (f"the employee name is {self.name} & his company is {self.company}")

a=employee()
b=programmer()

a.show()
b.language()

b.show()