"""
Polymorphism with Duck Typing
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "10_polymorphism_duck_typing.py"
"""

class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.speak())

