file = open("Q11/details.txt","w+")
content = """
Abhilash
Adithya
Mahendra
Vivek
Nishant
"""
file.write(content)
file.seek(0)
print(file.read())
file.close()