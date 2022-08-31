from ast import Num


#def factorial_iter(n):
#     fact=1
#    for i in range(n):
#        fact=fact * (i+1)
#    return fact

#num=int(input("Enter any number: "))
#n=factorial_iter(num)
#print(n)

def factorial_recurive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recurive(n-1)

num=int(input("Enter any number: "))
f=factorial_recurive(num)
 
print(f)