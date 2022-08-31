#(a+bi)(c+di)=(ac-bd) + (ad+bc)i

class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex(self.real + c.real ,self.imaginary + c.imaginary)
    def __mul__(self,c):
        mulreal=self.real*c.real - self.imaginary*c.imaginary
        mulimag=self.real*c.imaginary + self.imaginary*c.real
        return complex(mulreal,mulimag)
    def __str__(self):
            if self.imaginary<0:
                return f'{self.real} - {-self.imaginary}'
            else:
                return f'{self.real} + {self.imaginary}'

c1=complex(1,-4)
c2=complex(331,-37)
print(c1+c2)
print(c1*c2)
