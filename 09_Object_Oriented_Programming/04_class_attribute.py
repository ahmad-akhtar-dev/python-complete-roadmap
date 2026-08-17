"""
Class Attribute
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "04_class_attribute.py"
"""

class Student:
    university = "My University"

    def __init__(self, name):
        self.name = name

first = Student("Ahmad")
second = Student("Sara")
print(first.university)
print(second.university)

