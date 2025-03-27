def greatest(a,b,c):
    if a > b and a > c:
        return "A is the greatest"

    elif b > a and b > c:
        return "B is the greatest"

    else: 
        return "C is the greatest"


a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

print(greatest(a,b,c))