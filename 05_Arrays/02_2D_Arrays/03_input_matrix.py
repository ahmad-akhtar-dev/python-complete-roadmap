"""
2D Array: User Input
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_input_matrix.py"
"""

rows = 2
cols = 3
matrix = []
for r in range(rows):
    row = list(map(int, input(f"Enter {cols} values for row {r + 1}: ").split()))
    matrix.append(row[:cols])
print(matrix)

