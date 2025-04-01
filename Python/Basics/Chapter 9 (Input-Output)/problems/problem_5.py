from os import read
import random

def game():
    score = random.randint(1,100)
    
    with open("highscore.txt") as result:
        highscore = result.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"Your score is {score}")
    
    if score > highscore:
        with open("highscore.txt" , "w") as result:
            result.write(str(score))
    
            
game()