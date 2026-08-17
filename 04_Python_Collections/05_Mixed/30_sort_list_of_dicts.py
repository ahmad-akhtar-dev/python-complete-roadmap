"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

students = [{"name": "Ali", "marks": 80}, {"name": "Sara", "marks": 92}]
print(sorted(students, key=lambda s: s["marks"], reverse=True))
