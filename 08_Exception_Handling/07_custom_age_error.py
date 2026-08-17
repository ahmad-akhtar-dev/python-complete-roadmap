"""
Custom Exception
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_custom_age_error.py"
"""

class AgeTooSmallError(Exception):
    pass

age = int(input("Enter age: "))
try:
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18.")
    print("Access allowed.")
except AgeTooSmallError as error:
    print("Access denied:", error)

