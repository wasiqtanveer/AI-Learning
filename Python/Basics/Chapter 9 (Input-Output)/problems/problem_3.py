with open("donkey.txt", "r+") as files:
    see = files.read()
    if "donkey" in see:
        see = see.replace("donkey" , "######")
         
        files.seek(0)  # moves the cursor to the start of the file
        files.write(see) # writes the new string to the file
        files.truncate() # truncates the rest of the file
         
        
        