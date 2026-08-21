text = input()

reversed_text = ""
for character in text:
    reversed_text = character + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")