"""
Continue Statement: Skip Multiples
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_continue_skip_multiples.py"
"""

for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)

