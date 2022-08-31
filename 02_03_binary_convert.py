from ast import Num


def inte_binary(n):
    if not (n>0):
       return 0
    return (n%2) + inte_binary(n//2)*10

num=int(input('Enter any number: '))

n=inte_binary(num)
print('Binary number=', +n)
#print(n)