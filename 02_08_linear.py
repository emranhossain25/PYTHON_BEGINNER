from re import search


def linear_search(val,search):
    for i in range(0, len(val)):
        if val[i]==search:
            print(f' {search} is found in {i+1} posstion')
    else:
        print('{search} elenemt is not found ')
    

l=[1,10,20,13,23,45,47,85,96,45]
search=int(input("Enter element which you want search: "))
linear_search(l,search)