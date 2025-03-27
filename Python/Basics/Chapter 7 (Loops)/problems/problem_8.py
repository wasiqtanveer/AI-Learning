number = int(input("enter a number: "))

for i in range(1,number+1):
    if (i==1 or i == (number)):
        print("* " * (number))
    else:
        print("* " * 1,end="")
        print("  " * (number-2),end="")
        print("* " * 1,end="")
        print()
