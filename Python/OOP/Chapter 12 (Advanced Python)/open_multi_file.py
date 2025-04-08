with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    red = f1.read()
    blue = f2.read()
    
print("File 1: \n",red)
print("File 2: \n",blue)