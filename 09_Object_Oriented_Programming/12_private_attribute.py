"""
Private Attribute
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "12_private_attribute.py"
"""

class User:
    def __init__(self, password):
        self.__password = password

    def verify(self, value):
        return value == self.__password

user = User("python123")
print(user.verify("python123"))

