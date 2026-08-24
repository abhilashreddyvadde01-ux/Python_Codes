# Given a tuple of numbers, find the sum, maximum, and minimum values.
tup = (2,4,7,3,4,7,9,2)
sum =0
print(max(tup))
print(min(tup))
for num in tup:
    sum += num
print(sum)