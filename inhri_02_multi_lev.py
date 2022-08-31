class person:
    country="india"
    def takebreath(self):
        print("i am breaththing")
class Employee(person):
    company='OLA'
    def getsalaRY(self):
        print(f"salary {self.salary}")
    def takebreath(self):
        print("i am breaththing so im lucky")

class programmer(Employee):
    company='google'

    def salary(self):
        print(f" no salary for you")

p=person()
p.takebreath()
p1=programmer()
print(p1.company)