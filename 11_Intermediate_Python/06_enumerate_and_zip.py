"""
enumerate() and zip()
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_enumerate_and_zip.py"
"""

names = ["Ahmad", "Ali", "Sara"]
marks = [88, 75, 92]
for index, (name, score) in enumerate(zip(names, marks), start=1):
    print(index, name, score)

