"""
Count Vowels
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_count_vowels.py"
"""

text = input("Enter text: ").lower()
count = sum(1 for ch in text if ch in "aeiou")
print("Vowels:", count)

