"""
Generator Function
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_generator_function.py"
"""

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

for number in even_numbers(10):
    print(number)

