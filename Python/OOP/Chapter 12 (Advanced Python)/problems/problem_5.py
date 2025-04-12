table = int(input("Enter a number : "))

list2 = [(i*table) for i in range(1,11)]

with open("tables.txt","w") as table: 
    for i in list2: 
        table.write(f"{str(i)}") 