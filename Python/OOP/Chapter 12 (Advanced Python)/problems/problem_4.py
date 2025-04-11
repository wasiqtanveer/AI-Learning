try:
    number1 = int(input("Enter the first number : "))
    number2 = int(input("Enter the second number : "))
    
    print(f"{number1/number2}")
    
except ZeroDivisionError as e:
    print("Infinity")