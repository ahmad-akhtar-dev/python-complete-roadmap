"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(inverted)
