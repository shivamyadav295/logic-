my_list = []
i = 0

n = int(input("Enter the number of elements in the list: "))

while i < n:
    element = input("Enter an element: ")
    my_list.append(element)
    i += 1

print("Elements of the list are:", my_list)

my_list.sort()
print("Sorting of list:", my_list)

my_list.reverse()
print("Reverse of list is:", my_list)

inx = int(input("Enter index to insert at: "))
value = int(input("Enter value to insert: "))
my_list.insert(inx, value)
print("List after inserting an element:", my_list)

remove = int(input("Enter a value present in list to remove: "))
my_list.remove(remove)
print("List after removing element:", my_list)

pop = int(input("Enter the index to remove the element: "))
my_list.pop(pop)
print(my_list)