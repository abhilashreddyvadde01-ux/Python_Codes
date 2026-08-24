# Ask the user for a filename and create it using "x" mode. If a file with the same name already exists, handle the situation appropriately.

filename = input("Enter the filename you want to create: ")

try:
    file = open(filename,'x')
except:
    print("Already file existed on this name")
else:
    print("File created successfully")