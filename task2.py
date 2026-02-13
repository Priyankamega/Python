class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Amount:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn Amount:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")

account = BankAccount("John", 1000)


