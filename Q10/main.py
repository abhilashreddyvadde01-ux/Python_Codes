# Read a file containing numbers and find the largest and smallest number using a for loop.

file = open("Q10/data.py","w+")
sum = 0
content = """5
6
7
8
9
4
6
7
9
4
2
3
4
5
"""
file.write(content)
file.seek(0)
min = 0
max = 0
for num in file:
    if int(num)>max:
        max = int(num)
    if int(num)<min:
            min = int(num)

print(f"Maximum number is : {max}")
print(f"Minimum number is : {min}")