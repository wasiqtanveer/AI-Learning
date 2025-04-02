with open("donkey.txt") as file:
    files  = file.read()

with open("copy_donkey.txt",) as file:
    files_2 = file.read()
    
    if files == files_2:
        print("Both files have the same content")
    else:    
        print("Both files have different content")