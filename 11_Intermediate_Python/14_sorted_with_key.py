"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

students = [("Ali", 80), ("Sara", 92), ("Ahmad", 88)]
print(sorted(students, key=lambda item: item[1], reverse=True))
