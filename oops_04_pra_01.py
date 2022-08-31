class calculater:
    def __init__(self,num):
        self.number=num
    
    def square(self):
        print(f" The Value of {self.number} square is {self.number **2}")
    
    def squreroot(self):
        print(f"The Value of {self.number} squreroot is {self.number ** 0.5}")
    
    def cube(self):
        print(f"The Value of {self.number} cube is {self.number **3}")

cal=calculater(5)
cal.square()
cal.squreroot()
cal.cube()