# Given {"a": 10, "b": 20, "c": 30}, find the sum of all values

sides = {"a": 10, "b": 20, "c": 30}
sum = 0
for values in sides.values():
    sum = sum + values
print(sum)