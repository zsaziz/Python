from bankaccount import BankAccount
from bankaccountsmanager import BankAccountsManager
import unittest


class TestBankAccount(unittest.TestCase):

    def test_has_ID(self):
        za = BankAccount(1, 'Zain', 100)
        self.assertTrue(za.has_ID(1))
        self.assertFalse(za.has_ID(2))

    def test_withdraw(self):
        za = BankAccount(1, 'Zain', 100)
        za.withdraw(50)
        self.assertEqual(za.get_balance(), 50)
        za.withdraw(50)
        self.assertEqual(za.get_balance(), 0)
        with self.assertRaises(Exception):
            za.withdraw(1)

    def test_deposit(self):
        za = BankAccount(1, 'Zain', 100)
        self.assertEqual(za.get_balance(), 100)
        za.deposit(200)
        self.assertEqual(za.get_balance(), 300)

    def test_get_balance(self):
        za = BankAccount(1, 'Zain', 100)
        self.assertEqual(za.get_balance(), 100)
        za.withdraw(0)
        self.assertEqual(za.get_balance(), 100)

class BankAccountManager(unittest.TestCase):

    def test_add_account(self):
        za = BankAccountsManager()
        za.add_account(1, 'Zain')
        sa = BankAccount(1, 'Zain')
        self.assertEqual(za.get_account_report(1), "ID: {}\nName: {}\nBalance: ".format(sa.ID, sa.name) +
                         "{0:.2f}".format(sa.balance))

    def test_make_deposit(self):
        za = BankAccountsManager()
        za.add_account(1, 'Zain')
        za.make_deposit(1, 100)
        self.assertEqual(za.get_balance(1), 100)
        with self.assertRaises(Exception):
            za.make_deposit(2, 1)

    def test_make_withdrawl(self):
        za = BankAccountsManager()
        za.add_account(1, 'Zain', 100)
        za.make_withdrawl(1, 100)
        self.assertEqual(za.get_balance(1), 0)
        with self.assertRaises(Exception):
            za.make_withdrawl(2)
            za.make_withdrawl(1)

if __name__ == '__main__':
    unittest.main()

