# wont use import OS, instead we will copy the file content delete the file and make the new
# file with the same content
# can delete the file manually or using the OS module
import os



with open("old.txt") as file:
    files = file.read()
    
with open("renamed_by_python.txt", "w") as file:
    file.write(files)

os.remove("old.txt")