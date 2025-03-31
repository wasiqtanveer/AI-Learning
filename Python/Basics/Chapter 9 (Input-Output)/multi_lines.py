


files = open("name.txt")#no need to mention the "r" for read mode as it is default

# lines = files.readlines() # reads the file and stores it in lines
# print(lines,type(lines)) # prints the content of the file, return a list(Array) of lines
#can only use readline() or readlines() one at a time

# ==================printing lines seperately===========================

# line1 = files.readline()
# print(line1,end="")
# line2 = files.readline()
# print(line2, end="")
# line3 = files.readline()
# print(line3, end="")
# line4 = files.readline()
# print(line4, end="")


# for looping through al the lines in a file
# for i in files:
#     print(i,end="")
# ===================== OR ========================
line = files.readline()
while (line != ""):
    print(line,end="")
    line = files.readline()
