"""
Instance Method
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "03_instance_method.py"
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shape = Rectangle(5, 3)
print("Area:", shape.area())

