import unittest

from SemicolonPhase2.bankApp.exceptions.InvalidAccountException import InvalidAccountException
from SemicolonPhase2.bankApp.exceptions.InsufficientFundException import InsufficientFundException
from SemicolonPhase2.bankApp.exceptions.InvalidAmountException import InvalidAmountException
from SemicolonPhase2.bankApp.exceptions.InvalidPinException import InvalidPinException
from bank import Bank


class MyTestCase(unittest.TestCase):
    def test_thatMyBankCanRegisterCustomer(self):
        bank = Bank("Mavericks")
        bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(1, bank.numberOfAccount)

    def test_thatMyBankCanRegisterMoreThanOneCustomer(self):
        bank = Bank("Mavericks")
        self.assertEqual(0, bank.numberOfAccount)

        bank.register("Mr", "Sikiru", 1234)
        bank.register( "Mr", "Chibuzor", 5678)
        bank.register("Mr", "Femi", 9101)
        self.assertEqual(3, bank.numberOfAccount)

    def test_thatMyBankAccountIsZeroIntially(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(0, mavericks.get_balance(1234))

    def test_thatMyBankCanFindAnAccount(self):
        bank = Bank("Mavericks")
        mavericks1 = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(mavericks1, bank.findAccount(1))

    def test_thatMyBankRaiseErrorIfILookForAccountThatDoesNotExist(self):
        bank = Bank("Mavericks")
        mavericks1 = bank.register("Mr", "Sikiru", 1234)
        with self.assertRaises(InvalidAccountException) as error:
            bank.findAccount(2)

    def test_add3AccountCheckTheSecond(self):
        bank = Bank("Mavericks")
        self.assertEqual(0, bank.numberOfAccount)
        mavericks1 = bank.register("Mr", "Sikiru", 1234)
        mavericks2 = bank.register("Mr", "Chibuzor", 5678)
        mavericks3 = bank.register("Mr", "Femi", 9101)
        self.assertEqual(3, bank.numberOfAccount)
        self.assertEqual(mavericks2, bank.findAccount(2))

    def test_thatMyBankCanCheckBalance(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(0, bank.check_balance(1, 1234))

    def test_thatMyBankCanDepositIntoAnAccount(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(0, bank.check_balance(1, 1234))
        mavericks.deposit(2000)
        self.assertEqual(2_000, bank.check_balance(1, 1234))

    def test_thatBankCannotDepositNegativeAmount(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(0, bank.check_balance(1, 1234))
        with self.assertRaises(InvalidAmountException) as error:
            mavericks.deposit(-2000)
        self.assertEqual(0, bank.check_balance(1, 1234))

    def test_thatBankCannotDepositZero(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Mr", "Sikiru", 1234)
        self.assertEqual(0, bank.check_balance(1, 1234))
        with self.assertRaises(InvalidAmountException) as error:
            mavericks.deposit(0)

    def test_thatBankCanWithdraw(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Chibuzor", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        mavericks.deposit(2_000)
        self.assertEqual(2_000, bank.check_balance(1, 4321))
        bank.withdraw(1, 1_000, 4321)
        self.assertEqual(1_000, bank.check_balance(1, 4321))

    def test_ThatMyBankCannotWithdrawWithWrongPin(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Chibuzor", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        mavericks.deposit(2_000)
        self.assertEqual(2_000, bank.check_balance(1, 4321))
        with self.assertRaises(InvalidPinException) as error:
            bank.withdraw(1, 1_000, 3321)
        self.assertEqual(2_000, bank.check_balance(1, 4321))

    def test_ThatMyBankCannotWithdrawNegativeAmount(self):
        bank = Bank("Mavericks")
        mavericks = bank.register("Chibuzor", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        mavericks.deposit(2_000)
        self.assertEqual(2_000, bank.check_balance(1, 4321))
        with self.assertRaises(InvalidAmountException) as error:
            bank.withdraw(1, -1_000, 4321)
        self.assertEqual(2_000, bank.check_balance(1, 4321))

    def test_ThatMyBankCanTransfer(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        self.assertEqual(0, bank.check_balance(2, 4321))
        bank.deposit(1, 5_000)
        bank.deposit(2, 2_000)
        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))
        # bank.transfer(int, int, int, string)
        bank.transfer(1, 2, 1500, 4321)
        self.assertEqual(3_500, bank.check_balance(1, 4321))
        self.assertEqual(3_500, bank.check_balance(2, 4321))

    def test_ThatMyBankCannotTransferWithWrongPin(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        self.assertEqual(0, bank.check_balance(2, 4321))
        bank.deposit(1, 5_000)
        bank.deposit(2, 2_000)
        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))
        with self.assertRaises(InvalidPinException) as error:
            bank.transfer(1, 2, 1500, 1111)

        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))

    def test_ThatMyBankCannotTransferNegativeAmount(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        self.assertEqual(0, bank.check_balance(2, 4321))
        bank.deposit(1, 5_000)
        bank.deposit(2, 2_000)
        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))
        with self.assertRaises(InvalidAmountException) as error:
            bank.transfer(1, 2, -1500, 4321)

        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))

    def test_ThatMyBankCannotTransferToAccountThatDoesNotExist(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(0, bank.check_balance(1, 4321))
        self.assertEqual(0, bank.check_balance(2, 4321))
        bank.deposit(1, 5_000)
        bank.deposit(2, 2_000)
        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))
        with self.assertRaises(ValueError) as error:
            bank.transfer(1, 4, 1500, 4321)

        self.assertEqual(5_000, bank.check_balance(1, 4321))
        self.assertEqual(2_000, bank.check_balance(2, 4321))

    def test_ThatBankCanRemoveAccount(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(2, bank.getNumberOfAccounts())
        bank.remove(1, 4321)
        self.assertEqual(1, bank.getNumberOfAccounts())

    def test_ThatMyBankCannotRemoveAccountThatDoesNotExist(self):
        bank = Bank("Mavericks")
        bank.register("Chibuzor", "Dangote", 4321)
        bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(2, bank.getNumberOfAccounts())
        with self.assertRaises(InvalidAccountException) as error:
            bank.remove(4, 4321)
        self.assertEqual(2, bank.getNumberOfAccounts())


    def test_registerThreeAccountRemoveTheMiddleAccountAndGetAccountNumber(self):
        bank = Bank("Mavericks")
        chibuzor = bank.register("Chibuzor", "Dangote", 4321)
        dayo = bank.register("Dayo", "Dangote", 4321)
        bolaji = bank.register("Bolaji", "Dangote", 4321)
        self.assertEqual(1, chibuzor.number)
        self.assertEqual(2, dayo.number)
        self.assertEqual(3, bolaji.number)
        bank.remove(2, 4321)
        self.assertEqual(1, chibuzor.number)
        self.assertEqual(3, bolaji.number)

    def test_registerThreeAccountRemoveTheMiddleAccountAndGetAccountNumberAndAddAnotherAccount(self):
        bank = Bank("Mavericks")
        chibuzor = bank.register("Chibuzor", "Dangote", 4321)
        dayo = bank.register("Dayo", "Dangote", 4321)
        bolaji = bank.register("Bolaji", "Dangote", 4321)
        self.assertEqual(1, chibuzor.number)
        self.assertEqual(2, dayo.number)
        self.assertEqual(3, bolaji.number)
        bank.remove(2, 4321)
        self.assertEqual(1, chibuzor.number)
        self.assertEqual(3, bolaji.number)
        sultan = bank.register("Dayo", "Dangote", 4321)
        self.assertEqual(4, sultan.number)



    # def test_ThatMyBankCannotRemoveAccountWithWrongPin(self):
    #     bank = Bank("Mavericks")
    #     Bank.register(bank, "Chibuzor", "Dangote", 4321)
    #     Bank.register(bank, "Dayo", "Dangote", 4321)
    #     self.assertEqual(2, bank.getNumberOfAccounts())
    #     with self.assertRaises(InvalidPinException) as error:
    #         bank.remove(1, 1234)
    #     self.assertEqual(2, bank.getNumberOfAccounts())

