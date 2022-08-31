from datetime import date
from posixpath import split


def int_List(list1):
    for i in range(0,len(list1)):
        list1[i]=int(list1[i])
    return list1

def date_days(date1,date2):
    date1=int_List(date1)
    date2=int_List(date2)

    date1=date(*date1)
    date2=date(*date2)

    print(f"Number of Days = {(date2-date1).days}")

def main():
    date3=tuple(input("Enter The Date in Format YY/MM/DD=").split("/"))
    date4=tuple(input("Enter The Date in Format YY/MM/DD=").split("/"))

    date3=list(date3)
    date4=list(date4)

    date_days(date3,date4)

