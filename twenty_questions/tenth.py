inp = input("Enter a string: ")
inp = inp.lower()
countvowels = 0
countconso = 0
countdigits = 0
for item in inp:
    if item.isalpha():
        if item in ('a', 'e', 'i', 'o', 'u'):
            countvowels += 1
        else:
            countconso += 1

    if item.isdigit():
        countdigits += 1

print(f"Number of vowels: {countvowels}")
print(f"Number of consonants: {countconso}")
print(f"Number of digits: {countdigits}")