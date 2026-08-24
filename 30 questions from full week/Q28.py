# Write a function find_largest(numbers) that takes a list of numbers and returns the largest number without using max(). Take input and display the result.
numbers = map(int, input("Enter string of numbers: ").split())
def find_largest(numbers):
    max = 0
    for num in numbers:
        if num>max:
            max = num
    print(max)
find_largest(numbers)