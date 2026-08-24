file = open("Q4/data.py","w+")
sum = 0
content = """5
6
7
8
9
"""
file.write(content)
file.seek(0)
for num in file.readlines():
    sum = sum + int(num)
print(sum)
file.close()