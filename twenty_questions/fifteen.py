inp = [1,2,3,2,4,1,5]
count = 0
for num in inp:
    if inp.count(num)>1:
        count += 1
        inp.remove(num)
print(count)
