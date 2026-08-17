"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

students = [{"name": "Ali", "marks": 45}, {"name": "Sara", "marks": 90}]
passed = [s for s in students if s["marks"] >= 50]
print(passed)
