def average():                                    # function definition
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    
    avg = (a+b+c)/3
    print(avg)


# fucntion with an argument
def goodday(name):
    # name = input("what is your name: ")
    print(f"goodday, {name}")
    

#  function with default argument
def arg(name = "wasiq"): # if i provide argument than use the one i provided else will use (Wasiq)
    print(name)




#=================== function call =======================
# average() 
# goodday("wasiq")
# goodday("faiq")
goodday("haziq")
arg()