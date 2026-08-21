# Take a number n and print its multiplication table from 1 to 10.
num = int(input("Enter the num to print its table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")