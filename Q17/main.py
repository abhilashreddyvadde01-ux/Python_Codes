# Create a file containing 10 numbers. Use readlines() to calculate their average.

file = open("Q17/numbers.txt","w+")

content = """1
2
3
4
5
6
7
8
9
10"""
file.write(content)
file.seek(0)
sum = 0
count =0

for num in file.readlines():
    sum += int(num)
    count += 1
print(f"The average of those ten numbers is {sum/count}")



