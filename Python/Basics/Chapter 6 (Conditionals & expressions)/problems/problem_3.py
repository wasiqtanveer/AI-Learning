inp = input("say something: ")

spam_1 = "Make a lot of money"
spam_2 = "subscribe this"
spam_3 = "click this"
spam_4 = "buy now"

spam = {spam_1,spam_2,spam_3,spam_4}

if inp in spam:
    print("scam")

