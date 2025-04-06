from multiprocessing import Value


class Employee:
    def __init__(self, name, id_number,salary,increment):
        self.name = name
        self.id_number = id_number
        self.salary = salary
        self.increment = increment
        
    @property
    def salaryINCREMENT(self):
        return (self.salary+(self.salary * self.increment/100))
    
    @salaryINCREMENT.setter
    def salaryINCREMENT(self, value):
        self.increment = value
        
    def __str__(self):
        return f"""
Name:            {self.name}
ID:              {self.id_number}
Salary:          {self.salary}
Increment:       {self.increment}%
After Increment: {self.salaryINCREMENT}
    """

wasiq = Employee("Wasiq", 123, 1000, 300)
print(wasiq)