# Take a string as input and count the number of vowels in it.
string = input("Enter your string: ")
count = 0
string.lower()
for char in string:
    if char in ["a","e","i","o","u"]:
        count += 1
print("The number of vowels in it are: " + str(count))