
from random import randint, random

import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp Turn: Snake(s) Water(w) Gun(g) ?")
randIN=random.randint(1, 3)
if randIN==1:
    comp='s'
elif randIN==2:
    comp='w'
elif randIN==3:
    comp='g'

you=input("Your Turn: Snake(s) Water(w) Gun(g) ?")
a=gameWin(comp,you)

print(f"COMPUTAR CHOSE {comp}")
print(f"YOU CHOSE {you}")

if a==None:
    print("The Game is Tie")
elif a:
    print("Congratulation ! You Win")
else:
    print("computar Win! ")