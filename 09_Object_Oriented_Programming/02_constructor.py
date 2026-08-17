"""
Constructor __init__
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "02_constructor.py"
"""

class Student:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester

student = Student("Ahmad", 4)
print(student.name, student.semester)

