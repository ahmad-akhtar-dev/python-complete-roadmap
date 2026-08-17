"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

age = 15
try:
    assert age >= 18, "Age must be at least 18"
except AssertionError as error:
    print(error)
