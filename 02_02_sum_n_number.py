from ast import Num


def sum(n):
    if n<10:
        return n
    else:
        return n%10 + sum(n/10)

num=int(input('Enter any number'))

n=sum(num)
print('Sum of digist number=' +str(n))