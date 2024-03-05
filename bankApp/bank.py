from SemicolonPhase2.bankApp.exceptions.InvalidAccountException import InvalidAccountException
from account import Account


class Bank:
    def __init__(self, name):
        self.numberOfAccount = 0
        self.customerNumber = 0
        self.name = name
        self.accounts = []

    def generate_account_number(self):
        return self.customerNumber

    def register(self, first_name, last_name, pin):
        self.customerNumber += 1
        self.numberOfAccount += 1
        account = Account(first_name + " " + last_name, 0, pin, self.generate_account_number())
        self.accounts.append(account)
        return account

    def findAccount(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
        raise InvalidAccountException("Account not found")


    def check_balance(self, number, pin):
        account: Account = self.findAccount(number)
        return account.get_balance(pin)
        # for account in self.accounts:
        #     if account.number == number:
        #         return account.get_balance(pin)

    def deposit(self, number, amount):
        for account in self.accounts:
            if account.number == number:
                account.deposit(amount)

    def __str__(self):
        return f"Welcome to {self.name} bank"

    def withdraw(self, number, amount, pin):
        account_to_withdraw: Account = self.findAccount(number)
        account_to_withdraw.withdraw(amount,pin)
        # for account in self.accounts:
        #     if account.number == number:
        #         account_to_withdraw = account
        #         account_to_withdraw.withdraw(amount, pin)
        # if account_to_withdraw is None:
        #     raise InvalidAccountException("Account not found")

    def transfer(self, sender, receiver, amount, pin):
        receiver_account = None
        sender_account = None

        for account in self.accounts:
            if account.number == sender:
                sender_account = account
        for account in self.accounts:
            if account.number == receiver:
                receiver_account = account

        if sender_account is not None and receiver_account is not None:
            sender_account.withdraw(amount, pin)
            receiver_account.deposit(amount)
        else:
            raise ValueError(f"Account {receiver_account} does not exist")

    def getNumberOfAccounts(self):
        return len(self.accounts)

    def remove(self, number, pin):
        account_to_remove = None
        for account in self.accounts:
            if account.number == number:
                account_to_remove = account
                self.accounts.remove(account_to_remove)
                self.numberOfAccount -= 1
        if account_to_remove is None:
            raise InvalidAccountException("Invalid Account")

