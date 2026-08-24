file = open("Q3/details.txt","w+")
content = """
Abhilash
Adithya
Mahendra
Vivek
Nishant
"""
file.write(content)
file.seek(0)
for item in file.readlines():
    print(item)
file.close()