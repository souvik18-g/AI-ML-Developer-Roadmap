class employee:
    a=1
   
    @classmethod
    def value(cls):
        print(f" here the class attribute is {cls.a} ")

    @property
    def name(self):
        return f"{self.aname}{self.bname}"
    
    @name.setter
    def name(self,me):
        self.aname=me.split(" ")[0]
        self.bname=me.split(" ")[1]


e=employee() 
e.name="Souvik Guchait"
e.a=45
e.value() 
print(e.aname,e.bname) 