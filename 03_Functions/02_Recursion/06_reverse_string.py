"""
Reverse String Recursively
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_reverse_string.py"
"""

def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print(reverse_text("Python"))

