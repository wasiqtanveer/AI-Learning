class calculator:

    @staticmethod   
    def square(num1):
        return f"Square of {num1} is {pow(num1, 2)}"
    
    @staticmethod   
    def cube(num1):
        return f"Cube of {num1} is {pow(num1, 3)}"
    
    @staticmethod   
    def under_root(num1):
        return f"Square root of {num1} is {pow(num1, 0.5)}"
        

print("Printed using object name")
number = calculator()
print(number.square(5))
print(number.cube(2))
print(number.under_root(16)," \n")

# ============= OR ===========
print("Did using class name instead of object name")
print(calculator.square(5))
print(calculator.cube(2))
print(calculator.under_root(16))  