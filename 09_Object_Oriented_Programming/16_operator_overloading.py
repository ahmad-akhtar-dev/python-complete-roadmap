"""
Operator Overloading
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "16_operator_overloading.py"
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(1, 2) + Point(3, 4))

