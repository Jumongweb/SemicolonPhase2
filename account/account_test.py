import unittest
from account import Account


class MyTestCase(unittest.TestCase):
    def test_thatAccountIsZero(self):
        Chibuzor_account: Account = Account()
        self.assertEqual(0, Chibuzor_account.get_balance())

    def test_thatIAdd10k_BalanceIs10k(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(10_000)
        self.assertEqual(10_000, Chibuzor_account.get_balance())

    def test_withdrawTwoTimes(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(5_000)
        Chibuzor_account.deposit(5_000)
        self.assertEqual(10_000, Chibuzor_account.get_balance())

    def test_thatAddNegativeNumber_balanceRemainTheSame(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(-10000)
        self.assertEqual(0, Chibuzor_account.get_balance())

    def test_thatBalanceIs20k_AddNegativeNumber_balanceRemainTheSame(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(20_000)
        Chibuzor_account.deposit(-10000)
        self.assertEqual(20_000, Chibuzor_account.get_balance())

    def test_withdrawMoney(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(20_000)
        Chibuzor_account.withdraw(10_000)
        self.assertEqual(10_000, Chibuzor_account.get_balance())

    def test_withdrawMoney_Twice(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(20_000)
        Chibuzor_account.withdraw(10_000)
        Chibuzor_account.withdraw(2_000)
        self.assertEqual(8_000, Chibuzor_account.get_balance())

    def test_withdrawNegativeAmount(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(20_000)
        Chibuzor_account.withdraw(-10_000)
        self.assertEqual(20_000, Chibuzor_account.get_balance())

    def test_thatMyAccountCanNotWithrawnWhenBalanceIsZero(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.withdraw(10_000)
        self.failureException("Balance is zero")

    def test_thatMyAccountCannotAcceptZeroAsDeposit(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(0)
        self.failureException("You cannot deposit zero")

    def test_thatMyAccountCannotWithdrawnMoreThanMyBalance(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.deposit(2_000)
        Chibuzor_account.withdraw(3000)
        self.assertEqual(2000, Chibuzor_account.get_balance())

    def test_thatMyAccountCannotWithdrawnZero(self):
        Chibuzor_account: Account = Account()
        Chibuzor_account.withdraw(0)
        self.failureException("You cannot withdraw zero")

if __name__ == '__main__':
    unittest.main()
