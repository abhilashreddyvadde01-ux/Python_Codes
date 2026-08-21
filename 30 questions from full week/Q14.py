# Given a list of numbers, find the largest and smallest element without using max() or min().

lis = [3,43,34,54,3,32,21]
lis.sort()
print("The largest number: "+  str(lis[0]))
print("The smallest number: "+ str(lis[len(lis)-1]))