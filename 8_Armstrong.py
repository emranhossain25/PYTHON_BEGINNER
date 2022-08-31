from unicodedata import digit


lower=int(input("Enter the lower range"))
upper=int(input("Enter the upper range"))
for num in range(lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum +=digit ** 3
        temp //=10
        if num==sum:
            print(num)