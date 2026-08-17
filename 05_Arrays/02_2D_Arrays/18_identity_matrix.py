"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

size = 4
matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
for row in matrix:
    print(row)
