# Write a recursive function to find the sum of numbers from 1 to n.

n = int(input("Enter the value of n: "))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
print(sum(n))