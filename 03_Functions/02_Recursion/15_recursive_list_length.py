"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def list_length(items):
    if not items:
        return 0
    return 1 + list_length(items[1:])

print(list_length([10, 20, 30, 40]))
