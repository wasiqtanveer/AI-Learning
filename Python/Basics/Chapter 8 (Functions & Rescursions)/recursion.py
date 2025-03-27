def factorial(number):
    if (number == 1  or number == 0):
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Enter a number to find factorial of: "))
print(f"The factoial of {number} is: {factorial(number)}")