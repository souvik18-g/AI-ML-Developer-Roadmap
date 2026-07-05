from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def Book(self,fro,to):
        print(f"ticket to book of {self.trainNo}from {fro} to {to} ")
    def status(self):
        print(f"{self.trainNo} is on time")
    def price(self,fro,to):
        print(f"the price of {self.trainNo} from {fro} to {to} is {randint(250,5000)}") 
t=train(24999) 
t.Book("howrah","goa") 
t.status()
t.price("howrah","goa")       
