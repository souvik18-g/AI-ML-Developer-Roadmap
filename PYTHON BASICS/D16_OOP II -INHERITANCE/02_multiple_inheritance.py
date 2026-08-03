class employee:
    company="ITC"
    name="default"
    salary=10000
    def show(self):
        print(f"the employee name was {self.name} & his company was {self.company} & his salary was {self.salary}")

class programmer:
    company="TCS"
    salary=15000
    def mylanguage(self):
        print (f"the employee name is {self.name} & his company is {self.company}& his salary is {self.salary}" )


class selflanguage(employee,programmer):
    language="python"  
    def showlanguage(self):
        print (f"the employee name is {self.name} & his company is {self.company} & fav language {self.language}")


a=selflanguage()
a.show()
a.mylanguage()
a.showlanguage()
     