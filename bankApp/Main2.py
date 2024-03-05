from SemicolonPhase2.bankApp.bank import Bank
from SemicolonPhase2.bankApp.exceptions import InvalidAmountException, InvalidPinException, InsufficientFundException, InvalidAccountException


class BankApp:
    def __init__(self):
        self.bank = Bank("firstBank")


    def display(self):
        print("=" * 20)
        print("Welcome to Hades")
        print("1.Register account\n2. Deposit \n3. Withdraw \n4. Transfer \n5. Check balance \n6. Close Account "
              "\n7.Exit")
        print("=" * 20)
        reply = int(input("Enter your choice: "))
        try:
            if reply == 1:
                self.register_account()
            elif reply == 2:
                self.deposit()
            elif reply == 3:
                self.withdraw()
            elif reply == 4:
                self.transfer()
            elif reply == 5:
                self.check_balance()
            elif reply == 6:
                self.close_account()
            elif reply == 7:
                self.exit()
            else:
                print("Select between 1 - 7 only")
                self.display()
        except ValueError as e:
            print(e)
            print("Enter number only")
            self.display()
        except KeyboardInterrupt:
            print("Keyboard exit")


    def register_account(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter pin: ")
        account = self.bank.register(first_name, last_name, pin)
        print("Customer register successfully!")
        print("Account Number: ", account.number)
        self.display()

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = input("Enter an amount: ")
        bank = Bank("Hades")
        try:
            self.bank.deposit(int(account_number), int(amount))
            if bank.findAccount(account_number) is None:
                print("Account not found")
            print("Deposit successful!!!")
        except InvalidAccountException as e:
            print(e)
        finally:
            self.display()

    def transfer(self):
        amount = input("Enter amount you want to transfer: ")
        sender_account = input("Enter your account: ")
        receiver_account = input("receiver account number: ")
        pin = input("pin: ")
        try:
            self.bank.transfer(amount, sender_account, receiver_account, pin)
            print("Transfer successfully!!!")
        except InsufficientFundException as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        account = input("Enter your account number: ")
        amount = input("Enter the amount: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(int(account), int(amount), pin)
            print("Amount withdrawn successfully!!!")
        except InvalidAmountException as e:
            print(e)
        finally:
            self.display()

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            balance = self.bank.check_balance(int(account_number), pin)
            print("Your balance is: ", balance)
        except InvalidPinException as e:
            print(e)
            print("Enter a valid pin")
        finally:
            self.display()

    def close_account(self):
        account_number = int(input("Enter the account number: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.remove(account_number, pin)
            print("You account has been close!!!")
        except InvalidPinException as e:
            print(e)
            print("Enter a valid pin")
        except InvalidAccountException as e:
            print(e)
            print("Account does not exist")
        except Exception as e:
            print("Account does not exist")

    def exit(self):
        print("Goodbye!!!")
        return


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()