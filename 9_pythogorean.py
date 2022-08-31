from ast import If, Num
from itertools import count


def pythogorean_trplates(num):
    count=0
    for i in range(1,num):
        for j in range(1,num):
            for k in range(1,num):
                if ((i*i + j*j==k*k)and (i<j and j<k)):
                    count+=1
                    print(f"{count} triplets are {i},{j},{k}")
    if count==0:
        print("No Triplets Possible in which {num}")
num=int(input("Enter any number: "))
pythogorean_trplates(num)