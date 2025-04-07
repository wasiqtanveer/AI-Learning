from numpy import imag


class complex:
    def __init__(self,real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        real_part = self.real*other.real - self.imaginary*other.imaginary
        imaginary_part = self.real*other.imaginary + self.imaginary*other.real
        
        return complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
num1 = complex(2,3)
num2 = complex(4,5)

print(num1+num2)
print(num1*num2)