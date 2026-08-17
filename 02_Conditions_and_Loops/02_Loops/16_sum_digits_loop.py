"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

number = abs(int(input("Enter a number: ")))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Digit sum =", total)
