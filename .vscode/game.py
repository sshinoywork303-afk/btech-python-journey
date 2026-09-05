print("welcome to the number guessing game")
import random
secret = random.randint(1,100)
while True: 
   inpno = int(input("Enter your Number"))
   if inpno == secret:
     print("You Won!")
     break
   elif secret < inpno:
    print("The secret number is less than your number")
   elif secret > inpno:
    print("The secret number is greater than your number")