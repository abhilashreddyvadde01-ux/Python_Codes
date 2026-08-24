# Read a file containing numbers and use a for loop to print only the even numbers.

file = open("Q8/data.py","w+")
sum = 0
content = """5
6
7
8
9
"""
file.write(content)
file.seek(0)

for num in file:
    if int(num)%2==0:
        sum = sum + int(num)

print(sum)