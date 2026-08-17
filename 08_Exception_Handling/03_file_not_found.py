"""
Handle FileNotFoundError
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_file_not_found.py"
"""

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")

