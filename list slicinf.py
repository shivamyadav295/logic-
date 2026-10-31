no_of_element = int(input("Enter the number of elements in list: "))

i = 0
value = []

while i < no_of_element:
    element = input("Enter the element of list: ")
    value.append(element)
    i += 1

value = tuple(value)

print("List ke pehle 3 marks hain:", value[:3])
print("List ke pehle 5 marks hain:", value[:5])
print("List from index 0 to n:", value[0:len(value)])
print("Reverse indexing:", value[-1:-4:-1])
print("Reverse indexing:", value[-4:-1:1])
print("Slicing difference in indexing is 2:", value[0:6:2])
print("Negative slicing if list difference of 2:", value[-1:-7:-2])
print("Length of list is:", len(value))
print("Maximum number present in list is:", max(value))
print("Minimum number present in list is:", min(value))
print("Sum of all elements present in list is:", sum(value))
print("sorting of element present in list :",sorted(value))
rem=int(input("Enter the no to remove form list :"))
if rem in value :
     temp=list(value)
     temp.remove(rem)
     value=temp
     print("touple after removing element form list :",value)
else:
    print(rem,"element not found in list.")
    print("retry")

