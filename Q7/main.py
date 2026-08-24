# Read a file line by line using a for loop and print every line.

file = open("Q7/data.txt","w+")
content = """Name: Abhilash
Age: 22
Course: Python Full Stack"""
file.write(content)
file.seek(0)

for item in file:
    print(item)