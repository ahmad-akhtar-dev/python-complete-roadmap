"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

def is_even(number):
    return number % 2 == 0

value = int(input("Enter a number: "))
print("Even?", is_even(value))
