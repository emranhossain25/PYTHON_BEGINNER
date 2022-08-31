
from ast import If
from pickle import NONE
from random import randint, random


randomNumber=random.randint(1, 100)
userGueess=NONE
countNoOfguesess=0

while(userGueess!=randomNumber):
    userGueess=int(input("Enter Your guesess! "))
    countNoOfguesess +=1
    if(userGueess==randomNumber):
        print("Yes! Guess it right!....")
    else:
        if(userGueess>randomNumber):
            print("You guess it Wrong! enter a smaller number! ")
        else:
            print("You guess it Wrong!Enter larger number!...")
print(f"You guess it right{countNoOfguesess} attemp....")