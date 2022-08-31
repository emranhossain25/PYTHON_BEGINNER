def check_duplicate(n):
    dup=list()
    for i in n:
        if i in dup:
            return True
        dup.append(i)
    return False

list1=[12,45,78,32]
list2=[12,45,78,32,32,41]

print(check_duplicate(list1))
print(check_duplicate(list2))