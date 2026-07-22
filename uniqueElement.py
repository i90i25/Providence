n = int(input("Enter the no. of elements: "))
my_list = []
for i in range(n):
    element = int(input("Enter the element: "))
    my_list.append(element)
    unique_elements = []
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print("Original List: ",my_list)
print("Unique Elements: ",unique_elements)