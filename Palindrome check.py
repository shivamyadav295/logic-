#Ask for a word and check whether it reads the same backward, such as level.
num=int(input("enter a number to check palindrome:"))
real=num
rev=0
i=1
while num>0:
    i=num%10
    rev=rev*10+i
    num=num//10
if real==rev:
    print("It is a plindrome number.")
else:
    print ("not a plindrome number.")
