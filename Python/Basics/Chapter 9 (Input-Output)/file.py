files = open(r"C:\Users\Wasiq Tanveer\Desktop\git.txt") # loads file location to variable files
red = files.read() # reads the file and stores it in red
print(red) # prints the content of the file
files.close() # closes the file