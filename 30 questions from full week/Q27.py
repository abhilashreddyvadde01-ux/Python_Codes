# Write a function is_prime(n) that returns True if a number is prime and False otherwise. Take input and display the result.

def is_prime(n):
    flag = True
    for num in range(2,n):
        if n%num == 0:
            print("It is not prime number")
            flag = False
            break
    if flag:
        print("It is a Prime Number")
is_prime(19)
