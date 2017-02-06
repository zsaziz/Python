from bankaccount import BankAccount


class BankAccountsManager:
    def __init__(self):
        self.acc_list = []

    def add_account(self, ID, name, balance=0.00):
        self.acc_list.append(BankAccount(ID, name, balance))

    def make_deposit(self, ID, amount):
        for x in self.acc_list:
            if x.has_ID(ID):
                x.deposit(amount)
                return
        raise Exception("Account not found")

    def make_withdrawl(self, ID, amount):
        for x in self.acc_list:
            if x.has_ID(ID):
                x.withdraw(amount)
                return
        raise Exception("Account not found")

    def get_balance(self, ID):
        for x in self.acc_list:
            if x.has_ID(ID):
                return x.balance
        raise Exception("Account not found")

    def get_account_report(self, ID):
        for x in self.acc_list:
            if x.has_ID(ID):
                return "ID: {}\nName: {}\nBalance: ".format(ID, x.name) + "{0:.2f}".format(x.balance)
        raise Exception("Account not found")