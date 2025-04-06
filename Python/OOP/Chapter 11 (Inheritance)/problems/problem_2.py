class pets:
    def __init__(self,type,age):
        self.type = type
        self.age = age
    
class dog(pets):
    def __init__(self,type,age,breed):
        super().__init__(type,age)
        self.breed = breed
        
    def __str__(self):
        return f"""
TYPE: {self.type}   
AGE: {self.age}
BREED: {self.breed}
        """
        
d = dog("dog",5,"bulldog")
print(d)