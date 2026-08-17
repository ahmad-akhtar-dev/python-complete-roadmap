"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

number = int(input("Enter a positive number: "))
digits = str(number)
power = len(digits)
total = 0
for digit in digits:
    total += int(digit) ** power
print("Armstrong number" if total == number else "Not an Armstrong number")
