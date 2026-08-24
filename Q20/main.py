# Create a program that:

# Takes 5 student names from the user.
# Writes them to a file.
# Reads the file using a for loop.
# Prints each student with a serial number

file = open("Q20/names.txt","a+")

for i in range(1,6):
    name = input(f"Enter candidate- {i} name: ")
    file.write(str(i) + ")"  + ' ' + name + '\n')
file.seek(0)
print(file.read())
file.close()
