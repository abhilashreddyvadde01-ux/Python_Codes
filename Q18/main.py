# Create a file containing several names. Read the file using a for loop and count how many names are present.

file = open("Q18/names.txt", "w+")

content = """a
b
c
d
e
f
g
h
"""
file.write(content)
file.seek(0)
count = 0

for name in file.readlines():
    count += 1
print(count)