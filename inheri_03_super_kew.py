class person:
    country="india"
    def __init__(self):
         print("intializig person...")
        
    def takebreath(self):
        print("i am breaththing")
class Employee(person):
    company='OLA'
    def __init__(self):
        super().__init__()
        print("intializing programmer...")
    def getsalaRY(self):
        print(f"salary {self.salary}")
    def takebreath(self):
        print("i am breaththing so im lucky")

class programmer(Employee):
    company='google'
    def __init__(self):
        #super().__init__()
        print("intialling programmer..")
    def salary(self):
        print(f" no salary for you")
    def takebreath(self):
        return super().takebreath()

p=person()
p.takebreath()
p1=programmer()
print(p1.company)