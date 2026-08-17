"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

try:
    number = int("25")
    try:
        print(number / 0)
    except ZeroDivisionError:
        print("Inner error: division by zero")
except ValueError:
    print("Outer error: invalid number")
