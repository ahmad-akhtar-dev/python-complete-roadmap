"""
Calculator with Functions
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_function_calculator.py"
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

