class BankAccount:
    def __init__(self, ID, name, balance=0.00):
        self.name = name
        self.ID = ID
        self.balance = balance

    def has_ID(self, target):
        if target == self.ID:
            return True
        return False

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            raise Exception("No action: Amount greater than available balance")
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def get_balance(self):
        return self.balance