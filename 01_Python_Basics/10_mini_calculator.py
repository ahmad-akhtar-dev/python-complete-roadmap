"""
Mini Calculator
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_mini_calculator.py"
"""

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Sum:", first + second)
print("Difference:", first - second)
print("Product:", first * second)
if second != 0:
    print("Division:", first / second)
else:
    print("Division by zero is not allowed.")

