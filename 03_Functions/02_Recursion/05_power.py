"""
Recursive Power
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_power.py"
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))

