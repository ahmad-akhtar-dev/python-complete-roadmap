"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def recursive_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    rest_max = recursive_max(numbers[1:])
    return numbers[0] if numbers[0] > rest_max else rest_max

print(recursive_max([4, 18, 7, 25, 3]))
