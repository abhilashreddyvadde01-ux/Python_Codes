# Ask the user for two numbers and divide the first number by the second. Handle division errors, especially when the second number is zero.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(num1/num2)
except ValueError:
    print("Enter numericals not strings")
except ZeroDivisionError:
    print("Cannot divide with Zero.")
else:
    print("Valid calculations")
finally:
    print("Done!!")