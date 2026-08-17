"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def product(numbers):
    if not numbers:
        return 1
    return numbers[0] * product(numbers[1:])

print(product([2, 3, 4]))
