"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

word = input("Enter a word: ")
count = 0
for character in word:
    if character.isalpha():
        count += 1
print("Alphabetic characters =", count)
