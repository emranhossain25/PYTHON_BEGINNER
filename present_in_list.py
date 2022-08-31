from tkinter.font import names
from unicodedata import name


names=[' emran ', 'ruhul', 'amit', 'abdur', 'asif', 'aziz', 'mijanur']
name=input("Enter the name to check\n")

if name in names:
    print("THE NAME PRESENT IN LIST: ")
else:
    print("The name is not present in list: ")