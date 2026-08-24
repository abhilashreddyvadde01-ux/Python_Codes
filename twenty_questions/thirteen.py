numbers = [12, 5, 8, 21, 4, 15, 10]
max = numbers[0]
min = numbers[0]
sum = 0
for num in numbers:
    if num > max:
        max = num

for num in numbers:
    if num < min:
        min = num
for num in numbers:
    sum = sum + num
print(max)
print(min)
print(sum)