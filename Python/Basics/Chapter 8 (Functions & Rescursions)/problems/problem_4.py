number = int(input("Enter a number: "))

def triangle(number):
    for i in range(number+1):
        print("* "* (number-i) , end="")
        print()

triangle(number)