with open("poems.txt") as files:
    red = files.read()
    contain = False
    
    if "twinkle" in red:
        contain = True

if contain:
    print("The file contains the word \"twinkle\" ")
    
else:
    print("The file does not contain the word \"twinkle\" ")