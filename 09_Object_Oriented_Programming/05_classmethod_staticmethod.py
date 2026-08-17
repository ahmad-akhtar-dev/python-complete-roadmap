"""
Class Method and Static Method
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "05_classmethod_staticmethod.py"
"""

class Temperature:
    unit = "Celsius"

    @classmethod
    def show_unit(cls):
        return cls.unit

    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32

print(Temperature.show_unit())
print(Temperature.c_to_f(25))

