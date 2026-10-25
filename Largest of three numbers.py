#  Ask for three numbers and print the largest.


a=float(input("Enter the value of a:" ))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
if a>b and a>c:
    print("a is grater.")
elif b>a and b>c:
    print("b is grater.")
elif c>a and c>b:
    print("c is grater.")
else:
    print("Zero.")