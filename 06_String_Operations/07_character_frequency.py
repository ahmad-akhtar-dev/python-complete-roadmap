"""
Character Frequency
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_character_frequency.py"
"""

text = "banana"
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

