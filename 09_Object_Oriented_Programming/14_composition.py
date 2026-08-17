"""
Composition
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "14_composition.py"
"""

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready")

Car().start()

