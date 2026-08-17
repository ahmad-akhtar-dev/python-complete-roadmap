"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index not available"

print(safe_get([10, 20, 30], 5))
