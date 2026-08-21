# Given a list, create a new list containing only the even numbers.

lis = [1,2,3,4,5,6,7,8,9]
res = []
for num in lis:
    if num%2 == 0:
        res.append(num)

print(res)
