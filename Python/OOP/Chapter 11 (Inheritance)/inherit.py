class student:
    def __init__(self,name,std_id,dept):
        self.name = name
        self.std_id = std_id
        self.dept = dept
    
    
class front_bencher(student): # Inheriting from student
    def __init__(self,name,std_id,dept,attnedance):
        super().__init__(name,std_id,dept)
        self.attendance = attnedance
        
    def __str__(self):
        return f"""
    Name:         {self.name}
    ID:           {self.std_id}
    Department:   {self.dept}
    Attendance:   {self.attendance}
    """
    
class back_bencher(front_bencher): # Inheriting from front_bencher
    def __init__(self,name,std_id,dept,attendance,cease_status):
        super().__init__(name,std_id,dept,attendance)
        self.cease_status = cease_status
        
    def __str__(self):
        return super().__str__() + f"Cease Status: {self.cease_status}"

        
    
topper = front_bencher("wasiq" , 123 , "IT" , "90%")
print(topper)

back_b = back_bencher("Ali" , 124 , "IT" , "80%" , "Yes")
print(back_b)