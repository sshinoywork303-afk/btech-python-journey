while True:
 import random
 student_id = random.randint(1000, 9999)
 while True:
  Name = input("What is your Name?")
  if Name.isalpha():
    print(f"Welcome {Name}!")
    break
  else:
    print("Enter a valid Name")
 while True:
  Marks = (input("Enter Your Total Marks"))
  if Marks.isdigit():
    Marks = int(Marks)
    if 0 <= Marks <= 100:
     break
    else: 
     print("Enter a valid Mark!")
  else:
    print("Enter a valid Mark!")
 if Marks >= 90:
  print("A grade")
  grade = ("A")
 elif Marks >=80:
  print("B grade")
  grade = ("B")
 elif Marks >=70:
  print("C grade")
  grade = ("C")
 elif Marks >=50:
  print("D grade")
  grade = ("D")
 else:
  print("F grade. You failed.")
  grade = ("F")
 print("---------------------------")
 print(f"Student id : {student_id}")
 print(f"Student Name : {Name}")
 print(f"Total Marks : {Marks}")
 print(f"Grade : {grade}")
 print("________________________")
 again = (input("Do you want to input another Student(yes/no)"))
 if again == "no":
  break
