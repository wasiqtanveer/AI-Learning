temp = float(input("enter the temperature in Celcius: "))

def convert(temp):
    fahrenheit = (temp*(9/5))+32
    return fahrenheit

print(f"The {temp}° Clecius in Fahrenheight is: {convert(temp)}°")