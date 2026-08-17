"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

number = 10
try:
    number.append(5)
except AttributeError:
    print("Integers do not have append().")
