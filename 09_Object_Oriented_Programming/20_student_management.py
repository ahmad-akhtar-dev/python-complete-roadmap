"""
Mini OOP Project: Student Management
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "20_student_management.py"
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        return "A" if self.marks >= 80 else "B" if self.marks >= 70 else "C"

students = [Student("Ahmad", 88), Student("Ali", 74), Student("Sara", 93)]
for student in students:
    print(student.name, student.marks, student.grade())

