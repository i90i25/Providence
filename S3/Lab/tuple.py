n = int(input("Enter the no. of tuples: "))
my_list = []
for i in range(n):
    print(f"Enter the elements {i+1}: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    my_list.append((a,b))
print("\nList to be sorted: ")
for t in my_list:
    print(t)
for i in range(n):
    for j in range(0,n -i -1):
        if my_list[j][1]>my_list[j+1][1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
print("\nSorted list: ")
for t in my_list:
    print(t)