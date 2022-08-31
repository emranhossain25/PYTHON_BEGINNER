from tkinter import N


def sum_natural(n):
    if n<=1:
        return n
    return n + sum_natural(n-1)

num=int(input('Enter any number: '))

n=sum_natural(num)
print('sum_of_natual_number=' +str(n))