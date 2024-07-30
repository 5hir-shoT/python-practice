#6. Write a program that determines the grade of a student 
#   based on the percentage entered by the user.

marks=int(input("enter marks="))
if(marks>=90):
    print("Grade A")
elif(marks>=70):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
elif(marks>=40):
    print("Grade D")
else:
    print("Grade F")
