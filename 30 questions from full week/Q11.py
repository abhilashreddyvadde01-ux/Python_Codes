# Take a number and find the sum of its digits.
sum = 0
num = input("Enter your number: ")
for digit in num:
    sum = sum + int(digit)

print(sum)