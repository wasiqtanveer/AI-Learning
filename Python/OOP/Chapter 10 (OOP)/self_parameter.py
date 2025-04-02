import stat


class students:
    id = ""
    name = ""
    university = "University of Karachi"
    semester = "4th"
    
    def getinfo(self):
        if self.id =="":
            print("Please enter ID")
            return
        elif self.name == "":
            print("Please enter Name")
            return
        else:
            print(f"ID: {self.id}\nName: {self.name}\nUniversity: {self.university}\nSemester: {self.semester}")
    '''      
    if a function isnt using any class attribute then we dont have to use self as it will pass
    the whole object , insstead we use the static method it tells the systme that a function
    dosent use the object in its operation
    '''
    @staticmethod
    def hello():
        print("Hello,students")
            # OR
#             print(f"""
# +----------------------------------+
# |           Student Info           |
# +----------------------------------+
# | ID         : {self.id}
# | Name       : {self.name}
# | University : {self.university}
# | Semester   : {self.semester}
# +----------------------------------+
# """)

students.hello()     
iqbal = students()
iqbal.name = "Iqbal"
iqbal.id = "123"
iqbal.getinfo() # This is how you can call a method of a class by passing an object as an argument
print()
wasiq = students()
wasiq.name = "Wasiq"
wasiq.id = "456"
students.getinfo(wasiq)  # This is how you can call a method of a class by passing an object as an argument

"""
both students.getinfo(wasiq) and wasiq.getinfo() will give the same output, the difference is that in students.getinfo(wasiq) we are passing the object wasiq as an argument to the method getinfo() of the class students, while in wasiq.getinfo() we are calling the method getinfo() of the object wasiq.
"""