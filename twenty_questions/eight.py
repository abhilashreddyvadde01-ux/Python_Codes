inp = 'Python is very easy to learn'
a = inp.split(" ")
print(len(a))
for item  in a:
    if item == 'easy':
        a[a.index(item)] = 'powerful'
print(" ".join(a).upper())
