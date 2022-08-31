class Employee:
    company='Bharat Gas'
    salary=5000
    salarybonous=500
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybonous
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonous=val-self.salary

e=Employee()
print(e.salary)
e.totalsalary=5500
print(e.salary)
print(e.salarybonous)