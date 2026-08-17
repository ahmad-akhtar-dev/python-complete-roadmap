"""
Abstraction with ABC
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "13_abstraction.py"
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

print(Circle(3).area())

