class programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programmer("thomas",14000,700001)  
print(p.name,p.salary,p.pin,p.company)      
r=programmer("roger",14000,700001)  
print(r.name,r.salary,r.pin,r.company)              