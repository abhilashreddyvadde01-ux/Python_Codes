# Create notes.txt containing some text. Take a new sentence from the user and append it to the existing file using "a" mode. Then read and display the complete file.

file = open("Q1/data.txt","a+")

content = input("Enter the content, you wish to add to the text file:  ")
file.write(content)
file.seek(0)
print(file.read())