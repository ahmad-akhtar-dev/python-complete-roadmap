"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def to_binary(number):
    if number < 2:
        return str(number)
    return to_binary(number // 2) + str(number % 2)

print(to_binary(25))
