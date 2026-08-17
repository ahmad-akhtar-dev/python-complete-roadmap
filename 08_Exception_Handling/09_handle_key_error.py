"""
Handle KeyError
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_handle_key_error.py"
"""

student = {"name": "Ahmad", "marks": 88}
try:
    print(student["city"])
except KeyError as error:
    print("Missing key:", error)

