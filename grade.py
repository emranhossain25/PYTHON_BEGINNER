marks=int(input("Enter your marks: "))

if marks>=90:
    grade="Ex"
elif marks>=80:
    grade="A"

elif marks>=70:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=50:
    grade="D"
elif marks<50:
    grade="F"

print(grade + " is your grade:")
