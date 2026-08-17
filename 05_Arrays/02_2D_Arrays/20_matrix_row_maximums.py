"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

matrix = [[1,8,3],[4,2,9],[7,6,5]]
for index, row in enumerate(matrix, 1):
    print(f"Row {index} max = {max(row)}")
