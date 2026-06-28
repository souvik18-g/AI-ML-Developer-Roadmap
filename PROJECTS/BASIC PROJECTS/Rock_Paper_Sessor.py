import random
def play():
    user= input("what is your choice? 'r' for rock,'p' for paper,'s' for scissors :")
    computer= random.choice(["r,p,s"])

    if user==computer:
        return "oops tie"
    if is_win(user,computer):
        return "congrats! you won"
    return " oops! you lost"
def is_win(user,computer):
    if (user=='r' and computer=='s') or (user=='p' and computer=='r') or (user=='s' and computer=='p'):
        return True
    
print(play())    