"""
Multilevel Inheritance
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "07_multilevel_inheritance.py"
"""

class Animal:
    def eat(self): print("Eating")

class Mammal(Animal):
    def walk(self): print("Walking")

class Dog(Mammal):
    def bark(self): print("Barking")

dog = Dog()
dog.eat(); dog.walk(); dog.bark()

