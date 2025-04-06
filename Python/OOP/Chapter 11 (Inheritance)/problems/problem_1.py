class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class vector_3D(vector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
        
    def __str__(self):
        return f"""
X vector: {self.x}
Y vector: {self.y}  
Z vector: {self.z}
        """    
        
d3 = vector_3D(3,8,5)
print(d3)