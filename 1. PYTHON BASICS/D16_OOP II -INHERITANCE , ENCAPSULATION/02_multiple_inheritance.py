class employee:
    company="ITC"
    name="default"
    
    def show(self):
        print(f"the employee name is {self.name} & his company is {self.company}")

class programmer():
    company="TCS"
    def mylanguage(self):
        print (f"the employee name is {self.name} & his company is {self.company}")


class selflanguage(employee,programmer):
    language="python"  
    def showlanguage(self):
        print (f"the employee name is {self.name} & his company is {self.company} & fav language {self.language}")


a=selflanguage()
a.show()
a.mylanguage()
a.showlanguage()
     