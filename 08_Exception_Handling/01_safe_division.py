"""
Try and Except: Safe Division
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "01_safe_division.py"
"""

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")

