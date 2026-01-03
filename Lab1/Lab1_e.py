#Wap to input marks in 5 subjects and then calculate total marks,percentage,division and result(pass/fail)

marks1=float(input("Enter marks for Subject 1:"))
marks2=float(input("Enter marks for Subject 2:"))
marks3=float(input("Enter marks for Subject 3:"))
marks4=float(input("Enter marks for Subject 4:"))
marks5=float(input("Enter marks for Subject 5:"))

total=marks1+marks2+marks3+marks4+marks5

percentage = (total / 500) * 100
if marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33 and marks5 >= 33:
    result = "Pass"

    if percentage >=60:
        division ="First Division"
    elif percentage >=50:
        division ="Second Division"
    else:
        division ="Third Division"
else:
    result ="Fail"
    division ="No Division"


print("Total Marks:",total)
print("Percentage:",percentage)
print("Result:",result)
print("Division:",division)


