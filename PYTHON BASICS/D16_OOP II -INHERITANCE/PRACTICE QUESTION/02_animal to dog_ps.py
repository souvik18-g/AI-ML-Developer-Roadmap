class animal:
    pass
class pet(animal):
    pass
class Dog(pet):

    @staticmethod
    def bark():
        print("bow bow!")


b=Dog() 
b.bark()      