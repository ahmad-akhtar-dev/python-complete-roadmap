"""
Common Data Types
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_data_types.py"
"""

age = 20
height = 5.9
name = "Ahmad"
is_student = True
subjects = ["Python", "Java", "Web"]

values = [age, height, name, is_student, subjects]
for value in values:
    print(value, "->", type(value).__name__)

