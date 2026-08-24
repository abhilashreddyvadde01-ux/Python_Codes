# Take a sentence and find the longest word in it.
lis = []
sentence = input("Enter your sentence: ").split(" ")
for word in sentence:
    lis.append(len(word))
print(sentence[lis.index(max(lis))])