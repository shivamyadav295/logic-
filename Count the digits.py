#Ask for a whole number and count how many digits it has.
num=int(input("Enter a whole number:"))
real=num
i=0
if num<0:
    num=-num
while num >0:
    if num == 0:
        i=0
    else:
        num=num//10
    i=i+1

   
print(i)




