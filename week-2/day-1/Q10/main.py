
try:
    filename = input("Enter the filename: ")
    number = int(input("Enter a number: "))

    with open(filename, "r") as file:
        content = file.read()

    print("Number:", number)
    print("File content:")
    print(content)

except ValueError:
    print("Please enter a valid number.")
except FileNotFoundError:
    print("File not found.")