marks=float(input("Enter your marks:"))
if marks>=90 and marks<=100:
    print("GRADE A+")
elif marks>=80 and marks<90:
    print("GRADE A")
elif marks>=70 and marks<80:
    print("GRADE B")
elif marks>=60 and marks<70:
    print("GRADE C")
elif marks>=50 and marks<60:
    print("GRADE D")
else:
    print("FAIL")