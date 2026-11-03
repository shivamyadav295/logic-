#1. Repeated Digit Check — Input a number and check whether any digit appears more than once.
num=(2,4,3,43,43,54,54,45,45)
key=float(input("enter a number to check for repeated digits:"))
for i in range(len(num)):
    repeat=num.count(key)
    if repeat > 1:
        print("This number has repeated digits.")
    else:
        print("This number does not have repeated digits.")
print("the number of times the digit appears in the number is :",repeat)
