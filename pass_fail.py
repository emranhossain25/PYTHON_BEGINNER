sub1=int(input("Enter sub 1 marks: "))
sub2=int(input("Enter sub 2 marks: "))
sub3=int(input("Enter sub 3 marks: "))

if(sub1<33 and sub2<33 and sub3<33):
    print("You are fail ")
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail due less percentage: ")
else:
    print("Congratulations you have passed: ")