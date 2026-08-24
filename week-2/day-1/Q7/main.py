# Ask the user to enter two numbers and calculate their sum. Handle the situation where the user enters text instead of a number using try-except.

try:
    num1 = float(input("Enter number-1: "))
    num2 = float(input("Enter number-2: "))
    print(f"The sum of {num1} and {num2} is {num1+num2}")
except ValueError:
    print("It is ValuError")
                 