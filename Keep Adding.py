#keep adding - keep asking for numbers until the user enter 0, then pront their total.
print("This program will keep asking for numbers until you enter 0; then it will print the total of all the number you entered.")
total=0
while True:
    num=float(input("Enter a number:"))
    if num==0:
        break;
    total=total+num
print(" The total of the numbers entered by you is :",total)
