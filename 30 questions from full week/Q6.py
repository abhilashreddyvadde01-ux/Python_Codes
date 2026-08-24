# Take a string and print it in reverse without using a built-in reverse function.

text = input("Enter your string")
reversed_text = ""
for character in text:
    reversed_text = character + reversed_text
print(reversed_text)
