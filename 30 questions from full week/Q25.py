# Take a sentence as input and create a dictionary containing the frequency of each word.
sentence = input("Enter your string: ").split()
dic = {}
for item in sentence:
    if item not in dic.keys():
        dic[item] = sentence.count(item)
print(dic)
