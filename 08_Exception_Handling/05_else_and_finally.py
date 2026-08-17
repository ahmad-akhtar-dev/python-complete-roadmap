"""
Else and Finally
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_else_and_finally.py"
"""

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer.")
else:
    print("You entered:", number)
finally:
    print("This line always runs.")

