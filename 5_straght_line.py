from re import M
from tkinter import N


def straght(x,y,x1,y1,x2,y2):
    M=((y1-y)/(x1-x))
    N=((y2-y)/(y2-y))

    if M==N:
        print("The points are falling in the straght line")
    else:
        print("The points are not falling in the straght line")
straght(2,4,3,5,6,5)