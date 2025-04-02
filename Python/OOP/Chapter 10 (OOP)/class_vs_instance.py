class students:
    id = ""
    name = ""
    university = "University of Karachi"
    semester = "4th"
    
iqbal = students()
iqbal.id = "123"
iqbal.name = "Iqbal"
iqbal.university = "University of Punjab" # instance attribute will take precedense over class attribute
print(f"ID: {iqbal.id}\nName: {iqbal.name}\nUniversity: {iqbal.university}\nSemester: {iqbal.semester}")