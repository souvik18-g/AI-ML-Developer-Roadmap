class BankAccount:                              # ---- Class ----
    def __init__(self, owner, balance=0):        # constructor / dunder method
        self.owner = owner                        # public attribute
        self._pin = "1234"                        # protected attribute (single underscore, convention only)
        self.__balance = balance                  # private attribute (double underscore -> name mangled)

    @property                                     # getter decorator
    def balance(self):                            # exposes __balance safely (read-only access)
        return self.__balance

    def deposit(self, amt):                       # instance method
        if amt <= 0:                               # validation
            print("Deposit amount must be positive")
            return
        self.__balance += amt                      # modifies private attribute internally
        print(f"Deposited {amt}. New balance: {self.__balance}")

    def withdraw(self, amt):                       # instance method
        if amt <= 0:                                # validation
            print("Withdraw amount must be positive")
            return
        if amt > self.__balance:                    # validation
            print("Insufficient balance")
            return
        self.__balance -= amt                       # modifies private attribute internally
        print(f"Withdrew {amt}. New balance: {self.__balance}")


# ---- Object creation / instance ----
acc = BankAccount("Souvik", 1000)                 # instance of BankAccount

# ---- Method calls (controlled access, not direct attribute change) ----
acc.deposit(500)                                   # balance: 1000 -> 1500
acc.withdraw(2000)                                 # blocked -> insufficient balance
acc.withdraw(300)                                   # balance: 1500 -> 1200

print(acc.balance)                                 # accessed via @property, NOT acc.__balance directly

# print(acc.__balance)                              # this line would ERROR -> private attribute