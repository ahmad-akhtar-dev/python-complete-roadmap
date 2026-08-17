"""
Raise Your Own Error
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_raise_value_error.py"
"""

marks = int(input("Enter marks 0-100: "))
if not 0 <= marks <= 100:
    raise ValueError("Marks must be between 0 and 100.")
print("Valid marks:", marks)

