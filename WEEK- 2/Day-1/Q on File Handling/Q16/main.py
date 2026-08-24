# Create a file containing a paragraph. Use read() to count the total number of words.

file = open("Q16/data.txt","w+")
content = "Hi I am Abhilash"
file.write(content)
file.seek(0)
count = 0
for item in file.read().split(" "):
    count = count + 1
print(count)