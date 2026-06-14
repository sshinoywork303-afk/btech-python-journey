num = input("enter a number")
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
     print("Even Number")
    else: print("Odd Number")
else:print("Enter a Valid Number")