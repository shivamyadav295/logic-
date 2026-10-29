'''Input N and print:
1
12
123
'''
num = int(input("Enter a number: "))

i = 1
while i <= num:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1
        