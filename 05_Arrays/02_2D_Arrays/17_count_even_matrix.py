"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

matrix = [[1,2,3],[4,5,6]]
count = sum(1 for row in matrix for value in row if value % 2 == 0)
print(count)
