#Skip Counting — Input a step and a limit. Print multiples of the step up to the limit.
step=int(input("enter a step:"))
limit=int(input("enter a limit:"))
num=step
while num<=limit:
    print(num)
    num = num+step