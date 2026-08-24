# Take 5 numbers from the user and write them into a file, one number per line.

# Take 5 names from the user using input() and write them into a file.

file = open("Q14/names.txt","a+")
for i in range(5):
    file.write(input() + "\n")
file.seek(0)
print(file.read())
file.close()
    