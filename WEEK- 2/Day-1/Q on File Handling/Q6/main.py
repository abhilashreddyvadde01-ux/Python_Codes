file = open("Q6/data.txt","w+")
content = """Name: Abhilash
Age: 22
Course: Python Full Stack"""
file.write(content)
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
file.close()