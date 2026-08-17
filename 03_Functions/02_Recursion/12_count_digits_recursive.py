"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def count_digits(number):
    number = abs(number)
    if number < 10:
        return 1
    return 1 + count_digits(number // 10)

print(count_digits(987654))
