#contractor and statict method

from typing_extensions import Self


class Employee():
    company='Google'
    def __init__(self,name,salary,subunit): #constractor
        self.name=name
        self.salary=salary
        self.subunit=subunit
    def getdeatils(self):
        print(f"The name of The employee is {self.name}")
        print(f"The salary of The Employeeis{self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")
    @staticmethod
    def great():
        print("Good Morning: ")

Emran=Employee('EMRAN',100,"You Tube")
Emran.getdeatils()