with open("pyton.txt") as file:
    read = file.read()
    
    if "Python" in read:
        print("yes, its there....")
    else:
        print("nope, its not there....")
        