from re import L


line_number = 1
with open("p.txt") as lines:
    line = lines.readline()
    
    while line != "":
        if "Python" in line:
            print(f"Python in line {line_number}")
        else:
            print(f"line {line_number} doesnt contain python")
        
        line_number = line_number+1
        line = lines.readline()