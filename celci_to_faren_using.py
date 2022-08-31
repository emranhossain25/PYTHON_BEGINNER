from types import CellType


def Farenheit(celci):
    return (celci *(9/5)) +32

celci=float(input("Enter the Temparature: "))

f=Farenheit(celci)
print("Farenheit Temparature is: ",str(f))