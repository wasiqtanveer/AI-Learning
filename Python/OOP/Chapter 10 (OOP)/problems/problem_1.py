""""
Problem 1: Create a class calculator with the following methods:
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
"""
class calculator:
    def __init__(self,number):
        self.number = number
        
    def square(self):
        square = pow(self.number, 2)
        # return f"Square of {self.number} is {square}" , square
        return square
    
    def cube(self):
        cube = pow(self.number, 3)            
        # return f"Cube of {self.number} is {cube}" , cube
        return cube
    
    def under_root(self):
        root = pow(self.number, 0.5)
        # return f"Square root of {self.number} is {root}", root
        return root
    
    def __str__(self):
        return f"""
Square    : {self.square()}
Cube      : {self.cube()}
Under Root: {self.under_root()}
"""

number1 = calculator(16)
print(number1)  
print()