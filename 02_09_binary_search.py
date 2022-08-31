from operator import le
from re import search


#def binary_search(list1,val):
#   low=0
#    high=len(list1)-1
#    mid=0
#    while low<=high:
#        mid=(low+high)//2
#        if list1[mid]<val:
#            low=mid+1
#        elif list1[mid]>val:
#            high=mid-1
#        else:
#            return mid
#    return -1

def binary_search_recursive(list1,low,high,val):
    if high >=low:
        mid=(low+high)//2
        if list1[mid] ==val:
            return mid
        elif list1[mid] > val:
            return binary_search_recursive(list1,low,mid-1,val)
        else:
            return binary_search_recursive(list1,mid+1,high,val)
    return -1  

l=[1,5,6,4,9,6,10,44,55,16]
val=int(input("Enter the element which you want search: "))
s=binary_search_recursive(l,0,len(l)-1,val)

if s !=-1:
    print("Element Is present at index:",str(s))
else:
    print("Element Is not present: ")