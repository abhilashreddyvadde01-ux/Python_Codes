age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")
if age>=18 and has_id == 'yes':
    print("Allowed")
else:
    print("Not allowed")