# Given a list of numbers, use a set to find all the duplicate elements.
numbers = [1,2,4,32,1,5,76,4,32]
dup = set()
seen = set()
for num in numbers:
    if num in seen:
        dup.add(num)
    else:
        seen.add(num)
print(dup)