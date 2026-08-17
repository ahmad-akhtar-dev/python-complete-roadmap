"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def count_value(items, target):
    if not items:
        return 0
    return (1 if items[0] == target else 0) + count_value(items[1:], target)

print(count_value([1, 2, 1, 3, 1], 1))
