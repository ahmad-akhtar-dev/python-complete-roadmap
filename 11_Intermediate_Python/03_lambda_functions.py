"""
Lambda Functions
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_lambda_functions.py"
"""

double = lambda number: number * 2
print(double(8))
students = [("Ali", 75), ("Ahmad", 88), ("Sara", 92)]
print(sorted(students, key=lambda item: item[1], reverse=True))

