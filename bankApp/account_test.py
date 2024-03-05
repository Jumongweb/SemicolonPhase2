import unittest

from SemicolonPhase2.bankApp.exceptions.InvalidAmountException import InvalidAmountException
from SemicolonPhase2.bankApp.exceptions.InvalidPinException import InvalidPinException
from SemicolonPhase2.bankApp.exceptions.InsufficientFundException import InsufficientFundException
from account import Account


class MyTestCase(unittest.TestCase):
    def test_thatAccountIsZero(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.balance)

    def test_thatAccountCanAcceptDeposit(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))

    def test_thatAccountCanAcceptDepositTwice(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        account.deposit(5_000)
        self.assertEqual(15_000, account.get_balance(1234))

    def test_thatAccountCannotAcceptNegativeAmount(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        with self.assertRaises(InvalidAmountException) as error:
            account.deposit(-10_000)
        self.assertEqual(0, account.get_balance(1234))

    def test_thatICanCheckMyBalanceWithCorrectPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        self.assertEqual(10_000, account.get_balance(1234))

    def test_thatICannotCheckMyBalanceWithInCorrectPin(self):
        account = Account("Lawal", 0, 1234, 10001)
        with self.assertRaises(InvalidPinException) as error:
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
        with self.assertRaises(InvalidPinException) as error:
            account.withdraw(1000, 419)
        self.assertEqual(10_000, account.get_balance(1234))

    def test_withdrawTwoTimes(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(10_000)
        account.withdraw(2_000, 1234)
        account.withdraw(1_000, 1234)
        self.assertEqual(7_000, account.get_balance(1234))

    def test_withdrawNegativeNumber_balanceRemainTheSame(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        with self.assertRaises(InvalidAmountException) as error:
            account.deposit(-10_000)
        self.assertEqual(0, account.get_balance(1234))

    def test_thatBankThrowExceptionTwiceIfITryNegativeAmountTwice(self):
        account = Account("Lawal", 0,1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        account.deposit(20_000)
        with self.assertRaises(InvalidAmountException) as error:
            account.deposit(-10_000)

        with self.assertRaises(InvalidAmountException) as error:
            account.deposit(-10_000)
        self.assertEqual(20_000, account.get_balance(1234))

    def test_thatMyAccountCanNotWithrawnWhenAmountIsGreaterThanBalance(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        with self.assertRaises(InsufficientFundException) as error:
            account.withdraw(10_000, 1234)


    def test_thatMyAccountCannotAcceptZeroAsDeposit(self):
        account = Account("Lawal", 0, 1234, 10001)
        self.assertEqual(0, account.get_balance(1234))
        with self.assertRaises(InvalidAmountException) as error:
            account.deposit(0)


if __name__ == '__main__':
    unittest.main()
