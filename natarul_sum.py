num=int(input("Enter the number: "))
sum=0
for i in range(1, num+1):
    print(i,end=" ")
    sum=i+sum
print("sum=",sum)