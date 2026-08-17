"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

numbers = [1, 2, 3, 2, 4, 1, 5]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print("Duplicates:", duplicates)
