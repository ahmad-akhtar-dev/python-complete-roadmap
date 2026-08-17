"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

student = Student(88)
print(student.marks)
