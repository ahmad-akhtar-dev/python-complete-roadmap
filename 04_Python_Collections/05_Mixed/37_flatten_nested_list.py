"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

nested = [[1, 2], [3, 4], [5]]
flat = [item for row in nested for item in row]
print(flat)
