from itertools import count
from lib2to3.pgen2.token import OP
from pickle import NONE
import random

randomNumber=random.randint(1, 100)
userGueess=NONE
countNoOfguesess=0

while(userGueess!=randomNumber):
    userGueess=int(input("Enter your Guesess: "))
    countNoOfguesess +=1

    if (userGueess==randomNumber):
        print("Congtratulation! You guess it right")
    else:
        if (userGueess>randomNumber):
            print("Yo guesess it Wrong! Enter a Smaller Number: ") 
        else:
            print("You Guesess it Wrong! Enter a larger Number: ")    

print(f"YOU GUESSES RIGHT IN {countNoOfguesess} attemp")

with open('highscore_pro.txt', 'r') as f:
    highscore_pro=int(f.read())
if (countNoOfguesess<highscore_pro):
    with open('highscore_pro.txt','w') as f:
        f.write(str(countNoOfguesess))