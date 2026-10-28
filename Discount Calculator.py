#nput a shopping amount. Apply a 10% discount if it is ₹1,000 or more; otherwise, print the original amount.
amount=float(input("Enter the total amount:"))
if amount >1000:
    tenper=amount/100*10
    finalamount=amount-tenper
    print("Total amount to pay:",finalamount)
else:
    print("Your cart amount is less than 1000 so you are not eligble for 10% discount.")
