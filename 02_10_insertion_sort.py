def insertion_sort(l):
    for i in range(1, len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j -=1
        l[j+1]=key

l=[11,1,2,8,78,56,9,85,45]

insertion_sort(l)
print('Sorted Arrray is: ')
for i in range(len(l)):
     print(i)
    #print("%d" %l[i]) 