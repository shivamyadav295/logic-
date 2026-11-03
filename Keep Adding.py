#keep adding - keep asking for numbers until the user enter 0, then pront their total.
total=0
while True:
    num=float(input("enter a number:"))
    if num==0:
        break;
    total=total+num
    print("total is :",total)

