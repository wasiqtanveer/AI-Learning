import random

user = input("type \"R\" for rock, \"P\" for paper, \"S\" for scissor: ")

dict = {
    "r": -1,
    "R": -1,
    "p": 0,
    "P": 0,
    "s": 1,
    "S": 1,
}

dict_2 = {
    -1 : "Rock",
     0 : "Paper",
     1 : "Scissor"
}

computer_choice = random.choice([-1,0,1]) # computer choice
user_choice = dict[user] #user choice

print(f"User chose: {dict_2[user_choice]}\nComputer chose: {dict_2[computer_choice]} ")

# game's logic
if ((user_choice == -1 and computer_choice == 1) or (user_choice == 0 and computer_choice == -1) or (user_choice == 1 and computer_choice == 0) ):
    print("👨 User Won 👨")

elif (user_choice == computer_choice  ):
    print("📍 Draw 📍")

else:
    print("🤖 Computer won 🤖")
    