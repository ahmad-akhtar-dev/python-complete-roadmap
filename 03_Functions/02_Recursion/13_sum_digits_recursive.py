"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def sum_digits(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)

print(sum_digits(12345))
