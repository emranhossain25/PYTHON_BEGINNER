from tkinter import N


def sum_recursive(n):
    if n<=1:
        return n
    return n + sum_recursive(n-1)

num=int(input("Enter any number: "))

sum=sum_recursive(num)
print(sum)