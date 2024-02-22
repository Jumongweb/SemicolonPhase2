import unittest
from account import Account


class MyTestCase(unittest.TestCase):
    def test_thatAccountIsZero(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.balance)

    def test_thatICanCheckMyBalanceWithCorrectPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))

    def test_thatICannotCheckMyBalanceWithInCorrectPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        with self.assertRaises(ValueError) as error:
            account.get_balance(12345)

    def test_thatIAdd10k_BalanceIs10k_withCorrectPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))

    def test_thatMyAccountCanWithdraw(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))
        account.withdraw(1000, 1234)
        self.assertEqual(9_000, account.get_balance(1234))

    def test_thatMyAccountCannotWithdrawWithWrongPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))
        with self.assertRaises(ValueError) as error:
            account.withdraw(1000, 419)
        self.assertEqual(10_000, account.get_balance(1234))
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
