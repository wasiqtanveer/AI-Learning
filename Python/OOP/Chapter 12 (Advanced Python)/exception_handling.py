# number = int(input("Enter a number: "))
# print("Number is: ", number) 

try:
    number = int(input("Enter a number: "))

except ValueError as e:
    print("An exception occurred: ", e)
# except Exception as e:
#     print("An exception occurred: ", e) # program won't crash
    # Handle the exception
    
# ================= different exception handlers =======================


# zero division error
try:
    a = 10/0
    
except ZeroDivisionError as e:
    print("An exception occurred: ", e)
    
    
# type error

try:
    # a = "5" + 3
    print(a)
    
except TypeError as e:
    print("An exception occurred: ", e)
    
# ================= finally block =======================
try:
    number = int(input("Enter a number: "))
except ValueError as e:
    print("An exception occurred: ", e)
finally:
    print("This block will always execute")
    
    
