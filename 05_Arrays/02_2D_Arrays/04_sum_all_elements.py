"""
2D Array: Sum All Elements
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_sum_all_elements.py"
"""

matrix = [[1, 2, 3], [4, 5, 6]]
total = sum(sum(row) for row in matrix)
print("Total:", total)

