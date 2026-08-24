# Read a file containing names and print only names whose length is greater than 5.

file = open("Q9/details.txt","w+")
content = """
Abhilash
Adithya
Mahendra
abhi
lash
Vivek
Nishant
"""
file.write(content)
file.seek(0)
for item in file.readlines():
    if len(item)>5:
        print(item)
file.close()