import Lst

old = Lst.lists
new = []


for items in old:
    if items == "donkey":
        new.append("######")
    else:
        new.append(items)
        

with open("Lst.py" , "r+") as file:
    array  = file.read()

    new_list = array.replace(str(old), str(new))
    
    # Rewind the file pointer to the beginning of the file
    file.seek(0)
    
    # Write the modified content back to the file
    file.write(new_list)
    
    # Truncate the remaining content if the new content is shorter
    file.truncate()