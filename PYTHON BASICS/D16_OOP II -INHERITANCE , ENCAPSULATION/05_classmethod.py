class employee:
    a = 1

    @classmethod
    def value(cls):   # ← THIS is mandatory
        print(f"the class attribute is {cls.a}")

e = employee()
e.a = 45

e.value()