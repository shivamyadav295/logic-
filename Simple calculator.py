#ask for two numbers and an operation (+, -, *, or /), then print the result.

a=float(input("Enter tha value of a:"))
b=float(input("Enter the value of b:"))

#creating fuction for different operatons.


# creating function to add number. 
def sum(a,b):
    sum=a+b
    return sum 


# creting function for substract the number.
def sub(a,b):
    sub=a-b
    return sub

#creating function for  product the number.
def pro(a,b):
    product=a*b
    return product

#creating function for devision of th number.
def dev(a,b):
    dev=a/b
    return dev





# function calling for sum function.
print(sum(a,b))

#function calling for sub function.
print(sub(a,b))

#function calling for product function.
print(pro(a,b))

#function calling for devision functiom.
print(dev(a,b))