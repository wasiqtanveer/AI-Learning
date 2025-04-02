with open("donkey.txt") as file:
    files = file.read() # reads the file(donkey.txt) and stores it in the variable files

with open("copy_donkey.txt" , "w") as file:
    file.write(files) # writes the content of the file(donkey.txt) to the new file(copy_donkey.txt)