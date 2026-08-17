"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

students = [{"name": "Ali", "grade": "A"}, {"name": "Sara", "grade": "A"}, {"name": "Hamza", "grade": "B"}]
groups = {}
for student in students:
    groups.setdefault(student["grade"], []).append(student["name"])
print(groups)
