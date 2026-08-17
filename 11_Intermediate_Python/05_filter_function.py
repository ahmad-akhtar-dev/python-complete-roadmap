"""
filter()
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_filter_function.py"
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)

