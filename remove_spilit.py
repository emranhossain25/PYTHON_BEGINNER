import this


def remove_and_spilit(string ,word):
    newStr=string.replace(word,"")
    return newStr.strip()

This="  Emran is good   "
n=remove_and_spilit(This,"good")
print(n) 