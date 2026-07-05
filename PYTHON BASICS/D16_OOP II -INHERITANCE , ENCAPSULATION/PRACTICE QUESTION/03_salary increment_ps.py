class Employee:
    salary= 234
    increment=20

    @property
    def salaryAfterIncrement(self):
        return(self.salary+self.salary*self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,s):
        self.increment= (self.salary/self.salary-1)*100




a=Employee()  
print(a.salaryAfterIncrement) 
a.salary=280.8
print(a.increment)  
