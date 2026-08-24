# Create a simple student record program that asks for name, age, and marks, writes them to student.txt, and then reads the file and displays the information.

file = open("Q19/details.txt","a+")

for i in range(1,5):
    name = input(f"Enter candidate- {i} name: ")
    age = input(f"Enter candidate- {i} age: ")
    marks = input(f"Enter candidate- {i} marks: ")
    file.write(name + ' ' + age + ' ' + marks + "\n")
file.seek(0)

print(file.read())
file.close()