"""
1D Array: Second Largest
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_second_largest.py"
"""

numbers = [10, 30, 20, 50, 40]
unique = sorted(set(numbers), reverse=True)
print("Second largest:", unique[1] if len(unique) > 1 else "Not available")

