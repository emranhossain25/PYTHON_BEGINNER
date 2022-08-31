x=float(input("Enter the first number"))
y=float(input("Enter the second number"))
z=float(input("Enter the third number"))

min=0
if x<y and x<z:
   min=x
if y<x and y<z:
    min=y
if z<x and z<y:
    min=z

print(min," is the smallest number ")
