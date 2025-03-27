number = int(input("Enter a number: "))

def table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")
    

table(number)