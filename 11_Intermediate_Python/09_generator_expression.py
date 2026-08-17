"""
Generator Expression
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_generator_expression.py"
"""

squares = (n ** 2 for n in range(1, 6))
for value in squares:
    print(value)

