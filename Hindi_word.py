from webbrowser import get


hindi={
    "dadda":"Tifin",
    "payer":"Love",
    "shadhi":"maarriage",
    "vastu":"Items"
}

print("Operation are: ",hindi.keys())

a=input("Enter Hindi word")

print("The meaning of your word is",hindi.get(a))