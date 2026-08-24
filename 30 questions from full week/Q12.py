# Take a number and check whether it is a prime number.
num = int(input("Enter the number to check: "))
flag = True
for i in range(2,num):
    if num%i == 0:
        print("It is not prime")
        flag = False
if flag:
    print("It is prime")