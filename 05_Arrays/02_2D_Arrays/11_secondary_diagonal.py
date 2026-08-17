"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
size = len(matrix)
print([matrix[i][size - 1 - i] for i in range(size)])
