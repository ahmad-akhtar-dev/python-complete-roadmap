"""
Aggregation
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "15_aggregation.py"
"""

class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teacher):
        self.teacher = teacher

teacher = Teacher("Mr. Ali")
department = Department(teacher)
print(department.teacher.name)

