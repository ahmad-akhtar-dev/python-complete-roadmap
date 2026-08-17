"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

marks = [70, 80, 90]
print("All passed:", all(mark >= 50 for mark in marks))
print("Any distinction:", any(mark >= 85 for mark in marks))
