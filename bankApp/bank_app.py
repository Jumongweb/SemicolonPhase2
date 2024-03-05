from SemicolonPhase2.bankApp.bank import Bank
from SemicolonPhase2.bankApp.exceptions.InvalidAccountException import InvalidAccountException


class BankApp:
    def __init__(self):
        self.bank = Bank("Mavaricks")

    def main_menu(self):
        print("Welcome to Mavericks Bank ")
        print("Log in or Create Account")
        print("1. Already an account")
        print("2. Sign in")

        try:
            response = int(input("Reply: "))
            bank = Bank("Mavericks")

            if response == 1:
                first_name = input("Enter first_name: ")
                last_name = input("Enter last_name: ")
                pin = input("Enter pin: ")
                self.display()
            elif response == 2:
                self.display()
            else:
                print("You are to select 1 or 2")
                self.display()
        except ValueError:
            print("Enter number only")
            self.display()

    def display(self):
        try:
            print("Welcome to Mavericks Bank ")
            print("What would you like to do: ")
            print("1. Register account ")
            print("2. Deposit ")
            print("3. Withdraw ")
            print("4. Transfer ")
            print("5. Check Balance ")
            print("6. Close account ")
            print("7. Exit ")
            print()
            response = int(input("Enter reply: "))
            match response:
                case 1:
                    self.register_account()
                    self.display()
                case 5:
                    self.check_balance()
                    self.display()
                case 7:
                    exit()
                case _:
                    self.display()

        except ValueError:
            print("Choose only from 1 - 7")
        except KeyboardInterrupt:
            print("Keyboard escape")

    def register_account(self):
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        pin = input("Enter pin: ")
        bank = Bank("Mavericks")
        dayo = bank.register(first_name, last_name, pin)
        print(f"Account created successfully. Your account number is >>>>> {dayo.number}")

    def deposit(self):
        print("test")

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            balance = self.bank.check_balance(int(account_number), pin)
            print("Your balance is:", balance)
        except InvalidAccountException as e:
            print(e)
            self.display()

    # try:
    #     account_number = int(input("Enter account number: "))
    #     pin = input("Enter pin: ")
    #     bank = Bank("Mavericks")
    #     print(type(account_number))
    #     balance = bank.check_balance(account_number, pin)
    #     print(balance)
    # except InvalidAccountException:
    #     print("Account does not exist")
    #     display()

    def exit(self):
        print("Goodbye!!!")


# display()
if __name__ == '__main__':
    bank_app = BankApp()
    bank_app.main_menu()
