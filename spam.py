text=input("Enter the text: ")

if ("make lot of money" in text):
    spam=True
elif ("buy now" in text):
    spam=True
elif ("click this" in text):
    spam=True
elif ("subcribe this " in text):
    spam=True
else:
    spam=False
    
if(spam):
    print("THIS TEXT IS SPAM")
else:
    print("THIS TEXT IS NOT SPAM")