# Create a file containing three lines. Use readline() to read and print each line separately.
file = open("Q5/Data.txt","w+")
content = """Hi
My Name is
Abhlash
"""
file.write(content)
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())

file.close()