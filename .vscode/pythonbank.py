import random

account_Number = random.randint(1000, 9999)
transaction_history = []

def ask_pin(pin_number):
    attempts = 3

    while attempts > 0:
        askpin = input("Enter your 4 Digit Pin Number: ").strip()

        if askpin == pin_number:
            return True
        else:
            attempts = attempts - 1
            print(f"Incorrect PIN. {attempts} chances left.")

    if attempts == 0:
        print("Too many incorrect attempts!")
        return False


def create_pin():
    while True:
        pin_number = input("Create a four digit PIN: ").strip()

        if pin_number.isdigit() and len(pin_number) == 4:
            print("Your PIN Number is set.")
            return pin_number
        else:
            print("Enter a valid 4 digit Number!")


def deposit_money(balance):
    while True:
        deposit = input("Enter the amount to be Deposited: ")

        if deposit.isdigit():
            deposit = int(deposit)
            balance = deposit + balance

            transaction_history.append(f"Deposited ₹{deposit}")

            print(f"New Balance: {balance}")
            break
        else:
            print("Enter a Valid Number")

    return balance


def withdraw_money(balance):
    while True:
        withdraw_amm = input("Enter the Amount to be Withdrawn: ")

        if withdraw_amm.isdigit():
            withdraw_amm = int(withdraw_amm)

            if withdraw_amm <= balance:
                balance = balance - withdraw_amm

                transaction_history.append(f"Withdrawn ₹{withdraw_amm}")

                print(f"New Balance: {balance}")
                break
            else:
                print("Insufficient Balance!")
                break
        else:
            print("Enter a Valid Number!")

    return balance


def check_balance(balance):
    print(f"Balance: {balance}")

pin_number = create_pin()


while True:
    name = input("What is your Name? ")

    if name.isalpha():
        break
    else:
        print("Enter a valid Name!")


while True:
    balance = input("Enter Your Starting Balance: ")

    if balance.isdigit():
        balance = int(balance)
        break
    else:
        print("Please Enter a Valid Balance!")


print("----------------------")
print(f"Account Number: {account_Number}")
print(f"Name: {name}")
print(f"Balance: {balance}")
print("----------------------")

while True:
    print("========== Python Bank ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("5. Transaction History")
    print("6. Transfer Money")

    choose = input("Enter your choice: ").strip()

    if choose == "1" or choose.upper() == "DEPOSIT":
        if ask_pin(pin_number):
            balance = deposit_money(balance)

    elif choose == "2" or choose.upper() == "WITHDRAW":
        if ask_pin(pin_number):
            balance = withdraw_money(balance)

    elif choose == "3" or choose.upper() == "CHECK BALANCE":
        if ask_pin(pin_number):
            check_balance(balance)

    elif choose == "4" or choose.upper() == "EXIT":
        print("Thank You for using Python Banking Services :)")
        break

    elif choose == "5" or choose.upper() == "TRANSACTION HISTORY":
        for transaction in transaction_history:
         print(transaction)

    elif choose == "6" or choose.upper() == "TRANSFER MONEY":
            Transfer_Money()
            break
    else:
        print("Invalid Choice!")