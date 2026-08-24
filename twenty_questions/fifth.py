N = int(input("Enter the value of N: "))
res = ""
for i in range(1, N+1):
    if i%3 == 0 and i%5 == 0:
        res = res + " " + str(i)
print(res)