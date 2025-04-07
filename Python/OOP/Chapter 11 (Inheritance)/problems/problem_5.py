class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __mul__(self, other):
        return ((self.x*other.x)+(self.y*other.y)+(self.z*other.z))
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k" 
    
vec = vector(3,4,5)
vec2 = vector(1,2,3)

print("Vector Addition:",vec+vec2)
print("Vector Multiplication:",vec*vec2)

# The above code is a simple implementation of a vector class in Python.