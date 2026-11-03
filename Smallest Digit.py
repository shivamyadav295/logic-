#Smallest Digit — Input a whole number and find its smallest digit.
print("This program will find the smallest digit in a whole number.")
num=int(input("Enter a whole number: "))
smallest=9
while num>0:
    dig=num%10
    if dig<smallest:
        smallest=dig
    num=num//10
print("The smallest digit in the number is :",smallest)

    
