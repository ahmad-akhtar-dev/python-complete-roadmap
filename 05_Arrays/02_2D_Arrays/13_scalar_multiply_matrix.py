"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

matrix = [[1,2],[3,4]]
scalar = 3
result = [[value * scalar for value in row] for row in matrix]
print(result)
