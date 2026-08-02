import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hi_score.txt") as f:
        hi_score = f.read()# here we are reading the hiscore from the file and storing it in a variable hi_score.
         #If the file is empty then we will set the hi_score to 0.
        if(hi_score!=""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    print(f"Your score: {score}")
    if(score>hi_score):
        # write this hiscore to the file
        with open("hi_score.txt", "w") as f:
            f.write(str(score))

    return score

game()