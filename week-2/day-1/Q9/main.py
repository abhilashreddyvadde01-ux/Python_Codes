# Ask the user for a filename and attempt to open it in read mode. Handle the situation where the file does not exist.

filename = input("Enter the file name: ")
try:
    file = open(filename, 'r')
except FileNotFoundError:
    print("File Not Found")
else:
    print("File Found")
    file.close()