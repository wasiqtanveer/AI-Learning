number = int(input("Enter a number: "))
if (n := 5*number ) > 20:
    print(f"Number is {n}")
else:
    print("Number is less than or equal to 20")
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can be useful for simplifying code and reducing redundancy.
# In this example, the walrus operator is used to assign the value of 5*number to the variable n
# and then check if n is greater than 20 in a single line.
# This can make the code more concise and easier to read.
# The walrus operator is especially useful in situations where you want to use a value multiple times
