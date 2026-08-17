"""
Return Multiple Values
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_multiple_return_values.py"
"""

def calculate(a, b):
    return a + b, a - b, a * b

sum_value, difference, product = calculate(10, 4)
print(sum_value, difference, product)

