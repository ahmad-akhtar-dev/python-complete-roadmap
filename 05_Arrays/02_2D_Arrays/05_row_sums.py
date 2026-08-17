"""
2D Array: Row Sums
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_row_sums.py"
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for index, row in enumerate(matrix, start=1):
    print(f"Row {index} sum:", sum(row))

