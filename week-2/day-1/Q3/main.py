# Create a file containing some old information. Ask the user for new information and use "w" mode to replace the old content completely. Read the file afterward to verify the change
# Create students.txt with 3 student names. Ask the user for 2 additional names and append them to the same file without deleting the existing names.

file = open("Q2/data.txt","w+")

name1 = input("Enter a student name: ")
name2 = input("Enter other student name: ")
file.write('\n' + name1)
file.write("\n" + name2)
file.seek(0)
print(file.read())
file.close()