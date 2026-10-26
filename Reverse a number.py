num = int(input("Enter a number: "))
rev = 0

while num > 0:
    mod = num % 10
    rev = rev * 10 + mod
    num = num // 10
    print(rev)

print("reverse of this no is :", rev)
