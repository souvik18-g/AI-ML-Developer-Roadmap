class Animal:                                  # ---- Parent (Base) Class ----
    def __init__(self, name, sound):            # constructor / dunder method
        self.name = name                        # instance attribute           #step-4  name = "Rex"                                                      
        self.sound = sound                       # instance attribute      #            sound = "Bark" 

    def speak(self):                             # instance method (to be overridden)
        print(f"{self.name} makes a sound: {self.sound}")  #step 5


class Dog(Animal):                              # ---- Child Class (Inheritance) ----
    def __init__(self, name):                    # constructor      #step-2   Dog.__init__(self, "Rex")
        super().__init__(name, "Bark")           # super() -> calls Animal's __init__  #step-3    super().__init__("Rex", "Bark")

    def speak(self):                             # method overriding (Polymorphism)
        super().speak()                          # super() -> calls Animal's speak() too  
        print(f"{self.name} says  bark!")     # extra behavior specific to Dog    #step 5


class Cat(Animal):                              # ---- Child Class (Inheritance) ----
    def __init__(self, name):                    # constructor
        super().__init__(name, "Meow")           # super() -> calls Animal's __init__

    def speak(self):                             # method overriding (Polymorphism)
        super().speak()                          # calls Animal's speak()
        print(f"{self.name} says Meow Meow!")     # extra behavior specific to Cat


class Bird(Animal):                             # ---- Child Class (Inheritance) ----
    def __init__(self, name):                    # constructor
        super().__init__(name, "Chirp")          # super() -> calls Animal's __init__

    def speak(self):                             # method overriding (Polymorphism)
        super().speak()                          # calls Animal's speak()
        print(f"{self.name} says Tweet Tweet!")   # extra behavior specific to Bird


# ---- Object creation / instances ----
d = Dog("Rex")          # instance of Dog (IS-A Animal)    #step-1
c = Cat("Whiskers")      # instance of Cat (IS-A Animal)
b = Bird("Tweety")       # instance of Bird (IS-A Animal)

# ---- Method calls -> same method name, different behavior (Polymorphism) ----
d.speak()                
c.speak()                                    
b.speak()