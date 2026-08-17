"""
Multiple Exception Types
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_multiple_exceptions.py"
"""

try:
    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))
    divisor = int(input("Enter divisor: "))
    print(numbers[index] / divisor)
except ValueError:
    print("Please enter integers.")
except IndexError:
    print("Index is outside the list.")
except ZeroDivisionError:
    print("Divisor cannot be zero.")

