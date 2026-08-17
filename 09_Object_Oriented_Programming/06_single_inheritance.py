"""
Single Inheritance
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "06_single_inheritance.py"
"""

class Person:
    def speak(self):
        print("Person can speak.")

class Student(Person):
    def study(self):
        print("Student is studying.")

student = Student()
student.speak()
student.study()

