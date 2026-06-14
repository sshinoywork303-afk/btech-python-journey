print ("Welcome to Adult Age Calculator")
while True:
    Name =input("what is your name?")
    if Name.isalpha():
       break
    else: print("invalid Name! Use letters only")
while True:
    age =input("How old are you?")
    if age.isdigit():
     age = int(age)
     break
    else: print("invavlid age! Use numbers")
if age >= 18:
       print(f"hello {Name} , You are {age} years old.")
else: print("You are Not adult!" )