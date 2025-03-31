for j in range(2,21):
    files = open(fr"tables\table_{j}", "w") # opens the file in write mode
    for i in range(1,11):
        
        files.write(f"{j} x {i} = {j*i}\n")

files.close() # closes the file