"""
Variable Positional Arguments
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_args.py"
"""

def total_marks(*marks):
    return sum(marks)

print(total_marks(70, 80, 90))
print(total_marks(55, 65, 75, 85))

