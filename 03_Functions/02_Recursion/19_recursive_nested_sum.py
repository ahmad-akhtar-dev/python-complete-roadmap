"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def nested_sum(value):
    if isinstance(value, list):
        return sum(nested_sum(item) for item in value)
    return value

print(nested_sum([1, [2, 3], [4, [5]]]))
