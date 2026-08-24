# Ask the user for a filename and delete that file. If the file doesn’t exist, display an appropriate message instead of allowing the program to crash.

import os

filename = input("Enter the filename to delete: ")

try:
    os.remove(filename)
    print("File deleted successfully.")
except FileNotFoundError:
    print("File not found.")