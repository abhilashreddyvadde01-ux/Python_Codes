# Given `{"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}`, find the student with the highest marks.

dic = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}

for key, value in dic.items():
    if value == max(dic.values()):
        print(key)