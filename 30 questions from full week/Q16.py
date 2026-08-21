# Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
lis =  [10, 20, 10, 30, 20, 40, 30]
res = []
for item in lis:
    if item not in res:
        res.append(item)
print(res)
 