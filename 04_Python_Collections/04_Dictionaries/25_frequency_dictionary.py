"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

text = "banana"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)
