dict1 = {"apple": 3, "banana": 2, "mango": 1}
dict2 = {"avengers": 7, "batman": 20, "mazza": 12}
for key,value in dict2.items():
    dict1[key] = value
print(dict1)