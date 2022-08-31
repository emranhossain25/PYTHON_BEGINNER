class Employee:
    company='google'
    salary=100000
    location='Delhi'

    @classmethod
    def changesalary(clls,sal):
        clls.salary=sal

e=Employee()
print(e.salary)
e.changesalary(20000)
print(e.salary)
print(Employee.salary)