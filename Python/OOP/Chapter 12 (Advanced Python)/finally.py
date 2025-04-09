def hello():
    try:
        number =  int(input("Enter a number: "))
        print("Number is: ", number)        
        return 
    
    except ValueError as e:
        print("An exception occurred: ", e)
        
        
    finally:
        print("This block will always execute")
        #even if there is an exception, this block will always execute
        #if there is return in the try block it will still run 
        # which is not the case for simple print()
        # if there is return in the finally block it will run first
        # and then the return in the try block will run
        
hello()