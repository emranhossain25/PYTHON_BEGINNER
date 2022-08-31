#single inheritance and multipli

class Employee:
    company="Google"
    def showdetails(self):
        print("This is Employee: ")

#class programmer(Employee): single
class programmer:
    lauange='python'
     
    def laugage(self):
        print(f" launguage {self.lauange}") # this part is caled single inheritance

class person(Employee,programmer):
    person="men"
    def man(self):
        print(f" person {self.man}")
#e=Employee()
#e.showdetails()
#p=programmer()
#p.showdetails()
#print(p.company)
p=person()
p.showdetails()
print(p.company)\
