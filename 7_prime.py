
#num=int(input("Enter any number"))
#for j in range(1,num+1):
#    count=0
#for i in range(1,j+1):
 #       if j%i==0:
 #          count+=1
#if count==2:
 #   print(i)

lower=0
upper=300
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)