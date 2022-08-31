from turtle import circle


def inside (circle_x,circle_y,rad,x,y):
    if ((x-circle_x)*(x-circle_x)+(y-circle_y)*(y-circle_y)<=rad*rad):
        return True
    else:
        return False
circle_x=int(input("Enter circle_x: "))
circle_y=int(input("Enter circle_y: "))
x=int(input("Enter: x"))
y=int(input("Enter: y"))
rad=int(input("Enter radius: "))
if (inside(circle_x,circle_y,rad,x,y)):
    print("inside the circle")
else:
    print("Outside the circle")