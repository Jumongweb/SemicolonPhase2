import sys
from SemicolonPhase2.bankApp.bank import Bank
from SemicolonPhase2.bankApp.exceptions.InsufficientFundException import InsufficientFundException
from SemicolonPhase2.bankApp.exceptions.InvalidAccountException import InvalidAccountException
from SemicolonPhase2.bankApp.exceptions.InvalidPinException import InvalidPinException

bank = Bank("Hades Bank")


def main_main():
    try:
        print("=" * 40)
        print(f"""
            Welcome To {bank.name}!
            1. Register Account
            2. Deposit
            3. Withdraw
            4. Transfer
            5. CheckBalance
            6. Exit           
        """)
        print("=" * 40)

        response = int(input("Reply: "))
        match response:
            case 1:
                register_account()

            case 2:
                deposit()

            case 3:
                withdraw()

            case 4:
                transfer()

            case 5:
                check_balance()

            case 6:
                print("Goodbye. ")
                print("See you next time")
                sys.exit()

            case _:
                main_main()

    except ValueError as e:
        print("Oga. You can only enter 1 - 7")
        main_main()


def register_account():
    try:
        print("To create account: ")
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        pin = input("Enter pin: ")
        # bank = Bank("Mavericks")
        dee_ = bank.register(first_name, last_name, pin)
        print()
        print(f"Welcome {first_name} {last_name}")
        print(f"Account created successfully. Your account number is >>>>> {dee_.number}")
    except InvalidPinException as e:
        print(e)
    finally:
        main_main()


def deposit():
    print("Deposit: ")
    account_number = int(input("Enter Account Number to deposit into: "))
    amount = int(input("Enter amount to deposit "))
    try:
        bank.deposit(account_number, amount)
        print("Deposit successful")
    except  InsufficientFundException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except InvalidAccountException as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print()
        main_main()


def withdraw():
    print("Withdraw: ")
    amount = int(input("Enter Amount to withdraw: "))
    account_number = int(input("Enter account number: "))
    pin = input("Enter your pin")

    try:
        bank.withdraw(amount, account_number, pin)
        print(f"{amount} withdrawn successfully")
    except InsufficientFundException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except InvalidAccountException as e:
        print(e)
    finally:
        print()
        main_main()


def transfer():
    sender = int(input("Enter your account number "))
    receiver = int(input("Enter account you want to transfer to "))
    amount = int(input("Enter amount to transfer "))
    pin = input("Enter pin ")

    try:
        bank.transfer(sender, receiver, amount, pin)
        print(f"{amount} transferred from {sender} to {receiver}")
    except InvalidPinException as e:
        print(e)
    except InvalidAccountException as e:
        print(e)
    except InsufficientFundException as e:
        print(e)
    finally:
        print()
        main_main()


def check_balance():
    print("Balance: ")
    account_number = int(input("Enter account number: "))
    pin = input("Enter pin: ")

    try:
        balance = bank.check_balance(account_number, pin)
        print(f"You account balance is {balance}")
    except InvalidPinException as e:
        print(e)
    except InvalidAccountException as e:
        print(e)
    except InsufficientFundException as e:
        print(e)
    finally:
        print()
        main_main()


main_main()
