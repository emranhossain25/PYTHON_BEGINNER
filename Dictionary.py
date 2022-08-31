from turtle import update


myDict={
    "fast": " IN A QUICK MANNER",
    "Emran": "a coder",
     "marks": {1,3,4},
     "anotherDict": {'emran':'a Engineer'}
}

#methods of dictionary 
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)

updateDict={
    "Emran":"Friend",
    "NURJAHAN":"GF",
    "JASMINE":"FIRST LOVE ",
    "ROCK":"A DANCER"
}

myDict.update(updateDict)
print(myDict)
print(myDict.get("Emran"))
print(myDict["Emran"])
