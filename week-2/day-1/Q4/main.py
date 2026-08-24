# Ask the user for a filename. Check whether the file exists before attempting to open it. Display an appropriate message depending on whether the file exists or not.

filename = input("Enter the filename to check: ")

try:
    file = open(filename, "r")
except:
    print("File Not found")
else:
    print("File Found")

