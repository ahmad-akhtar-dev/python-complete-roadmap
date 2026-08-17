"""
Robust Calculator
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_robust_calculator.py"
"""

try:
    a = float(input("A: "))
    operator = input("Operator (+, -, *, /): ")
    b = float(input("B: "))
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        raise ValueError("Unsupported operator")
    print("Result:", result)
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
finally:
    print("Calculator finished.")

