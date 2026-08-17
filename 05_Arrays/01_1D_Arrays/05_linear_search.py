"""
1D Array: Linear Search
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_linear_search.py"
"""

numbers = [4, 7, 12, 19, 25]
target = 19
position = -1
for i, number in enumerate(numbers):
    if number == target:
        position = i
        break
print("Index:", position)

