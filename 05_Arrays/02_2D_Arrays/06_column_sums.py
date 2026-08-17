"""
2D Array: Column Sums
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_column_sums.py"
"""

matrix = [[1, 2, 3], [4, 5, 6]]
for col in range(len(matrix[0])):
    total = sum(matrix[row][col] for row in range(len(matrix)))
    print(f"Column {col + 1} sum:", total)

