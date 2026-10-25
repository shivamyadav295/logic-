#Choose a secret number. Keep asking the user to guess until they get it right
i=0
while i<=100 :
    num=int(input("GUESS THE NUMBER BETWEEN 1 TO 100:"))
    if num==14:
        print("yes it is a correct number")
        break
    else:
        i=i+1
print("thankyou")




