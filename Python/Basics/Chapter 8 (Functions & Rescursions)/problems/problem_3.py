number = int(input("enter a number: "))

def sum(number):
    if number == 1:
        return 1
    
    else:
        return number + sum(number-1)

print(f"the sum of {number} natural numbers is {sum(number)}")