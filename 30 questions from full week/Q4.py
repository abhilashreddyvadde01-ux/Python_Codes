# Take three numbers as input and print the largest number.
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a>b and a>c:
    print("a")
elif b>a and b>c:
    print("b")
else:
    print("c")