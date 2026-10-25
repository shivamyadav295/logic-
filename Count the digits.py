#Ask for a whole number and count how many digits it has.
num = int(input("Enter a whole number: "))
real = num
i = 0

if num < 0:
    num = -num

if num == 0:
    i = 1
else:
    while num > 0:
        num = num // 10
        i = i + 1

print(i)
print("sonu")


