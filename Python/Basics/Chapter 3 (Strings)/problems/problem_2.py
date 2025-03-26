name = input("your name : ")
date = input("Todays date : ")

# print(f"Dear {name},\nYou are selected!\n{date}")

letter =''' Dear <|Name|>,
    Yor are selected!
    <|Date|>
            '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))