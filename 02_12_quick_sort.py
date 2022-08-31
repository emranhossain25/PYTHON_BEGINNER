def partition(arr,low,high):
    pivot=arr[high]
    i=(low-1)

    for j in range(low, high):
        if arr[j]<=pivot:
            i=i+1
        arr[i],arr[j]=arr[j],arr[i] #swap arr[i] and arr[j]
        
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)

def quick_sort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        partitionindex=partition(arr,low,high)
        quick_sort(arr,low,partitionindex - 1)
        quick_sort(arr, partitionindex + 1,high)

arr=[10,7,8,9,1,5]
print('BEFORE SORTING(UNSORTED ARARY)')
#print(data)
n=len(arr)

quick_sort(arr,0,n-1)
for i in range(n):
    print(arr[i],end=' ')