class employee:
    name ="Souvik"
    language= "py" # this is class attribute
    age= 20
    def __init__(self,name,age,language): #this called dunder method  which automticlly called
        self.name=name
        self.age=age
        self.language=language
        print("right now i learn oops in python")
    def getinfo(self):
        print(f"My name is {self.name} & my age is {self.age} also now i learn {self.language}")

souvik=employee("Avik",20,"C")  
# souvik.language="C" this is instant attribute
print(souvik.name,souvik.age,souvik.language) 
souvik.getinfo()

