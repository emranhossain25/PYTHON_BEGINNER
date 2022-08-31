from operator import le
from turtle import left


def merge_sort(l,lb,ub):
    if ub-lb >1:
        mid=(lb+ub)//2
        merge_sort(l,lb,mid)
        merge_sort(l,mid,ub)
        merge(l,lb,mid,ub)

def merge(l,lb,mid,ub):
    left=l[lb:mid]
    right=l[mid:ub]
    k=lb
    i=0
    j=0
    while(lb+i < mid and mid+j < ub):
        if(left[i]<=right[j]):
            l[k]=left[i]
            i +=1
        else:
            l[k]=right[j]
            j +=1
        k +=1
        
    if lb+1 < mid:
        while k<ub:
            l[k]=left[i]
            i +=1
            k +=1
    else:
        while k<ub:
            l[k]=right[j]
            j +=1
            k +=1

l1=input("Enter the list element: ").split()
l1=[int(n) for n in l1]
merge_sort(l1,0,len(l1))
print("SORTED LIST: ",end='')
print(l1)