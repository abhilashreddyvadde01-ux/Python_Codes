# Given a dictionary containing student names and marks, calculate the average marks.

dic = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
sum = 0
count = 0
for values in dic.values():
    sum = sum + values
    count += 1
print("Marks average: " , sum/count)