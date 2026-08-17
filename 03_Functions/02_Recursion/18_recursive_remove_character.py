"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def remove_character(text, target):
    if not text:
        return ""
    first = "" if text[0] == target else text[0]
    return first + remove_character(text[1:], target)

print(remove_character("banana", "a"))
