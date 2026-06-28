class employee:
    name ="Souvik"
    language= "py" 
    age= 20
    
    def getinfo(self):
        print(f"My name is {self.name} & my age is {self.age} also now i learn {self.language}")

souvik=employee()  
souvik.language="C"
print(souvik.name,souvik.age,souvik.language) 
souvik.getinfo()

