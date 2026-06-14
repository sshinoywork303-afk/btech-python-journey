print("Enter the marks obtained in the exam")
Maths = int(input("Maths"))
physics = int(input("physics"))
Chemistry = int(input("Chemistry"))
second_lang = int(input("second language"))
computer_science = int(input("computer science"))
English = int(input("English"))
total_marks = Maths + physics + Chemistry + second_lang + computer_science + English
avg_t = total_marks/6
print("Total Mark :",total_marks)
print(f"Average marks:{avg_t}")
if avg_t >= 90:
 print("A grade")
elif avg_t >=80:
 print("B grade")
elif avg_t >=70:
 print("C grade")
elif avg_t >=60:
 print("D grade")
else:
 print("F grade")