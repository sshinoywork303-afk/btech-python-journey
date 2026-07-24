import random
account_Number = random.randint(1000, 9999)
def ask_pin(pin_number):
  attempts = 3
  while attempts > 0:
    askpin = input("Enter your 4 Digit Pin Number:").strip()
    if askpin == pin_number :
       return True
    else:
      attempts = attempts - 1
      print(f"Incorrect PIN. {attempts} chances left.")
  if attempts == 0:
    print("Too many incorrect attempts!")
    return False 
def create_pin():
  while True:
      pin_number = input("create a four digit pin :").strip()
      if pin_number.isdigit() and len(pin_number) == 4:
        print("Your pin Number is set.")
        return pin_number
      else:
        print("Enter a valid Number!")
def deposit_money(balance):
      while True:
       deposit = input("Enter the amount to be Deposited :")
       if deposit.isdigit():
         deposit = int(deposit)
         balance = deposit + balance
         balance =int(balance)
         print(f"New Balance: {balance}")
         break
       else :
         print ("Enter a Valid Number")
      return balance
def withdraw_money(balance):
 while True :
       withdraw_amm = input("Enter the Amount to be Withdrawed :")
       if withdraw_amm.isdigit():
         withdraw_amm = int(withdraw_amm)
         if withdraw_amm <= balance:
          balance = balance - withdraw_amm
          print(f"New Balance: {balance}")
         else:
          print("Insufficient Balance!")
          break
       else:
         print("Enter a Valid Number!")
       return balance
def check_balance(balance):
  print(f"Balance :{balance}")
while True :
  pin_number = create_pin()
  name = input("what is your Name?")
  if name.isalpha():
      break
  else :
      print("Enter a valid Name!")
while True:
  balance = input("Enter Your Starting Balance")
  if balance.isdigit():
      balance = int(balance)
      break
  else:
   print("please Enter a Valid balance!")
print("----------------------")
print(f"Account Number : {account_Number}")
print(f"Name : {name}")
print(f"Balance : {balance}")
print("----------------------")
while True:
    print("========== Python Bank ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choose = input("Enter your choice: ").strip()
    if choose == "1" or choose.upper() == "Deposit":
     if ask_pin(pin_number):
       balance = deposit_money(balance)
    elif choose == "2" or choose.upper() == "Withdraw" :
     if ask_pin(pin_number):
       balance = withdraw_money(balance)
    elif choose == "3" or choose.upper() == "Check Balance" :
      if ask_pin(pin_number):
       check_balance(balance)
    elif choose == "4" or choose.upper() == "Exit" :
      print("Thank You for using python Banking Services :)")
      break