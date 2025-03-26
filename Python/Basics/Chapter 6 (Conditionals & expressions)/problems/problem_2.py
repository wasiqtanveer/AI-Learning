marks_1 = int(input("Enter the marks of 1st subject: "))
marks_2 = int(input("Enter the marks of 2nd subject: "))
marks_3 = int(input("Enter the marks of 3rd subject: "))

total = ((marks_1 + marks_2 + marks_3 ) / 300) * 100

if total >= 40 :
    print("You are pass" , total)

else:
    print("you failed" , total)