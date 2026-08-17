"""
Keep Asking Until Integer
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "02_integer_input_loop.py"
"""

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("That was not a whole number. Try again.")
print("Age:", age)

