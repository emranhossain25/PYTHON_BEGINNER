class Train():
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getdetails(self):
        print('*******')
        print(f"The name of train is {self.name}")
        print(f"AVAILBLE TICKET ARE {len(self.seats)}")
        print("*******")
    def bookticket(self):
        if len(self.seats)>0:
            print(f" Congtratulation !Your seats has been booked ")
            self.seats.pop()
        else:
            print("Sorry Seats is not availble try in tatkal: ")
    def cancelticket(self,num):
        self.seats.append(num)
        print("Congratulation! Your seats are cancel successfully")
    def fareInfo(self):
        print(f"The price of ticket is RS {self.fare}")

#name=input("Enter The train name: ")
#fare=int(input("Enter the price of ticket: "))
#seats=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#num=int(input("Enter the ticket number which you want to cancel: "))

#tran=Train(name,fare,seats)
#tran.getdetails()
#tran.fareInfo()
#tran.bookticket()
#tran.cancelticket(num)

train=Train('Rajdhani Express',500,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
train.getdetails()
train.fareInfo()
train.bookticket()
train.cancelticket(10)