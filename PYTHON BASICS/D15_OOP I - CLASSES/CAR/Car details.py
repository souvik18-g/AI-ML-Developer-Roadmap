class car:                               #make class car:             
    def __init__(self,brand,speed):      # create constructor with two parameters brand and speed
        self.brand=brand                 # instance variable brand is assigned to self.brand
        self.speed=speed

    def accelerate(self,amount):                   # create instance method accelerate
        self.speed+=amount                         # increase speed by the given amount    

    def brake(self,amount):                        # create instance method brake
        self.speed-=amount                         # decrease speed by the given amount

    def __str__(self):                               # create instance method __str__ to return string representation of the object
        return f"Car brand: {self.brand}, Speed: {self.speed} km/h"  # return formatted string with brand and speed


car1=car("Toyota",100)                       # create an object of car with brand "Toyota" and speed 100
car2=car("Tesla",0)                            # create an object of car with brand "Tesla" and speed 0
car1.accelerate(50)                            # call accelerate method on car1 with amount 50
car2.accelerate(100)                           # call accelerate method on car2 with amount 100
car1.brake(30)                                 # call brake method on car1 with amount 30
car2.brake(50)                                 # call brake method on car2 with amount 50
print(car1)                                    # print the string representation of car1    
print(car2)                                    # print the string representation of car2