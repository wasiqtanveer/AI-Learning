number  = int(input("Enter a number: "))

prime = True

if number < 2:
    prime = False

elif number == 2:
    prime = True

else:
    for i in range(2,number):
        if (number % i == 0):
            prime = False
            break

if prime:
    print(number,": Is a prime Number")

else:
    print(number,": Is not a prime Number")