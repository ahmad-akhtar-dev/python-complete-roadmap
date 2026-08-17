"""
Method Overriding
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "09_method_overriding.py"
"""

class Animal:
    def sound(self): print("Animal sound")

class Cat(Animal):
    def sound(self): print("Meow")

Cat().sound()

