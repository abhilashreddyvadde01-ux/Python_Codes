inp = 'banana apple mango cherry'
a = inp.split(" ")
key = inp[0]
for item in a:
    if item < key:
        key = item
print(key)