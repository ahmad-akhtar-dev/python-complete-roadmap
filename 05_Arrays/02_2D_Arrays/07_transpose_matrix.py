"""
2D Array: Transpose
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_transpose_matrix.py"
"""

matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [list(row) for row in zip(*matrix)]
for row in transpose:
    print(row)

