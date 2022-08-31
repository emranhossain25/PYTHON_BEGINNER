class Vector:
    def __init__(self,vec):
        self.vec=vec
    
    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 +=f" {i}a{index}"
            index +=1
        return str1[:-1]
    def __add__(self,vec2):
        newlit=[]
        for i in range(len(self.vec)):
            newlit.append(self.vec[i] + vec2.vec[i])
        return Vector(newlit)
    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    def __len__(self):
        return len(self.vec)

v1=Vector([1,4,9])
v2=Vector([1,8,6])
print(v1+v2)
print(v1+ v2)