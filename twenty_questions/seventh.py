n =  input("Enter the value of n: ")
count = 0
for i in n:
    if int(i) % 2 == 0:
        count = count + 1
print(count)