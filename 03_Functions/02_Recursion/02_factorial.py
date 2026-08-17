"""
Recursive Factorial
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "02_factorial.py"
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

