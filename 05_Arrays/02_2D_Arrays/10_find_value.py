"""
2D Array: Find a Value
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_find_value.py"
"""

matrix = [[3, 8, 1], [4, 7, 6], [9, 2, 5]]
target = 7
found = None
for r, row in enumerate(matrix):
    for c, value in enumerate(row):
        if value == target:
            found = (r, c)
            break
    if found:
        break
print("Position:", found)

