#Input three side lengths. Check whether they can form a triangle.
s1=float(input("Enter the side1 of trangle:"))
s2=float(input("Enter the side2 of trangle:"))
s3=float(input("Enter the side3 of tangle :"))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("It can form Trangle with the help of these sides:")
else:
    print("It can not form Trangle with the help these sides:")