class human:
    age = 21
    height = 5.0
    name = ""
    
    
wasiq = human()
wasiq.name = "Wasiq"
print(wasiq.name,wasiq.age,wasiq.height)



















# This code run fine but The linter might still show warnings because it's 
# being cautious about attribute access, but the code will run correctly. This approach is 
# common in Python, especially when you want to add instance-specific attributes that aren't 
# part of the class definition.
"""
class human:
    age = 21
    height = 5.0
    
    
wasiq = human()
wasiq.name = "Wasiq"
print(wasiq.name,wasiq.age,wasiq.height)
"""



