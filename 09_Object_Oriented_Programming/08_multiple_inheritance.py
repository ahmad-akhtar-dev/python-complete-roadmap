"""
Multiple Inheritance
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "08_multiple_inheritance.py"
"""

class Camera:
    def take_photo(self): print("Photo taken")

class Phone:
    def call(self): print("Calling")

class SmartPhone(Camera, Phone):
    pass

device = SmartPhone()
device.take_photo(); device.call()

