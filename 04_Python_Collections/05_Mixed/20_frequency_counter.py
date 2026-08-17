"""
Frequency Counter with Dictionary
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "20_frequency_counter.py"
"""

words = ["python", "java", "python", "web", "python", "java"]
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)

