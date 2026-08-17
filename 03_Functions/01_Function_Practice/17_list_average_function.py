"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print("Average:", average([10, 20, 30, 40]))
