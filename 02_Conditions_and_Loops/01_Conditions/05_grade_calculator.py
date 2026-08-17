"""
Grade Calculator
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_grade_calculator.py"
"""

marks = float(input("Enter marks from 0 to 100: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

