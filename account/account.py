class Account:
    def __init__(self):
        self.balance = 0
    def get_balance(self):
        return self.balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance > withdraw_amount and withdraw_amount > 0:
            self.balance -= withdraw_amount



# class Account:
#     def __init__(self):
#         self.balance = 0
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, deposit_amount):
#         if deposit_amount > 0:
#             self.balance += deposit_amount
#
#     def withdraw(self, withdraw_amount):
#         if self.balance > withdraw_amount and withdraw_amount > 0:
#             self.balance -= withdraw_amount

