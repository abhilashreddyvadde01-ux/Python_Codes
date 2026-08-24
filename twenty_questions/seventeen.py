numbers = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
sum =0
for outer in numbers:
    for num in outer:
        sum = sum + num

print(sum)