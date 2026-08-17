"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]
print("Even:", evens)
print("Odd:", odds)
