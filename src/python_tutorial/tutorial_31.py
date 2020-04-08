class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Sorry there is not enough money in your account")

    def statement(self):
        print("Account balance: £{}".format(self.balance))




class Curent(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)
    def __str__(self):
        return "{}'s Current Account: Balance: £{}".format(self.name, self.balance)

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)
    def __str__(self):
        return "{}'s Saving Account: Balance: £{}".format(self.name, self.balance)


x = Curent("Nima", 500)
print(x.name)
print(x.balance)
x.deposit(300)
x.statement()
x.withdraw(700)
x.statement()
x.deposit(1000)
print(x.balance)
x.statement()
print(x)

y = Saving("Pardis", 86000)
print(y.name)
y.deposit(14000)
y.statement()
print(y)