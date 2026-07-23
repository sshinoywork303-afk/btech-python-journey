import random
account_Number = random.randint(1000, 9999)
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
     balance = deposit_money(balance)
    elif choose == "2" or choose.upper() == "Withdraw" :
     balance = withdraw_money(balance)
    elif choose == "3" or choose.upper() == "Check Balance" :
      check_balance(balance)
    elif choose == "4" or choose.upper() == "Exit" :
      print("Thank You for using python Banking Services :)")
      break