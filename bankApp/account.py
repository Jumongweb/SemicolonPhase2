class Account:
    def __init__(self, name, balance, pin, number):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.number = number

    def get_balance(self, pin):
        if self.pin == pin:
            return self.balance
        raise ValueError("Invalid pin")

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount

    def withdraw(self, withdraw_amount, pin):
        if self.pin == pin:
            if self.balance > withdraw_amount > 0:
                self.balance -= withdraw_amount

    @classmethod
    def generateAccount():
        return
