class number:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
       return self.a + self.b
    def subtrattion(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def isequal(self):
        if (self.a==self.b):
            print("Number is equal: ")
        else:
            print("Number is not Equal: ")
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

num=number(num1,num2)
print(f"Sum={num.sum()}")
print(f"subtraction={num.subtrattion()}")
print(f"Multification={num.multiplication()}")
num.isequal()