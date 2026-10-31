'''Print numbers from 1 to 30. For multiples of 3 print “Fizz”,
 for multiples of 5 print “Buzz”,
and for multiples of both print “FizzBuzz”.'''


num=int(input("Enter the no for ranage from 0 to ?:"))
i=1
while i<=num:
    if i%3==0 and i%5==0:
        print("fizzBuzz")
   
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("fizzBuzz")
    else:
        print(i)
    i+=1
print("Thankyou got using my code")
