class c2v:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'
    
class c3v(c2v):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'

v1=c2v(4,5)
v2=c3v(5,6,7)
print(v1)
print(v2)