file = open("Q15/scores.txt","w+")

content = """Rahul 80
Aman 35
Priya 92
Neha 45
"""
file.write(content)
file.seek(0)  # Seek to beginning before reading

for line in file.readlines():
    line = line.strip()
    if line:  # Skip empty lines
        parts = line.split()  # Split by space
        name = parts[0]
        score = int(parts[1])
        if score >= 50:
            print(f"{name} {score}")

file.close()