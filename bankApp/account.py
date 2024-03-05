from SemicolonPhase2.bankApp.exceptions.InsufficientFundException import InsufficientFundException
from SemicolonPhase2.bankApp.exceptions.InvalidAmountException import InvalidAmountException
from SemicolonPhase2.bankApp.exceptions.InvalidPinException import InvalidPinException


class Account:
    def __init__(self, name, balance, pin, number):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.number = number

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance
        raise InvalidPinException("Invalid pin")

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            raise InvalidAmountException("Invalid amount")
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount, pin):
        if self.pin != pin:
            raise InvalidPinException("Invalid Pin")
        if withdraw_amount > self.balance:
            raise InsufficientFundException("Insufficient Amount")
        if withdraw_amount <= 0:
            raise InvalidAmountException("Invalid Amount")
        self.balance -= withdraw_amount

    def __str__(self):
        return f"Account name: {self.name}\nAccount number: {self.number}\nAccount balance: {self.balance}"

    # @classmethod
    # def generateAccount():
    #     return
