# Create a file and write numbers from 1 to 10, with each number on a separate line.

file = open("Q12/numbers.txt","a+")
for i in range(10):
    file.write(str(i) )
    file.write("\n")
file.seek(0)
for i in file.readlines():
    print(i)
file.close()