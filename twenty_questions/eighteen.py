words = ['apple', 'banana', 'kiwi', 'orange', 'grape']
res = []
for item in words:
    if len(item)>5:
        res.append(item)
print(res)