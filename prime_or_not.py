num=int(input("Enter the number: "))
prime=True
for i in range(2, num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("Number is prime")
else:
    print("Number is notb prime")