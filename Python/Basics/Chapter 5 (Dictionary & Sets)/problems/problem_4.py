langauge = {}

friend_1 = input("Enter name and language only: ")
friend_2 = input("Enter name and language only: ")
friend_3 = input("Enter name and language only: ")
friend_4 = input("Enter name and language only: ")

key_1 , val_1 = friend_1.split()
key_2 , val_2 = friend_2.split()
key_3 , val_3 = friend_3.split()
key_4 , val_4 = friend_4.split()

langauge.update({key_1 : val_1})
langauge.update({key_2 : val_2})
langauge.update({key_3 : val_3})
langauge.update({key_4 : val_4})

print(langauge)