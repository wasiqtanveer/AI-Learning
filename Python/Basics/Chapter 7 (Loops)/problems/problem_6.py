number = int(input("enter a number: "))

for i in range(1,number+1):
    print(" " * (number-i), end="")
    print("*" * (i*2-1), end="")
    print()