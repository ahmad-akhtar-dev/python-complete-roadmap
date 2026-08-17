"""
2D Array: Matrix Addition
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_add_matrices.py"
"""

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
result = [[a[r][c] + b[r][c] for c in range(2)] for r in range(2)]
print(result)

