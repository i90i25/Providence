m = int(input("Enter a number: "))
n = int(input("Enter a number: "))
square_even = {i*i for i in range(m,n+1) if i%2==0}
print("Square of even number",square_even)