from hmac import new
import random

random_number = random.randint(1,100) # 100 is the inclusive
tries = 0

with open("highscore.txt") as result:
    highscore = result.read()
    if highscore != "":
        highscore = int(highscore)
        
    else:
        highscore = 1000

print(f"Current Highscore: {highscore}")
def check(random_number, tries):
    while True:
        user = int((input("Guess the number : ")))
        tries += 1
        if user < 1 or user > 100:
            print("Please guess a number between 1 and 100")
            continue
        
        if user == random_number:
            print("You guessed it right")
            break
        
        elif abs(user-random_number) < 5:
            print("You are very close")
            if (user-random_number) > 0:
                print("Guess lower ")
            else:
                print("Guess higher ")
        
        else:
            print("You are far off")
            if (user-random_number) > 0:
                print("Guess lower ")
            else:
                print("Guess higher ")
    return tries


def high(highscore,tries):
    if tries < highscore:
        highscore = tries
        print(f"New highscore  : {highscore}")
    else:
        print(f"Highscore : {highscore}")
    return highscore

tries = (check(random_number, tries))
new_highscore = high(highscore, tries)

if new_highscore != highscore:
    with open("highscore.txt", "w") as result:
        result.write(str(new_highscore))


print(f"Guessed in   : {tries} tries")

