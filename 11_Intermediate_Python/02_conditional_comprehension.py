"""
Conditional List Comprehension
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "02_conditional_comprehension.py"
"""

numbers = range(1, 21)
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)

