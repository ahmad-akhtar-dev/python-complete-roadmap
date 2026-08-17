"""
Custom Iterator
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_custom_iterator.py"
"""

class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for number in Counter(5):
    print(number)

