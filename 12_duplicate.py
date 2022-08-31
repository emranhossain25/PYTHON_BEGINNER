from msilib.schema import DuplicateFile


def remove(duplicate):
    Final_List=[]
    for no in duplicate:
        if no not in Final_List:
            Final_List.append(no)
    return Final_List

duplicate=[2,4,10,20,5,2,20,4,12,25,2,4,7,23]
print(remove(duplicate))