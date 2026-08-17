"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

try:
    value = int("abc")
except ValueError as error:
    message = f"Handled error: {error}"
    print(message)
