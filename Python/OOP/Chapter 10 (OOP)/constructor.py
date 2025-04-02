class employee:
    def __init__(self,name,emp_id,age): # dunder method(method that automatically starts)
        self.name = name
        self.emp_id = emp_id
        self.age = age
        
    def __str__(self): #dunder method (method that automatically starts)
        return f"""
    |___________________________________
    |*******Employee  Information*******
    |___________________________________
    | Name        : {self.name}
    | Employee ID : {self.emp_id}
    | Employee Age: {self.age}
    |___________________________________
    """
    
wasiq = employee("wasiq" , 123 , 21)

print(wasiq)